#!/bin/bash
# Build Docker image

set -e

echo "Building Document Converter Docker image..."

docker build -t document-converter:latest .

echo ""
echo "Build complete! Run with:"
echo "  docker run -p 8000:8000 document-converter:latest"
echo ""
echo "Or use docker-compose:"
echo "  docker-compose up"
