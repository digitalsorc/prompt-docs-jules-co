"""
Queue Manager Module
Handles job queuing, parallel processing, and job lifecycle management.
"""

import os
import time
import uuid
import threading
import queue
from concurrent.futures import ThreadPoolExecutor, Future
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass, field, asdict
from enum import Enum
from datetime import datetime
import json

from .converter import DocumentConverter, ConversionConfig, ConversionResult, ConversionStatus


@dataclass
class ConversionJob:
    """Represents a document conversion job."""
    job_id: str
    filename: str
    original_path: str
    file_size: int
    status: ConversionStatus = ConversionStatus.PENDING
    progress: float = 0.0
    message: str = ""
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    started_at: Optional[str] = None
    completed_at: Optional[str] = None
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert job to dictionary."""
        return asdict(self)


@dataclass
class QueueStatus:
    """Status of the conversion queue."""
    total_jobs: int = 0
    pending: int = 0
    in_progress: int = 0
    completed: int = 0
    failed: int = 0
    is_paused: bool = False
    is_processing: bool = False
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert status to dictionary."""
        return asdict(self)


class QueueManager:
    """Manages the document conversion queue and worker pool."""
    
    def __init__(
        self,
        max_workers: int = 4,
        output_dir: str = "converted_output",
        config: Optional[ConversionConfig] = None
    ):
        """Initialize the queue manager.
        
        Args:
            max_workers: Maximum number of parallel workers
            output_dir: Directory to save converted files
            config: Default conversion configuration
        """
        self.max_workers = max_workers
        self.output_dir = output_dir
        self.config = config or ConversionConfig()
        
        # Job storage
        self._jobs: Dict[str, ConversionJob] = {}
        self._job_order: List[str] = []  # Maintain order
        
        # Threading primitives
        self._lock = threading.Lock()
        self._executor: Optional[ThreadPoolExecutor] = None
        self._futures: Dict[str, Future] = {}
        
        # Queue control
        self._is_paused = False
        self._is_processing = False
        
        # Callbacks
        self._on_job_update: Optional[Callable[[ConversionJob], None]] = None
        self._on_queue_update: Optional[Callable[[QueueStatus], None]] = None
        
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
    
    def set_job_update_callback(self, callback: Callable[[ConversionJob], None]) -> None:
        """Set callback for job status updates."""
        self._on_job_update = callback
    
    def set_queue_update_callback(self, callback: Callable[[QueueStatus], None]) -> None:
        """Set callback for queue status updates."""
        self._on_queue_update = callback
    
    def _notify_job_update(self, job: ConversionJob) -> None:
        """Notify about job update."""
        if self._on_job_update:
            try:
                self._on_job_update(job)
            except Exception:
                pass
    
    def _notify_queue_update(self) -> None:
        """Notify about queue update."""
        if self._on_queue_update:
            try:
                self._on_queue_update(self.get_status())
            except Exception:
                pass
    
    def add_job(self, filepath: str, filename: Optional[str] = None) -> ConversionJob:
        """Add a new conversion job to the queue.
        
        Args:
            filepath: Path to the file to convert
            filename: Optional filename override
            
        Returns:
            Created ConversionJob
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        
        if filename is None:
            filename = os.path.basename(filepath)
        
        file_size = os.path.getsize(filepath)
        job_id = str(uuid.uuid4())
        
        job = ConversionJob(
            job_id=job_id,
            filename=filename,
            original_path=filepath,
            file_size=file_size,
            status=ConversionStatus.PENDING,
            message="Waiting in queue"
        )
        
        with self._lock:
            self._jobs[job_id] = job
            self._job_order.append(job_id)
        
        self._notify_job_update(job)
        self._notify_queue_update()
        
        return job
    
    def add_jobs(self, filepaths: List[str]) -> List[ConversionJob]:
        """Add multiple conversion jobs to the queue.
        
        Args:
            filepaths: List of file paths to convert
            
        Returns:
            List of created ConversionJobs
        """
        jobs = []
        for filepath in filepaths:
            try:
                job = self.add_job(filepath)
                jobs.append(job)
            except FileNotFoundError:
                # Skip non-existent files
                continue
        return jobs
    
    def remove_job(self, job_id: str) -> bool:
        """Remove a job from the queue.
        
        Args:
            job_id: ID of job to remove
            
        Returns:
            True if removed, False if not found or in progress
        """
        with self._lock:
            if job_id not in self._jobs:
                return False
            
            job = self._jobs[job_id]
            if job.status == ConversionStatus.IN_PROGRESS:
                # Cancel the future if possible
                if job_id in self._futures:
                    self._futures[job_id].cancel()
            
            del self._jobs[job_id]
            if job_id in self._job_order:
                self._job_order.remove(job_id)
            if job_id in self._futures:
                del self._futures[job_id]
        
        self._notify_queue_update()
        return True
    
    def clear_completed(self) -> int:
        """Remove all completed and failed jobs from the queue.
        
        Returns:
            Number of jobs removed
        """
        removed = 0
        with self._lock:
            to_remove = [
                job_id for job_id, job in self._jobs.items()
                if job.status in [ConversionStatus.COMPLETED, ConversionStatus.FAILED, ConversionStatus.CANCELLED]
            ]
            for job_id in to_remove:
                del self._jobs[job_id]
                if job_id in self._job_order:
                    self._job_order.remove(job_id)
                removed += 1
        
        self._notify_queue_update()
        return removed
    
    def clear_all(self) -> int:
        """Clear all jobs from the queue.
        
        Returns:
            Number of jobs removed
        """
        # First stop processing
        self.stop()
        
        with self._lock:
            count = len(self._jobs)
            self._jobs.clear()
            self._job_order.clear()
            self._futures.clear()
        
        self._notify_queue_update()
        return count
    
    def reorder_job(self, job_id: str, new_position: int) -> bool:
        """Move a job to a new position in the queue.
        
        Args:
            job_id: ID of job to move
            new_position: New position (0-indexed)
            
        Returns:
            True if moved, False if not found
        """
        with self._lock:
            if job_id not in self._job_order:
                return False
            
            self._job_order.remove(job_id)
            new_position = max(0, min(new_position, len(self._job_order)))
            self._job_order.insert(new_position, job_id)
        
        return True
    
    def get_job(self, job_id: str) -> Optional[ConversionJob]:
        """Get a job by ID.
        
        Args:
            job_id: Job ID
            
        Returns:
            ConversionJob or None if not found
        """
        return self._jobs.get(job_id)
    
    def get_jobs(self) -> List[ConversionJob]:
        """Get all jobs in queue order.
        
        Returns:
            List of ConversionJobs
        """
        with self._lock:
            return [self._jobs[job_id] for job_id in self._job_order if job_id in self._jobs]
    
    def get_status(self) -> QueueStatus:
        """Get current queue status.
        
        Returns:
            QueueStatus instance
        """
        with self._lock:
            pending = sum(1 for j in self._jobs.values() if j.status == ConversionStatus.PENDING)
            in_progress = sum(1 for j in self._jobs.values() if j.status == ConversionStatus.IN_PROGRESS)
            completed = sum(1 for j in self._jobs.values() if j.status == ConversionStatus.COMPLETED)
            failed = sum(1 for j in self._jobs.values() if j.status in [ConversionStatus.FAILED, ConversionStatus.CANCELLED])
            
            return QueueStatus(
                total_jobs=len(self._jobs),
                pending=pending,
                in_progress=in_progress,
                completed=completed,
                failed=failed,
                is_paused=self._is_paused,
                is_processing=self._is_processing
            )
    
    def _process_job(self, job: ConversionJob) -> None:
        """Process a single conversion job.
        
        Args:
            job: Job to process
        """
        def progress_callback(progress: float, message: str):
            job.progress = progress
            job.message = message
            self._notify_job_update(job)
        
        try:
            # Update job status
            job.status = ConversionStatus.IN_PROGRESS
            job.started_at = datetime.now().isoformat()
            job.progress = 0.0
            job.message = "Starting conversion"
            self._notify_job_update(job)
            
            # Create converter with progress callback
            converter = DocumentConverter(self.config)
            converter.set_progress_callback(progress_callback)
            
            # Perform conversion
            result = converter.convert_and_save(
                job.original_path,
                self.output_dir,
                job.filename
            )
            
            # Update job with result
            job.progress = 1.0
            if result.success:
                job.status = ConversionStatus.COMPLETED
                job.message = "Conversion complete"
                job.result = result.to_dict()
            else:
                job.status = ConversionStatus.FAILED
                job.error = result.error
                job.message = f"Failed: {result.error}"
            
            job.completed_at = datetime.now().isoformat()
            
        except Exception as e:
            job.status = ConversionStatus.FAILED
            job.error = str(e)
            job.message = f"Error: {str(e)}"
            job.completed_at = datetime.now().isoformat()
        
        self._notify_job_update(job)
        self._notify_queue_update()
    
    def start(self) -> None:
        """Start processing the queue."""
        if self._is_processing:
            return
        
        self._is_processing = True
        self._is_paused = False
        
        # Create thread pool
        self._executor = ThreadPoolExecutor(max_workers=self.max_workers)
        
        # Start processing thread
        threading.Thread(target=self._processing_loop, daemon=True).start()
        
        self._notify_queue_update()
    
    def _processing_loop(self) -> None:
        """Main processing loop."""
        while self._is_processing:
            if self._is_paused:
                time.sleep(0.1)
                continue
            
            # Find next pending job
            next_job = None
            with self._lock:
                for job_id in self._job_order:
                    job = self._jobs.get(job_id)
                    if job and job.status == ConversionStatus.PENDING:
                        # Check if we have capacity
                        active_count = sum(
                            1 for j in self._jobs.values()
                            if j.status == ConversionStatus.IN_PROGRESS
                        )
                        if active_count < self.max_workers:
                            next_job = job
                            break
            
            if next_job:
                # Submit job to executor
                future = self._executor.submit(self._process_job, next_job)
                with self._lock:
                    self._futures[next_job.job_id] = future
            else:
                # No pending jobs or at capacity, wait a bit
                time.sleep(0.1)
            
            # Check if all jobs are done
            with self._lock:
                pending_or_active = any(
                    j.status in [ConversionStatus.PENDING, ConversionStatus.IN_PROGRESS]
                    for j in self._jobs.values()
                )
                if not pending_or_active and len(self._jobs) > 0:
                    # All done
                    break
        
        self._is_processing = False
        self._notify_queue_update()
    
    def pause(self) -> None:
        """Pause queue processing (jobs in progress will complete)."""
        self._is_paused = True
        self._notify_queue_update()
    
    def resume(self) -> None:
        """Resume queue processing."""
        self._is_paused = False
        
        # Restart if not processing
        if not self._is_processing:
            self.start()
        
        self._notify_queue_update()
    
    def stop(self) -> None:
        """Stop queue processing and cancel pending jobs."""
        self._is_processing = False
        
        if self._executor:
            self._executor.shutdown(wait=False)
            self._executor = None
        
        # Mark pending jobs as cancelled
        with self._lock:
            for job in self._jobs.values():
                if job.status == ConversionStatus.PENDING:
                    job.status = ConversionStatus.CANCELLED
                    job.message = "Cancelled"
        
        self._notify_queue_update()
    
    def retry_job(self, job_id: str) -> bool:
        """Retry a failed job.
        
        Args:
            job_id: ID of job to retry
            
        Returns:
            True if job was reset, False if not found or not failed
        """
        with self._lock:
            job = self._jobs.get(job_id)
            if not job:
                return False
            
            if job.status not in [ConversionStatus.FAILED, ConversionStatus.CANCELLED]:
                return False
            
            # Reset job status
            job.status = ConversionStatus.PENDING
            job.progress = 0.0
            job.message = "Waiting in queue (retry)"
            job.error = None
            job.result = None
            job.started_at = None
            job.completed_at = None
        
        self._notify_job_update(job)
        self._notify_queue_update()
        
        # Start processing if not already running
        if not self._is_processing:
            self.start()
        
        return True
    
    def update_config(self, config: ConversionConfig) -> None:
        """Update the conversion configuration.
        
        Args:
            config: New configuration
        """
        self.config = config
        self.max_workers = config.max_workers


# Singleton instance
_queue_manager: Optional[QueueManager] = None


def get_queue_manager(
    max_workers: int = 4,
    output_dir: str = "converted_output",
    config: Optional[ConversionConfig] = None
) -> QueueManager:
    """Get or create the queue manager singleton.
    
    Args:
        max_workers: Maximum number of parallel workers
        output_dir: Directory to save converted files
        config: Default conversion configuration
        
    Returns:
        QueueManager instance
    """
    global _queue_manager
    if _queue_manager is None:
        _queue_manager = QueueManager(max_workers, output_dir, config)
    return _queue_manager


def reset_queue_manager() -> None:
    """Reset the queue manager singleton."""
    global _queue_manager
    if _queue_manager:
        _queue_manager.stop()
    _queue_manager = None
