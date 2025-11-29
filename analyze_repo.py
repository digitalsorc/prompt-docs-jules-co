
import os
import json
import mimetypes
from pypdf import PdfReader
# import pdfplumber # Disable heavy analysis for initial manifest

def analyze_pdf(filepath):
    metadata = {
        "page_count": 0,
        "has_images": "unknown", # Skip heavy check
        "has_tables": "unknown", # Skip heavy check
        "is_readable": True,
        "error": None
    }
    try:
        reader = PdfReader(filepath)
        metadata["page_count"] = len(reader.pages)
        # We assume most PDFs have text. We can check if extracting text returns anything for the first page.
        try:
             if len(reader.pages) > 0:
                text = reader.pages[0].extract_text()
                if text and len(text.strip()) > 0:
                    metadata["has_text"] = True
                else:
                    metadata["has_text"] = False
        except:
             metadata["has_text"] = "error"

    except Exception as e:
        metadata["is_readable"] = False
        metadata["error"] = str(e)

    return metadata

def analyze_text_file(filepath):
    metadata = {
        "line_count": 0,
        "word_count": 0
    }
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            metadata["line_count"] = len(content.splitlines())
            metadata["word_count"] = len(content.split())
    except Exception as e:
        metadata["error"] = str(e)
    return metadata

def main():
    manifest = []

    ignore_dirs = {
        'converted-documents', 'converted-assets', 'visual-context', 'original-documents', '.git'
    }

    files_processed = 0

    for root, dirs, files in os.walk('.'):
        # Filter directories
        dirs[:] = [d for d in dirs if d not in ignore_dirs and not d.startswith('.')]

        for file in files:
            if file.startswith('.') or file == 'analyze_repo.py':
                continue

            filepath = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()

            file_info = {
                "original_path": filepath,
                "filename": file,
                "extension": ext,
                "file_type": "unknown",
                "metadata": {}
            }

            # print(f"Processing {filepath}...")

            if ext == '.pdf':
                file_info["file_type"] = "pdf"
                file_info["metadata"] = analyze_pdf(filepath)
            elif ext in ['.md', '.markdown']:
                file_info["file_type"] = "markdown"
                file_info["metadata"] = analyze_text_file(filepath)
            elif ext == '.txt':
                file_info["file_type"] = "text"
                file_info["metadata"] = analyze_text_file(filepath)
            else:
                continue

            manifest.append(file_info)
            files_processed += 1

    with open('conversion-manifest.json', 'w') as f:
        json.dump(manifest, f, indent=2)

    print(f"Analysis complete. Processed {files_processed} files.")

if __name__ == "__main__":
    main()
