"""
API Module
FastAPI REST API for the document converter application.
"""

import os
import io
import shutil
import zipfile
import tempfile
import uuid
from typing import List, Optional, Dict, Any
from datetime import datetime

from fastapi import FastAPI, File, UploadFile, HTTPException, Query, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, StreamingResponse, JSONResponse
from pydantic import BaseModel, Field

from .converter import ConversionConfig, DocumentConverter, get_pdf_support
from .config import ConfigManager, get_config_manager
from .queue_manager import QueueManager, get_queue_manager, ConversionJob, QueueStatus, ConversionStatus
from .database import Database, get_database


# Pydantic models for API
class ConfigUpdate(BaseModel):
    """Configuration update request."""
    optimization_level: Optional[str] = None
    preserve_tables: Optional[bool] = None
    preserve_code_blocks: Optional[bool] = None
    heading_structure: Optional[str] = None
    max_heading_level: Optional[int] = None
    enable_ocr: Optional[bool] = None
    language: Optional[str] = None
    max_file_size_mb: Optional[int] = None
    timeout_seconds: Optional[int] = None
    error_handling: Optional[str] = None
    filename_pattern: Optional[str] = None
    output_structure: Optional[str] = None
    add_front_matter: Optional[bool] = None
    generate_summary: Optional[bool] = None
    extract_keywords: Optional[bool] = None
    max_workers: Optional[int] = None
    memory_limit_mb: Optional[int] = None
    cleanup_temp_files: Optional[bool] = None


class ProfileCreate(BaseModel):
    """Create profile request."""
    name: str
    config: ConfigUpdate


class JobResponse(BaseModel):
    """Job response model."""
    job_id: str
    filename: str
    original_path: str
    file_size: int
    status: str
    progress: float
    message: str
    created_at: str
    started_at: Optional[str] = None
    completed_at: Optional[str] = None
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None


class QueueStatusResponse(BaseModel):
    """Queue status response model."""
    total_jobs: int
    pending: int
    in_progress: int
    completed: int
    failed: int
    is_paused: bool
    is_processing: bool


class ConversionPreviewRequest(BaseModel):
    """Preview conversion request."""
    content: str
    filename: str


# Create FastAPI app
app = FastAPI(
    title="Document Converter API",
    description="A production-ready API for bulk document conversion to optimized markdown",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global state
UPLOAD_DIR = "uploads"
OUTPUT_DIR = "converted_output"
CONFIG_DIR = "config_profiles"
DB_PATH = "converter.db"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


# Startup/shutdown events
@app.on_event("startup")
async def startup_event():
    """Initialize services on startup."""
    # Initialize config manager
    get_config_manager(CONFIG_DIR)
    
    # Initialize database
    get_database(DB_PATH)
    
    # Initialize queue manager with default config
    config_manager = get_config_manager()
    config = config_manager.get_default_config()
    get_queue_manager(
        max_workers=config.max_workers,
        output_dir=OUTPUT_DIR,
        config=config
    )


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown."""
    queue_manager = get_queue_manager()
    queue_manager.stop()


# Health check
@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "pdf_support": get_pdf_support(),
        "timestamp": datetime.now().isoformat()
    }


# System info
@app.get("/api/system/info")
async def system_info():
    """Get system information."""
    queue_manager = get_queue_manager()
    database = get_database()
    
    return {
        "version": "1.0.0",
        "pdf_support": get_pdf_support(),
        "queue_status": queue_manager.get_status().to_dict(),
        "statistics": database.get_statistics(),
        "upload_dir": UPLOAD_DIR,
        "output_dir": OUTPUT_DIR
    }


# File upload endpoints
@app.post("/api/upload", response_model=List[JobResponse])
async def upload_files(files: List[UploadFile] = File(...)):
    """Upload files for conversion.
    
    Accepts multiple files and adds them to the conversion queue.
    """
    queue_manager = get_queue_manager()
    jobs = []
    
    for file in files:
        # Validate file type
        ext = os.path.splitext(file.filename)[1].lower()
        if ext not in ['.pdf', '.md', '.markdown', '.txt']:
            continue
        
        # Save uploaded file
        file_id = str(uuid.uuid4())
        safe_filename = f"{file_id}_{file.filename}"
        filepath = os.path.join(UPLOAD_DIR, safe_filename)
        
        with open(filepath, "wb") as f:
            content = await file.read()
            f.write(content)
        
        # Add to queue
        job = queue_manager.add_job(filepath, file.filename)
        jobs.append(JobResponse(**job.to_dict()))
    
    if not jobs:
        raise HTTPException(status_code=400, detail="No valid files uploaded")
    
    return jobs


@app.post("/api/upload/single", response_model=JobResponse)
async def upload_single_file(file: UploadFile = File(...)):
    """Upload a single file for conversion."""
    queue_manager = get_queue_manager()
    
    # Validate file type
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ['.pdf', '.md', '.markdown', '.txt']:
        raise HTTPException(status_code=400, detail=f"Unsupported file type: {ext}")
    
    # Save uploaded file
    file_id = str(uuid.uuid4())
    safe_filename = f"{file_id}_{file.filename}"
    filepath = os.path.join(UPLOAD_DIR, safe_filename)
    
    with open(filepath, "wb") as f:
        content = await file.read()
        f.write(content)
    
    # Add to queue
    job = queue_manager.add_job(filepath, file.filename)
    
    return JobResponse(**job.to_dict())


# Queue management endpoints
@app.get("/api/queue", response_model=List[JobResponse])
async def get_queue():
    """Get all jobs in the queue."""
    queue_manager = get_queue_manager()
    jobs = queue_manager.get_jobs()
    return [JobResponse(**job.to_dict()) for job in jobs]


@app.get("/api/queue/status", response_model=QueueStatusResponse)
async def get_queue_status():
    """Get queue status."""
    queue_manager = get_queue_manager()
    status = queue_manager.get_status()
    return QueueStatusResponse(**status.to_dict())


@app.post("/api/queue/start")
async def start_queue():
    """Start processing the queue."""
    queue_manager = get_queue_manager()
    queue_manager.start()
    return {"message": "Queue processing started"}


@app.post("/api/queue/pause")
async def pause_queue():
    """Pause queue processing."""
    queue_manager = get_queue_manager()
    queue_manager.pause()
    return {"message": "Queue processing paused"}


@app.post("/api/queue/resume")
async def resume_queue():
    """Resume queue processing."""
    queue_manager = get_queue_manager()
    queue_manager.resume()
    return {"message": "Queue processing resumed"}


@app.post("/api/queue/stop")
async def stop_queue():
    """Stop queue processing."""
    queue_manager = get_queue_manager()
    queue_manager.stop()
    return {"message": "Queue processing stopped"}


@app.delete("/api/queue/clear")
async def clear_queue():
    """Clear all jobs from the queue."""
    queue_manager = get_queue_manager()
    count = queue_manager.clear_all()
    return {"message": f"Cleared {count} jobs"}


@app.delete("/api/queue/clear-completed")
async def clear_completed():
    """Clear completed and failed jobs."""
    queue_manager = get_queue_manager()
    count = queue_manager.clear_completed()
    return {"message": f"Cleared {count} completed jobs"}


# Job endpoints
@app.get("/api/jobs/{job_id}", response_model=JobResponse)
async def get_job(job_id: str):
    """Get a specific job by ID."""
    queue_manager = get_queue_manager()
    job = queue_manager.get_job(job_id)
    
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    return JobResponse(**job.to_dict())


@app.delete("/api/jobs/{job_id}")
async def delete_job(job_id: str):
    """Remove a job from the queue."""
    queue_manager = get_queue_manager()
    removed = queue_manager.remove_job(job_id)
    
    if not removed:
        raise HTTPException(status_code=404, detail="Job not found or in progress")
    
    return {"message": "Job removed"}


@app.post("/api/jobs/{job_id}/retry")
async def retry_job(job_id: str):
    """Retry a failed job."""
    queue_manager = get_queue_manager()
    retried = queue_manager.retry_job(job_id)
    
    if not retried:
        raise HTTPException(status_code=404, detail="Job not found or not failed")
    
    return {"message": "Job queued for retry"}


# Download endpoints
@app.get("/api/download/{job_id}")
async def download_result(job_id: str):
    """Download the converted file for a job."""
    queue_manager = get_queue_manager()
    job = queue_manager.get_job(job_id)
    
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    if job.status != ConversionStatus.COMPLETED:
        raise HTTPException(status_code=400, detail="Job not completed")
    
    if not job.result or not job.result.get('output_path'):
        raise HTTPException(status_code=404, detail="Output file not found")
    
    output_path = job.result['output_path']
    if not os.path.exists(output_path):
        raise HTTPException(status_code=404, detail="Output file not found on disk")
    
    return FileResponse(
        output_path,
        filename=os.path.basename(output_path),
        media_type="text/markdown"
    )


@app.get("/api/download/all")
async def download_all():
    """Download all completed conversions as a zip file."""
    queue_manager = get_queue_manager()
    jobs = queue_manager.get_jobs()
    
    completed_jobs = [
        job for job in jobs
        if job.status == ConversionStatus.COMPLETED
        and job.result and job.result.get('output_path')
    ]
    
    if not completed_jobs:
        raise HTTPException(status_code=404, detail="No completed conversions")
    
    # Create zip in memory
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for job in completed_jobs:
            output_path = job.result['output_path']
            if os.path.exists(output_path):
                zip_file.write(output_path, os.path.basename(output_path))
    
    zip_buffer.seek(0)
    
    return StreamingResponse(
        zip_buffer,
        media_type="application/zip",
        headers={"Content-Disposition": "attachment; filename=converted_documents.zip"}
    )


# Preview endpoint
@app.get("/api/preview/{job_id}")
async def preview_result(job_id: str):
    """Get preview of converted content."""
    queue_manager = get_queue_manager()
    job = queue_manager.get_job(job_id)
    
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    if job.status != ConversionStatus.COMPLETED:
        raise HTTPException(status_code=400, detail="Job not completed")
    
    if not job.result or not job.result.get('output_path'):
        raise HTTPException(status_code=404, detail="Output file not found")
    
    output_path = job.result['output_path']
    if not os.path.exists(output_path):
        raise HTTPException(status_code=404, detail="Output file not found on disk")
    
    with open(output_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return {
        "job_id": job_id,
        "filename": job.filename,
        "content": content,
        "metadata": job.result.get('metadata', {})
    }


# Configuration endpoints
@app.get("/api/config")
async def get_config():
    """Get current configuration."""
    config_manager = get_config_manager()
    config = config_manager.get_default_config()
    return config.to_dict()


@app.put("/api/config")
async def update_config(updates: ConfigUpdate):
    """Update configuration."""
    config_manager = get_config_manager()
    queue_manager = get_queue_manager()
    
    # Get current config
    config = config_manager.get_default_config()
    
    # Apply updates
    update_dict = updates.model_dump(exclude_unset=True)
    for key, value in update_dict.items():
        if hasattr(config, key):
            setattr(config, key, value)
    
    # Save and update queue manager
    config_manager.update_default_config(config)
    queue_manager.update_config(config)
    
    return config.to_dict()


@app.get("/api/config/profiles")
async def list_profiles():
    """List all configuration profiles."""
    config_manager = get_config_manager()
    return config_manager.list_profiles()


@app.get("/api/config/profiles/{name}")
async def get_profile(name: str):
    """Get a specific profile."""
    config_manager = get_config_manager()
    try:
        config = config_manager.load_profile(name)
        return config.to_dict()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Profile not found")


@app.post("/api/config/profiles")
async def create_profile(profile: ProfileCreate):
    """Create a new configuration profile."""
    config_manager = get_config_manager()
    
    # Create config from updates
    config = ConversionConfig()
    update_dict = profile.config.model_dump(exclude_unset=True)
    for key, value in update_dict.items():
        if hasattr(config, key):
            setattr(config, key, value)
    
    path = config_manager.save_profile(profile.name, config)
    
    return {"message": f"Profile '{profile.name}' created", "path": path}


@app.delete("/api/config/profiles/{name}")
async def delete_profile(name: str):
    """Delete a configuration profile."""
    config_manager = get_config_manager()
    
    try:
        deleted = config_manager.delete_profile(name)
        if deleted:
            return {"message": f"Profile '{name}' deleted"}
        else:
            raise HTTPException(status_code=404, detail="Profile not found")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/config/profiles/{name}/apply")
async def apply_profile(name: str):
    """Apply a configuration profile."""
    config_manager = get_config_manager()
    queue_manager = get_queue_manager()
    
    try:
        config = config_manager.load_profile(name)
        config_manager.update_default_config(config)
        queue_manager.update_config(config)
        return {"message": f"Profile '{name}' applied", "config": config.to_dict()}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Profile not found")


# History endpoints
@app.get("/api/history")
async def get_history(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    status: Optional[str] = None,
    search: Optional[str] = None
):
    """Get conversion history."""
    database = get_database()
    history = database.get_history(limit, offset, status, search)
    return {"items": history, "limit": limit, "offset": offset}


@app.get("/api/history/{job_id}")
async def get_history_item(job_id: str):
    """Get a specific history item."""
    database = get_database()
    item = database.get_job_by_id(job_id)
    
    if not item:
        raise HTTPException(status_code=404, detail="History item not found")
    
    return item


@app.delete("/api/history/{job_id}")
async def delete_history_item(job_id: str):
    """Delete a history item."""
    database = get_database()
    deleted = database.delete_job(job_id)
    
    if not deleted:
        raise HTTPException(status_code=404, detail="History item not found")
    
    return {"message": "History item deleted"}


@app.delete("/api/history")
async def clear_history(older_than_days: Optional[int] = None):
    """Clear conversion history."""
    database = get_database()
    count = database.clear_history(older_than_days)
    return {"message": f"Cleared {count} history items"}


@app.get("/api/statistics")
async def get_statistics():
    """Get conversion statistics."""
    database = get_database()
    return database.get_statistics()


# Serve static files for frontend (in production)
# app.mount("/", StaticFiles(directory="app/frontend/dist", html=True), name="static")
