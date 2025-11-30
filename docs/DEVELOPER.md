# Developer Guide

Technical documentation for contributing to the Document Converter application.

## Architecture Overview

The application follows a modern web architecture:

```
┌─────────────────────────────────────────────────────────────┐
│                      Frontend (React)                        │
│  ┌─────────┐  ┌────────────┐  ┌──────────┐  ┌─────────────┐ │
│  │ Upload  │  │   Queue    │  │ Settings │  │   Preview   │ │
│  └────┬────┘  └─────┬──────┘  └────┬─────┘  └──────┬──────┘ │
│       │             │              │                │        │
│       └─────────────┼──────────────┼────────────────┘        │
│                     │              │                          │
└─────────────────────┼──────────────┼──────────────────────────┘
                      │              │
                      ▼              ▼
┌─────────────────────────────────────────────────────────────┐
│                  REST API (FastAPI)                          │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                    API Endpoints                      │   │
│  │  /upload  /queue  /jobs  /config  /download  /history │   │
│  └───────────────────────┬──────────────────────────────┘   │
│                          │                                   │
│  ┌───────────────────────┼──────────────────────────────┐   │
│  │              Backend Services                         │   │
│  │  ┌──────────┐  ┌──────────────┐  ┌────────────────┐  │   │
│  │  │ Converter │  │ Queue Manager │  │ Config Manager │  │   │
│  │  └──────────┘  └──────────────┘  └────────────────┘  │   │
│  │        │              │                   │           │   │
│  │        └──────────────┼───────────────────┘           │   │
│  │                       │                               │   │
│  │              ┌────────▼────────┐                      │   │
│  │              │    Database     │                      │   │
│  │              │    (SQLite)     │                      │   │
│  │              └─────────────────┘                      │   │
│  └───────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## Project Structure

```
/
├── app/
│   ├── __init__.py              # Package init
│   ├── main.py                  # Application entry point
│   ├── backend/
│   │   ├── __init__.py
│   │   ├── api.py               # FastAPI endpoints
│   │   ├── converter.py         # Core conversion logic
│   │   ├── config.py            # Configuration management
│   │   ├── queue_manager.py     # Job queue and workers
│   │   └── database.py          # SQLite database
│   └── frontend/
│       ├── src/
│       │   ├── main.jsx         # React entry
│       │   ├── App.jsx          # Main app component
│       │   ├── index.css        # Tailwind styles
│       │   ├── components/      # React components
│       │   └── services/        # API client
│       ├── package.json
│       └── vite.config.js
├── tests/                       # Test files
├── docs/                        # Documentation
├── scripts/                     # Build/run scripts
├── requirements.txt             # Python dependencies
├── Dockerfile
└── docker-compose.yml
```

## Backend Development

### Core Modules

#### converter.py

The main conversion engine. Key classes:

```python
class ConversionConfig:
    """Configuration dataclass for conversion settings."""
    optimization_level: str = "standard"
    preserve_tables: bool = True
    # ... other settings

class DocumentConverter:
    """Main converter class."""
    
    def convert(self, filepath: str) -> ConversionResult:
        """Convert a single document."""
        
    def convert_and_save(self, filepath: str, output_dir: str) -> ConversionResult:
        """Convert and save to output directory."""
```

#### queue_manager.py

Handles job queuing and parallel processing:

```python
class QueueManager:
    """Manages conversion queue and worker pool."""
    
    def add_job(self, filepath: str) -> ConversionJob:
        """Add a file to the queue."""
        
    def start(self) -> None:
        """Start processing the queue."""
        
    def pause(self) -> None:
        """Pause processing."""
```

#### api.py

FastAPI application with REST endpoints:

```python
# Key endpoints
POST /api/upload           # Upload files
GET  /api/queue            # Get queue
POST /api/queue/start      # Start processing
GET  /api/jobs/{job_id}    # Get job details
GET  /api/download/{job_id} # Download result
GET  /api/config           # Get configuration
PUT  /api/config           # Update configuration
```

### Adding New Features

#### Adding a New API Endpoint

1. Define the Pydantic model (if needed):
```python
class MyRequest(BaseModel):
    field: str
```

2. Add the endpoint:
```python
@app.post("/api/my-endpoint")
async def my_endpoint(request: MyRequest):
    # Implementation
    return {"result": "success"}
```

3. Update frontend API service:
```javascript
export async function myEndpoint(data) {
    return request('/my-endpoint', {
        method: 'POST',
        body: JSON.stringify(data)
    });
}
```

#### Adding a New Configuration Option

1. Update `ConversionConfig` in `converter.py`:
```python
@dataclass
class ConversionConfig:
    # ... existing fields
    new_option: str = "default"
```

2. Update API model in `api.py`:
```python
class ConfigUpdate(BaseModel):
    # ... existing fields
    new_option: Optional[str] = None
```

3. Update frontend settings panel in `SettingsPanel.jsx`

#### Adding a New Conversion Format

1. Add file type detection:
```python
def detect_file_type(self, filename: str) -> DocumentType:
    # Add new extension
    elif ext in ['.docx']:
        return DocumentType.WORD
```

2. Add conversion method:
```python
def convert_word(self, filepath: str, filename: str) -> ConversionResult:
    # Implementation
```

3. Update `convert()` method to handle new type

## Frontend Development

### Component Architecture

```
App.jsx
├── FileUploader.jsx     # Drag-drop upload
├── JobQueue.jsx         # Queue display
│   └── JobItem          # Individual job
├── SettingsPanel.jsx    # Configuration
│   ├── QualitySettings
│   ├── ProcessingSettings
│   ├── OutputSettings
│   └── PerformanceSettings
├── PreviewModal.jsx     # Markdown preview
└── Toast.jsx            # Notifications
```

### State Management

The app uses React's built-in state with hooks:

```javascript
// Main application state
const [jobs, setJobs] = useState([]);
const [queueStatus, setQueueStatus] = useState({});
const [config, setConfig] = useState(null);
const [preview, setPreview] = useState(null);
```

### API Integration

API calls are centralized in `services/api.js`:

```javascript
// Usage in components
import api from './services/api';

const handleUpload = async (files) => {
    const jobs = await api.uploadFiles(files);
    setJobs(prev => [...prev, ...jobs]);
};
```

### Styling

Using Tailwind CSS with custom configuration:

- Dark mode: `dark:` prefix classes
- Custom colors in `tailwind.config.js`
- Component-specific styles in `index.css`

### Adding a New Component

1. Create component file:
```javascript
// src/components/MyComponent.jsx
import React from 'react';

export default function MyComponent({ prop1, prop2 }) {
    return (
        <div className="p-4 rounded-lg bg-white dark:bg-slate-800">
            {/* Component content */}
        </div>
    );
}
```

2. Import and use in App.jsx:
```javascript
import MyComponent from './components/MyComponent';

// In render
<MyComponent prop1="value" prop2={data} />
```

## Testing

### Running Tests

```bash
# Backend tests
pytest tests/

# With coverage
pytest tests/ --cov=app --cov-report=html

# Frontend tests (if added)
cd app/frontend
npm test
```

### Writing Tests

#### Backend Tests

```python
# tests/test_converter.py
import pytest
from app.backend.converter import DocumentConverter, ConversionConfig

class TestDocumentConverter:
    def test_detect_file_type_pdf(self):
        converter = DocumentConverter()
        assert converter.detect_file_type("test.pdf") == DocumentType.PDF
    
    def test_convert_txt(self, tmp_path):
        # Create test file
        test_file = tmp_path / "test.txt"
        test_file.write_text("Test content")
        
        converter = DocumentConverter()
        result = converter.convert(str(test_file))
        
        assert result.success
        assert "Test content" in result.output_content
```

#### API Tests

```python
# tests/test_api.py
from fastapi.testclient import TestClient
from app.backend.api import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_upload_file():
    with open("test.txt", "rb") as f:
        response = client.post(
            "/api/upload/single",
            files={"file": ("test.txt", f, "text/plain")}
        )
    assert response.status_code == 200
```

## Debugging

### Backend Debugging

```python
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Add breakpoints
import pdb; pdb.set_trace()

# Run with auto-reload
python -m app.main server --reload
```

### Frontend Debugging

```javascript
// Browser DevTools
console.log('Debug value:', value);

// React DevTools extension for component inspection

// Network tab for API calls
```

## Code Style

### Python

- Follow PEP 8
- Use type hints
- Docstrings for public functions

```python
def convert_document(filepath: str, config: ConversionConfig = None) -> ConversionResult:
    """Convert a document to markdown.
    
    Args:
        filepath: Path to the document file.
        config: Optional conversion configuration.
        
    Returns:
        ConversionResult with success status and content.
    """
```

### JavaScript

- Use functional components
- Consistent prop destructuring
- JSDoc comments for complex functions

```javascript
/**
 * Upload files to the conversion queue.
 * @param {File[]} files - Array of files to upload
 * @returns {Promise<Job[]>} Array of created jobs
 */
async function uploadFiles(files) {
    // Implementation
}
```

## Building for Production

### Backend

```bash
# Install production dependencies only
pip install --no-dev -r requirements.txt

# Run with production settings
uvicorn app.backend.api:app --host 0.0.0.0 --port 8000 --workers 4
```

### Frontend

```bash
cd app/frontend
npm run build
```

The build output goes to `app/frontend/dist/`.

### Docker

```bash
# Build image
docker build -t document-converter:latest .

# Run container
docker run -d -p 8000:8000 document-converter:latest
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Run tests
5. Submit a pull request

### Commit Messages

Use conventional commits:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `refactor:` Code refactoring
- `test:` Adding tests
- `chore:` Maintenance tasks
