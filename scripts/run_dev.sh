#!/bin/bash
# Development server script

set -e

echo "Starting Document Converter Development Server..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required"
    exit 1
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

# Check Node.js
if ! command -v npm &> /dev/null; then
    echo "Warning: Node.js not found. Frontend will not be available."
    echo "Starting backend only..."
    python3 -m app.main server --reload
else
    # Install frontend dependencies
    echo "Installing frontend dependencies..."
    cd app/frontend
    npm install
    
    # Start frontend dev server in background
    echo "Starting frontend dev server..."
    npm run dev &
    FRONTEND_PID=$!
    
    cd ../..
    
    # Start backend
    echo "Starting backend server..."
    python3 -m app.main server --reload --no-browser
    
    # Cleanup
    kill $FRONTEND_PID 2>/dev/null || true
fi
