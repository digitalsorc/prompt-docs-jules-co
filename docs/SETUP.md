# Installation & Deployment Guide

This guide explains how to install, configure, and deploy the Document Converter application.

## Quick Start (Recommended)

### Option 1: Docker (Easiest)

The simplest way to run the application:

```bash
# Clone the repository
git clone https://github.com/digitalsorc/prompt-docs-jules-co.git
cd prompt-docs-jules-co

# Start with Docker Compose
docker-compose up

# Access the application
# Open http://localhost:8000 in your browser
```

### Option 2: Local Development

For development or running without Docker:

```bash
# Clone the repository
git clone https://github.com/digitalsorc/prompt-docs-jules-co.git
cd prompt-docs-jules-co

# Create Python virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Install frontend dependencies
cd app/frontend
npm install
npm run build
cd ../..

# Run the application
python -m app.main server

# Access the application
# Open http://localhost:8000 in your browser
```

## Detailed Installation

### System Requirements

- **Python**: 3.10 or higher
- **Node.js**: 18 or higher (for frontend build)
- **Memory**: 2GB RAM minimum, 4GB recommended
- **Storage**: 500MB for application, plus space for converted documents

### Step 1: Install Python Dependencies

```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

Required packages:
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `pdfplumber` - PDF text extraction
- `pypdf` - PDF metadata reading
- `pyyaml` - YAML configuration support

### Step 2: Build Frontend

```bash
cd app/frontend
npm install
npm run build
```

This creates an optimized production build in `app/frontend/dist/`.

### Step 3: Run the Application

```bash
# Development mode (auto-reload)
python -m app.main server --reload

# Production mode
python -m app.main server

# Custom host/port
python -m app.main server --host 127.0.0.1 --port 5000
```

### Step 4: Access the Application

Open your browser and navigate to:
- **Application**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## Docker Deployment

### Build Docker Image

```bash
docker build -t document-converter:latest .
```

### Run Container

```bash
docker run -p 8000:8000 \
  -v $(pwd)/uploads:/app/uploads \
  -v $(pwd)/converted_output:/app/converted_output \
  document-converter:latest
```

### Docker Compose

For persistent storage and easier management:

```bash
docker-compose up -d
```

The `docker-compose.yml` file sets up:
- Port mapping (8000)
- Volume mounts for uploads, output, and config
- Health checks
- Auto-restart policy

## Cloud Deployment

### Deploy to Render

1. Fork the repository to your GitHub account
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Configure:
   - **Environment**: Docker
   - **Port**: 8000
5. Deploy

### Deploy to Railway

1. Fork the repository
2. Create a new project on Railway
3. Deploy from GitHub
4. Railway auto-detects Dockerfile

### Deploy to Fly.io

```bash
# Install flyctl
curl -L https://fly.io/install.sh | sh

# Login
flyctl auth login

# Create app
flyctl launch

# Deploy
flyctl deploy
```

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `HOST` | `0.0.0.0` | Server host |
| `PORT` | `8000` | Server port |
| `UPLOAD_DIR` | `uploads` | Upload directory |
| `OUTPUT_DIR` | `converted_output` | Output directory |
| `CONFIG_DIR` | `config_profiles` | Config profiles directory |
| `DB_PATH` | `converter.db` | SQLite database path |

### Configuration Profiles

Configuration profiles are stored in `config_profiles/` as JSON or YAML files.

Create a custom profile:

```bash
# Create via API
curl -X POST http://localhost:8000/api/config/profiles \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-profile",
    "config": {
      "max_workers": 8,
      "optimization_level": "maximum"
    }
  }'
```

Or create a file `config_profiles/my-profile.json`:

```json
{
  "optimization_level": "maximum",
  "preserve_tables": true,
  "preserve_code_blocks": true,
  "max_workers": 8,
  "add_front_matter": true
}
```

## Troubleshooting

### PDF Processing Not Working

If PDF support shows "Limited", install PDF dependencies:

```bash
pip install pdfplumber pypdf
```

### Port Already in Use

Change the port:

```bash
python -m app.main server --port 8001
```

### Permission Errors

Ensure write permissions for:
- `uploads/`
- `converted_output/`
- `config_profiles/`

```bash
mkdir -p uploads converted_output config_profiles
chmod 755 uploads converted_output config_profiles
```

### Database Errors

Delete and recreate the database:

```bash
rm converter.db
python -m app.main server
```

## Security Considerations

### For Production Deployment

1. **Use HTTPS**: Deploy behind a reverse proxy (nginx, Caddy) with SSL
2. **Limit file size**: Set `max_file_size_mb` in configuration
3. **Restrict origins**: Update CORS settings in `api.py`
4. **Add authentication**: Implement your own auth layer or use a reverse proxy

### File Upload Security

The application:
- Validates file extensions before processing
- Uses UUIDs for uploaded filenames
- Sanitizes output filenames
- Does not execute uploaded files

## Support

For issues and feature requests:
- Open an issue on GitHub
- Check existing documentation
- Review the API docs at `/docs`
