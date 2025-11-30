"""Tests for the API endpoints."""

import pytest
import os
import tempfile
from fastapi.testclient import TestClient

# Import after setting up test environment
os.environ["UPLOAD_DIR"] = tempfile.mkdtemp()
os.environ["OUTPUT_DIR"] = tempfile.mkdtemp()
os.environ["CONFIG_DIR"] = tempfile.mkdtemp()

from app.backend.api import app


@pytest.fixture
def client():
    """Create a test client."""
    return TestClient(app)


@pytest.fixture
def temp_file():
    """Create a temporary test file."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("Test content for upload")
        return f.name


class TestHealthEndpoint:
    """Tests for health check endpoint."""
    
    def test_health_check(self, client):
        """Test health endpoint returns healthy status."""
        response = client.get("/api/health")
        
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "pdf_support" in data
        assert "timestamp" in data


class TestSystemInfoEndpoint:
    """Tests for system info endpoint."""
    
    def test_system_info(self, client):
        """Test system info endpoint."""
        response = client.get("/api/system/info")
        
        assert response.status_code == 200
        data = response.json()
        assert "version" in data
        assert "pdf_support" in data
        assert "queue_status" in data


class TestUploadEndpoints:
    """Tests for file upload endpoints."""
    
    def test_upload_single_valid_file(self, client, temp_file):
        """Test uploading a valid file."""
        with open(temp_file, "rb") as f:
            response = client.post(
                "/api/upload/single",
                files={"file": ("test.txt", f, "text/plain")}
            )
        
        assert response.status_code == 200
        data = response.json()
        assert "job_id" in data
        assert data["filename"] == "test.txt"
        assert data["status"] == "pending"
    
    def test_upload_invalid_file_type(self, client):
        """Test uploading an unsupported file type."""
        response = client.post(
            "/api/upload/single",
            files={"file": ("test.jpg", b"fake image data", "image/jpeg")}
        )
        
        assert response.status_code == 400
    
    def test_upload_multiple_files(self, client, temp_file):
        """Test uploading multiple files."""
        with open(temp_file, "rb") as f:
            content = f.read()
        
        files = [
            ("files", ("test1.txt", content, "text/plain")),
            ("files", ("test2.txt", content, "text/plain"))
        ]
        
        response = client.post("/api/upload", files=files)
        
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2


class TestQueueEndpoints:
    """Tests for queue management endpoints."""
    
    def test_get_queue(self, client):
        """Test getting the queue."""
        response = client.get("/api/queue")
        
        assert response.status_code == 200
        assert isinstance(response.json(), list)
    
    def test_get_queue_status(self, client):
        """Test getting queue status."""
        response = client.get("/api/queue/status")
        
        assert response.status_code == 200
        data = response.json()
        assert "total_jobs" in data
        assert "pending" in data
        assert "in_progress" in data
        assert "completed" in data
        assert "failed" in data
        assert "is_paused" in data
        assert "is_processing" in data
    
    def test_start_queue(self, client):
        """Test starting the queue."""
        response = client.post("/api/queue/start")
        
        assert response.status_code == 200
    
    def test_pause_queue(self, client):
        """Test pausing the queue."""
        response = client.post("/api/queue/pause")
        
        assert response.status_code == 200
    
    def test_resume_queue(self, client):
        """Test resuming the queue."""
        response = client.post("/api/queue/resume")
        
        assert response.status_code == 200
    
    def test_stop_queue(self, client):
        """Test stopping the queue."""
        response = client.post("/api/queue/stop")
        
        assert response.status_code == 200
    
    def test_clear_queue(self, client):
        """Test clearing the queue."""
        response = client.delete("/api/queue/clear")
        
        assert response.status_code == 200


class TestJobEndpoints:
    """Tests for job management endpoints."""
    
    def test_get_nonexistent_job(self, client):
        """Test getting a non-existent job."""
        response = client.get("/api/jobs/nonexistent-id")
        
        assert response.status_code == 404
    
    def test_delete_nonexistent_job(self, client):
        """Test deleting a non-existent job."""
        response = client.delete("/api/jobs/nonexistent-id")
        
        assert response.status_code == 404
    
    def test_retry_nonexistent_job(self, client):
        """Test retrying a non-existent job."""
        response = client.post("/api/jobs/nonexistent-id/retry")
        
        assert response.status_code == 404


class TestConfigEndpoints:
    """Tests for configuration endpoints."""
    
    def test_get_config(self, client):
        """Test getting configuration."""
        response = client.get("/api/config")
        
        assert response.status_code == 200
        data = response.json()
        assert "optimization_level" in data
        assert "max_workers" in data
    
    def test_update_config(self, client):
        """Test updating configuration."""
        response = client.put(
            "/api/config",
            json={"max_workers": 8}
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["max_workers"] == 8
    
    def test_list_profiles(self, client):
        """Test listing configuration profiles."""
        response = client.get("/api/config/profiles")
        
        assert response.status_code == 200
        assert isinstance(response.json(), list)
    
    def test_create_profile(self, client):
        """Test creating a new profile."""
        response = client.post(
            "/api/config/profiles",
            json={
                "name": "test-profile",
                "config": {"max_workers": 2}
            }
        )
        
        assert response.status_code == 200
    
    def test_get_nonexistent_profile(self, client):
        """Test getting a non-existent profile."""
        response = client.get("/api/config/profiles/nonexistent")
        
        assert response.status_code == 404
    
    def test_delete_default_profile(self, client):
        """Test that default profile cannot be deleted."""
        response = client.delete("/api/config/profiles/default")
        
        assert response.status_code == 400


class TestHistoryEndpoints:
    """Tests for history endpoints."""
    
    def test_get_history(self, client):
        """Test getting conversion history."""
        response = client.get("/api/history")
        
        assert response.status_code == 200
        data = response.json()
        assert "items" in data
        assert "limit" in data
        assert "offset" in data
    
    def test_get_history_with_filters(self, client):
        """Test getting history with filters."""
        response = client.get("/api/history?limit=10&status=completed")
        
        assert response.status_code == 200
    
    def test_get_statistics(self, client):
        """Test getting statistics."""
        response = client.get("/api/statistics")
        
        assert response.status_code == 200
        data = response.json()
        assert "total_conversions" in data
        assert "by_status" in data
    
    def test_clear_history(self, client):
        """Test clearing history."""
        response = client.delete("/api/history")
        
        assert response.status_code == 200


class TestDownloadEndpoints:
    """Tests for download endpoints."""
    
    def test_download_nonexistent_job(self, client):
        """Test downloading result for non-existent job."""
        response = client.get("/api/download/nonexistent-id")
        
        assert response.status_code == 404
    
    def test_preview_nonexistent_job(self, client):
        """Test previewing non-existent job."""
        response = client.get("/api/preview/nonexistent-id")
        
        assert response.status_code == 404
