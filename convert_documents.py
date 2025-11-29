
import os
import json
import shutil
import re
import datetime
import pdfplumber
import pytesseract
from PIL import Image
import io

# Configuration
CONVERTED_DOCS_DIR = "converted-documents"
ASSETS_DIR = "converted-assets/images"
VISUAL_CONTEXT_DIR = "visual-context"
MANIFEST_FILE = "conversion-manifest.json"

os.makedirs(CONVERTED_DOCS_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(VISUAL_CONTEXT_DIR, exist_ok=True)

def generate_front_matter(metadata, filename):
    today = datetime.date.today().strftime("%Y-%m-%d")
    title = metadata.get("title", filename.replace("-", " ").replace("_", " ").replace(".md", "").replace(".txt", "").replace(".pdf", ""))

    # Basic topic extraction (placeholder)
    topics = []
    keywords = []

    front_matter = f"""---
title: "{title}"
original_file: "{metadata.get('original_path', '')}"
document_type: "{metadata.get('document_type', 'reference')}"
conversion_date: "{today}"
topics: {json.dumps(topics)}
keywords: {json.dumps(keywords)}
summary: "Converted from {filename}"
related_documents: []
---

"""
    return front_matter

def clean_text(text):
    # Remove excessive newlines but preserve paragraph structure
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text

def convert_txt(filepath, filename):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Heuristic: If first line looks like a title, use it
        lines = content.splitlines()
        title = filename
        body = content
        if lines and len(lines[0]) < 100:
             title = lines[0].strip()

        metadata = {
            "title": title,
            "original_path": filepath,
            "document_type": "article"
        }

        front_matter = generate_front_matter(metadata, filename)

        # Optimize structure (simple markdown conversion)
        # Assuming paragraphs are separated by blank lines

        final_content = front_matter + body

        new_filename = os.path.splitext(filename)[0] + ".md"
        output_path = os.path.join(CONVERTED_DOCS_DIR, new_filename)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_content)

        return True, None
    except Exception as e:
        return False, str(e)

def convert_md(filepath, filename):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Check if front matter exists
        has_front_matter = content.strip().startswith("---")

        metadata = {
            "title": filename, # extraction logic could be better
            "original_path": filepath,
            "document_type": "guide"
        }

        final_content = content
        if not has_front_matter:
            front_matter = generate_front_matter(metadata, filename)
            final_content = front_matter + content
        else:
            # TODO: Enrich existing front matter
            pass

        output_path = os.path.join(CONVERTED_DOCS_DIR, filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_content)

        return True, None
    except Exception as e:
        return False, str(e)

def process_pdf(filepath, filename):
    # Placeholder for PDF processing
    return False, "Not implemented yet"

def main():
    with open(MANIFEST_FILE, 'r') as f:
        manifest = json.load(f)

    results = []

    for item in manifest:
        original_path = item['original_path']
        filename = item['filename']
        file_type = item['file_type']

        print(f"Converting {filename}...")

        success = False
        error = None

        if file_type == 'text':
            success, error = convert_txt(original_path, filename)
        elif file_type == 'markdown':
            success, error = convert_md(original_path, filename)
        # elif file_type == 'pdf':
        #     success, error = process_pdf(original_path, filename)
        else:
            # Skip PDFs for this first pass or unknown
            continue

        if success:
            print(f"  Success: {filename}")
        else:
            print(f"  Failed: {filename} - {error}")

if __name__ == "__main__":
    main()
