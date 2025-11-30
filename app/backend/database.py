"""
Database Module
Lightweight SQLite database for job history and metadata storage.
"""

import sqlite3
import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional
from contextlib import contextmanager
from dataclasses import asdict


class Database:
    """SQLite database for storing conversion history and metadata."""
    
    def __init__(self, db_path: str = "converter.db"):
        """Initialize database.
        
        Args:
            db_path: Path to SQLite database file
        """
        self.db_path = db_path
        self._init_db()
    
    @contextmanager
    def _get_connection(self):
        """Get a database connection with context manager."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()
    
    def _init_db(self) -> None:
        """Initialize database schema."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            # Conversion history table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS conversion_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    job_id TEXT UNIQUE NOT NULL,
                    filename TEXT NOT NULL,
                    original_path TEXT NOT NULL,
                    output_path TEXT,
                    file_type TEXT,
                    file_size INTEGER,
                    status TEXT NOT NULL,
                    error TEXT,
                    duration_ms INTEGER,
                    config_profile TEXT,
                    created_at TEXT NOT NULL,
                    started_at TEXT,
                    completed_at TEXT,
                    metadata TEXT
                )
            ''')
            
            # Create index for faster queries
            cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_history_created 
                ON conversion_history(created_at DESC)
            ''')
            
            cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_history_status 
                ON conversion_history(status)
            ''')
            
            conn.commit()
    
    def save_job(self, job_data: Dict[str, Any], config_profile: str = "default") -> int:
        """Save a conversion job to history.
        
        Args:
            job_data: Job data dictionary
            config_profile: Name of config profile used
            
        Returns:
            Database row ID
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            # Extract result metadata if present
            result = job_data.get('result', {})
            metadata = json.dumps(result.get('metadata', {})) if result else '{}'
            
            cursor.execute('''
                INSERT OR REPLACE INTO conversion_history 
                (job_id, filename, original_path, output_path, file_type, file_size,
                 status, error, duration_ms, config_profile, created_at, started_at,
                 completed_at, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                job_data.get('job_id', ''),
                job_data.get('filename', ''),
                job_data.get('original_path', ''),
                result.get('output_path', '') if result else '',
                result.get('file_type', '') if result else '',
                job_data.get('file_size', 0),
                job_data.get('status', 'unknown'),
                job_data.get('error', ''),
                result.get('duration_ms', 0) if result else 0,
                config_profile,
                job_data.get('created_at', datetime.now().isoformat()),
                job_data.get('started_at', ''),
                job_data.get('completed_at', ''),
                metadata
            ))
            
            conn.commit()
            return cursor.lastrowid
    
    def get_history(
        self,
        limit: int = 100,
        offset: int = 0,
        status: Optional[str] = None,
        search: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Get conversion history.
        
        Args:
            limit: Maximum number of records
            offset: Offset for pagination
            status: Filter by status
            search: Search in filename
            
        Returns:
            List of history records
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            query = 'SELECT * FROM conversion_history WHERE 1=1'
            params = []
            
            if status:
                query += ' AND status = ?'
                params.append(status)
            
            if search:
                query += ' AND filename LIKE ?'
                params.append(f'%{search}%')
            
            query += ' ORDER BY created_at DESC LIMIT ? OFFSET ?'
            params.extend([limit, offset])
            
            cursor.execute(query, params)
            rows = cursor.fetchall()
            
            return [dict(row) for row in rows]
    
    def get_job_by_id(self, job_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific job by ID.
        
        Args:
            job_id: Job ID
            
        Returns:
            Job record or None
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM conversion_history WHERE job_id = ?',
                (job_id,)
            )
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def delete_job(self, job_id: str) -> bool:
        """Delete a job from history.
        
        Args:
            job_id: Job ID
            
        Returns:
            True if deleted
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'DELETE FROM conversion_history WHERE job_id = ?',
                (job_id,)
            )
            conn.commit()
            return cursor.rowcount > 0
    
    def clear_history(self, older_than_days: Optional[int] = None) -> int:
        """Clear conversion history.
        
        Args:
            older_than_days: Only clear records older than this many days
            
        Returns:
            Number of records deleted
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            if older_than_days is not None:
                from datetime import timedelta
                cutoff = (datetime.now() - timedelta(days=older_than_days)).isoformat()
                cursor.execute(
                    'DELETE FROM conversion_history WHERE created_at < ?',
                    (cutoff,)
                )
            else:
                cursor.execute('DELETE FROM conversion_history')
            
            conn.commit()
            return cursor.rowcount
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get conversion statistics.
        
        Returns:
            Statistics dictionary
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            # Total conversions
            cursor.execute('SELECT COUNT(*) as total FROM conversion_history')
            total = cursor.fetchone()['total']
            
            # By status
            cursor.execute('''
                SELECT status, COUNT(*) as count 
                FROM conversion_history 
                GROUP BY status
            ''')
            by_status = {row['status']: row['count'] for row in cursor.fetchall()}
            
            # Average duration
            cursor.execute('''
                SELECT AVG(duration_ms) as avg_duration 
                FROM conversion_history 
                WHERE status = 'completed' AND duration_ms > 0
            ''')
            avg_duration = cursor.fetchone()['avg_duration'] or 0
            
            # Total file size processed
            cursor.execute('''
                SELECT SUM(file_size) as total_size 
                FROM conversion_history 
                WHERE status = 'completed'
            ''')
            total_size = cursor.fetchone()['total_size'] or 0
            
            # Recent activity (last 7 days)
            cursor.execute('''
                SELECT DATE(created_at) as date, COUNT(*) as count
                FROM conversion_history
                WHERE created_at >= datetime('now', '-7 days')
                GROUP BY DATE(created_at)
                ORDER BY date
            ''')
            recent_activity = {row['date']: row['count'] for row in cursor.fetchall()}
            
            return {
                'total_conversions': total,
                'by_status': by_status,
                'average_duration_ms': round(avg_duration, 2),
                'total_size_processed': total_size,
                'recent_activity': recent_activity
            }


# Singleton instance
_database: Optional[Database] = None


def get_database(db_path: str = "converter.db") -> Database:
    """Get or create the database singleton.
    
    Args:
        db_path: Path to database file
        
    Returns:
        Database instance
    """
    global _database
    if _database is None:
        _database = Database(db_path)
    return _database
