#!/usr/bin/env python3
"""
Document Converter Application
Main entry point for running the application.
"""

import os
import sys
import argparse
import webbrowser
from pathlib import Path


def run_server(host: str = "0.0.0.0", port: int = 8000, reload: bool = False, open_browser: bool = True):
    """Run the FastAPI server.
    
    Args:
        host: Host to bind to
        port: Port to bind to
        reload: Enable auto-reload for development
        open_browser: Open browser automatically
    """
    import uvicorn
    
    # Ensure we're in the right directory
    app_dir = Path(__file__).parent
    os.chdir(app_dir.parent)
    
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║            Document Converter Application v1.0.0             ║
╠══════════════════════════════════════════════════════════════╣
║  API Server: http://{host}:{port}                              ║
║  API Docs:   http://{host}:{port}/docs                         ║
║  Frontend:   http://localhost:{port}                           ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    # Open browser if requested
    if open_browser:
        try:
            webbrowser.open(f"http://localhost:{port}")
        except Exception:
            pass
    
    uvicorn.run(
        "app.backend.api:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )


def run_cli(files: list, output_dir: str = "converted_output", config_file: str = None):
    """Run conversion from command line.
    
    Args:
        files: List of files to convert
        output_dir: Output directory
        config_file: Optional config file path
    """
    from app.backend.converter import DocumentConverter, ConversionConfig
    from app.backend.config import ConfigManager
    
    # Load config
    if config_file:
        config_manager = ConfigManager()
        config = config_manager.import_profile(config_file, "_temp_cli")
        config = config_manager.load_profile("_temp_cli")
    else:
        config = ConversionConfig()
    
    converter = DocumentConverter(config)
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"\nConverting {len(files)} file(s) to {output_dir}/\n")
    
    success_count = 0
    for filepath in files:
        if not os.path.exists(filepath):
            print(f"  ✗ File not found: {filepath}")
            continue
        
        print(f"  Converting: {os.path.basename(filepath)}...", end=" ")
        result = converter.convert_and_save(filepath, output_dir)
        
        if result.success:
            print(f"✓ → {result.output_path}")
            success_count += 1
        else:
            print(f"✗ {result.error}")
    
    print(f"\nCompleted: {success_count}/{len(files)} files converted")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Document Converter - Convert PDF, MD, TXT to optimized markdown"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Server command
    server_parser = subparsers.add_parser("server", help="Run the web server")
    server_parser.add_argument("--host", default="0.0.0.0", help="Host to bind to")
    server_parser.add_argument("--port", type=int, default=8000, help="Port to bind to")
    server_parser.add_argument("--reload", action="store_true", help="Enable auto-reload")
    server_parser.add_argument("--no-browser", action="store_true", help="Don't open browser")
    
    # CLI command
    cli_parser = subparsers.add_parser("convert", help="Convert files from command line")
    cli_parser.add_argument("files", nargs="+", help="Files to convert")
    cli_parser.add_argument("-o", "--output", default="converted_output", help="Output directory")
    cli_parser.add_argument("-c", "--config", help="Config file (JSON or YAML)")
    
    args = parser.parse_args()
    
    if args.command == "server":
        run_server(
            host=args.host,
            port=args.port,
            reload=args.reload,
            open_browser=not args.no_browser
        )
    elif args.command == "convert":
        run_cli(
            files=args.files,
            output_dir=args.output,
            config_file=args.config
        )
    else:
        # Default: run server
        run_server()


if __name__ == "__main__":
    main()
