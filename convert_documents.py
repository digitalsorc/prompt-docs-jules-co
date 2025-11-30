#!/usr/bin/env python3
"""
Document Conversion Script for AI Knowledge Systems
Converts PDF, MD, and TXT files to optimized markdown format with front matter.
"""

import os
import json
import re
import datetime
import argparse
import pdfplumber
from collections import Counter

# Configuration
CONVERTED_DOCS_DIR = "converted-documents"
ASSETS_DIR = "converted-assets/images"
VISUAL_CONTEXT_DIR = "visual-context"
ORIGINAL_DOCS_DIR = "original-documents"
MANIFEST_FILE = "conversion-manifest.json"
REPORT_FILE = "conversion-report.md"

# Create directories
for d in [CONVERTED_DOCS_DIR, ASSETS_DIR, VISUAL_CONTEXT_DIR, ORIGINAL_DOCS_DIR]:
    os.makedirs(d, exist_ok=True)


def extract_keywords(text, max_keywords=10):
    """Extract keywords from text using simple frequency analysis."""
    # Common AI/ML terms to prioritize
    domain_terms = {
        'prompt', 'llm', 'model', 'chain', 'agent', 'rag', 'retrieval',
        'reasoning', 'inference', 'training', 'fine-tuning', 'embedding',
        'transformer', 'attention', 'context', 'generation', 'evaluation',
        'benchmark', 'optimization', 'parameter', 'token', 'neural'
    }
    
    # Clean and tokenize
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
    
    # Count frequency
    word_freq = Counter(words)
    
    # Filter common words
    stop_words = {'the', 'and', 'for', 'are', 'with', 'that', 'this', 'from', 'can', 'will', 'has', 'have', 'been', 'which', 'their', 'more', 'not', 'also', 'such', 'use', 'using'}
    
    keywords = []
    for word, _ in word_freq.most_common(50):
        if word not in stop_words and (word in domain_terms or len(keywords) < max_keywords):
            keywords.append(word)
            if len(keywords) >= max_keywords:
                break
    
    return keywords


def extract_topics(text, filename):
    """Extract topics based on content analysis."""
    topics = []
    text_lower = text.lower()
    filename_lower = filename.lower()
    
    topic_patterns = {
        'prompt-engineering': ['prompt engineering', 'prompting', 'prompt design'],
        'llm': ['large language model', 'llm', 'language model'],
        'rag': ['retrieval augmented', 'rag', 'retrieval-augmented'],
        'chain-of-thought': ['chain of thought', 'cot', 'chain-of-thought'],
        'react': ['react', 'reasoning and acting'],
        'agents': ['agent', 'autonomous', 'agentic'],
        'fine-tuning': ['fine-tuning', 'lora', 'peft', 'adapter'],
        'evaluation': ['evaluation', 'benchmark', 'metrics'],
        'multimodal': ['multimodal', 'vision', 'image', 'visual'],
        'code-generation': ['code generation', 'copilot', 'code completion'],
        'dialogue': ['dialogue', 'conversation', 'chat'],
    }
    
    for topic, patterns in topic_patterns.items():
        if any(p in text_lower or p in filename_lower for p in patterns):
            topics.append(topic)
    
    return topics[:5]  # Limit to 5 topics


def generate_summary(text, max_sentences=3):
    """Generate a simple summary from the first few meaningful sentences."""
    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text[:3000])
    
    summary_sentences = []
    for sentence in sentences:
        # Skip very short sentences or those that look like headers/citations
        if len(sentence) > 50 and not sentence.startswith('[') and not re.match(r'^\d+\.?\s*$', sentence):
            summary_sentences.append(sentence.strip())
            if len(summary_sentences) >= max_sentences:
                break
    
    return ' '.join(summary_sentences) if summary_sentences else "Document converted for AI knowledge systems."


def clean_title(filename):
    """Generate a clean title from filename."""
    title = filename.replace("-", " ").replace("_", " ")
    title = re.sub(r'\.(md|txt|pdf)$', '', title, flags=re.IGNORECASE)
    # Remove leading numbers like "01_" or "37_"
    title = re.sub(r'^\d+[\s_-]*', '', title)
    return title.strip()


def generate_front_matter(metadata, filename, content=""):
    """Generate YAML front matter for the markdown file."""
    today = datetime.date.today().strftime("%Y-%m-%d")
    title = metadata.get("title", clean_title(filename))
    
    # Extract keywords and topics from content
    keywords = extract_keywords(content) if content else []
    topics = extract_topics(content, filename) if content else []
    summary = generate_summary(content) if content else f"Converted from {filename}"
    
    # Escape quotes in title and summary
    title = title.replace('"', '\\"')
    summary = summary.replace('"', '\\"')[:500]  # Limit summary length
    
    front_matter = f'''---
title: "{title}"
original_file: "{metadata.get('original_path', '')}"
document_type: "{metadata.get('document_type', 'reference')}"
conversion_date: "{today}"
topics: {json.dumps(topics)}
keywords: {json.dumps(keywords)}
summary: "{summary}"
related_documents: []
---

'''
    return front_matter


def clean_text(text):
    """Clean and normalize extracted text."""
    if not text:
        return ""
    
    # Remove excessive whitespace
    text = re.sub(r'[ \t]+', ' ', text)
    # Remove excessive newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Fix common OCR/extraction issues
    text = re.sub(r'(?<=[a-z])-\n(?=[a-z])', '', text)  # Fix hyphenated words
    
    return text.strip()


def table_to_markdown(table):
    """Convert a pdfplumber table to markdown format."""
    if not table or not table[0]:
        return ""
    
    # Clean cells
    def clean_cell(cell):
        if cell is None:
            return ""
        return str(cell).replace('\n', ' ').replace('|', '\\|').strip()
    
    rows = [[clean_cell(cell) for cell in row] for row in table]
    
    # Ensure all rows have the same number of columns
    max_cols = max(len(row) for row in rows)
    rows = [row + [''] * (max_cols - len(row)) for row in rows]
    
    if not rows:
        return ""
    
    # Create markdown table
    md_lines = []
    
    # Header row
    md_lines.append('| ' + ' | '.join(rows[0]) + ' |')
    md_lines.append('|' + '|'.join(['---'] * len(rows[0])) + '|')
    
    # Data rows
    for row in rows[1:]:
        md_lines.append('| ' + ' | '.join(row) + ' |')
    
    return '\n'.join(md_lines)


def detect_headings(text, lines):
    """Detect and format headings based on text patterns."""
    formatted_lines = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Skip empty lines
        if not stripped:
            formatted_lines.append('')
            continue
        
        # Detect potential headings (short, possibly uppercase, followed by content)
        is_heading = False
        heading_level = 2
        
        # All caps short text is likely a heading
        if stripped.isupper() and len(stripped) < 80 and len(stripped.split()) < 10:
            is_heading = True
            heading_level = 2
        # Numbered sections like "1. Introduction" or "1.1 Methods"
        elif re.match(r'^(\d+\.)+\s*[A-Z]', stripped):
            is_heading = True
            # Count dots to determine heading level
            dots = len(re.findall(r'\.', stripped.split()[0]))
            heading_level = min(dots + 1, 4)
        # Lines ending with no period that are short
        elif len(stripped) < 60 and not stripped.endswith('.') and stripped[0].isupper():
            # Check if next line is longer (content)
            if i + 1 < len(lines) and len(lines[i + 1].strip()) > len(stripped):
                is_heading = True
                heading_level = 3
        
        if is_heading:
            # Clean heading text
            heading_text = re.sub(r'^(\d+\.)+\s*', '', stripped)  # Remove numbering
            heading_text = heading_text.title() if heading_text.isupper() else heading_text
            formatted_lines.append(f'\n{"#" * heading_level} {heading_text}\n')
        else:
            formatted_lines.append(stripped)
    
    return formatted_lines


def process_pdf(filepath, filename):
    """Extract and convert PDF to markdown."""
    try:
        all_text = []
        tables_md = []
        
        with pdfplumber.open(filepath) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                # Extract text
                text = page.extract_text()
                if text:
                    all_text.append(f"\n<!-- Page {page_num} -->\n")
                    all_text.append(text)
                
                # Extract tables
                tables = page.extract_tables()
                for table in tables:
                    if table and len(table) > 1:
                        md_table = table_to_markdown(table)
                        if md_table:
                            tables_md.append(f"\n**Table (Page {page_num}):**\n\n{md_table}\n")
        
        # Combine all text
        raw_text = '\n'.join(all_text)
        cleaned_text = clean_text(raw_text)
        
        if not cleaned_text:
            return False, "No text extracted from PDF"
        
        # Process text into markdown format
        lines = cleaned_text.split('\n')
        formatted_lines = detect_headings(cleaned_text, lines)
        
        # Add document title as H1
        title = clean_title(filename)
        body = '\n'.join(formatted_lines)
        
        # Add tables at the end if any
        if tables_md:
            body += '\n\n## Tables\n' + '\n'.join(tables_md)
        
        # Generate metadata
        metadata = {
            "title": title,
            "original_path": filepath,
            "document_type": "research" if 'paper' in filename.lower() or any(x in body.lower() for x in ['abstract', 'methodology', 'references']) else "guide"
        }
        
        front_matter = generate_front_matter(metadata, filename, body)
        
        # Create main heading
        main_content = f"# {title}\n\n{body}"
        final_content = front_matter + main_content
        
        # Write output
        new_filename = os.path.splitext(filename)[0].lower().replace(' ', '-').replace('_', '-') + ".md"
        # Clean up multiple dashes
        new_filename = re.sub(r'-+', '-', new_filename)
        output_path = os.path.join(CONVERTED_DOCS_DIR, new_filename)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        return True, None
        
    except Exception as e:
        return False, str(e)


def convert_txt(filepath, filename):
    """Convert text file to markdown."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Heuristic: If first line looks like a title, use it
        lines = content.splitlines()
        title = clean_title(filename)
        body = content
        if lines and len(lines[0]) < 100 and lines[0].strip():
            title = lines[0].strip()

        metadata = {
            "title": title,
            "original_path": filepath,
            "document_type": "article"
        }

        front_matter = generate_front_matter(metadata, filename, content)

        # Add main heading if not present
        if not body.strip().startswith('#'):
            body = f"# {title}\n\n{body}"

        final_content = front_matter + body

        new_filename = os.path.splitext(filename)[0].lower().replace(' ', '-').replace('_', '-') + ".md"
        new_filename = re.sub(r'-+', '-', new_filename)
        output_path = os.path.join(CONVERTED_DOCS_DIR, new_filename)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_content)

        return True, None
    except Exception as e:
        return False, str(e)


def convert_md(filepath, filename):
    """Optimize existing markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Check if front matter exists
        has_front_matter = content.strip().startswith("---")

        # Extract content without front matter for analysis
        content_for_analysis = content
        if has_front_matter:
            # Find the end of front matter
            parts = content.split('---', 2)
            if len(parts) >= 3:
                content_for_analysis = parts[2]

        title = clean_title(filename)
        
        # Try to extract title from first H1
        h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if h1_match:
            title = h1_match.group(1).strip()

        metadata = {
            "title": title,
            "original_path": filepath,
            "document_type": "guide"
        }

        final_content = content
        if not has_front_matter:
            front_matter = generate_front_matter(metadata, filename, content_for_analysis)
            final_content = front_matter + content

        # Normalize filename
        new_filename = filename.lower().replace(' ', '-').replace('_', '-')
        new_filename = re.sub(r'-+', '-', new_filename)
        if not new_filename.endswith('.md'):
            new_filename += '.md'
        
        output_path = os.path.join(CONVERTED_DOCS_DIR, new_filename)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_content)

        return True, None
    except Exception as e:
        return False, str(e)


def generate_report(results):
    """Generate conversion report."""
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    success_count = sum(1 for r in results if r['success'])
    fail_count = len(results) - success_count
    
    report = f"""# Document Conversion Report

**Date:** {today}

## Summary

- **Total Files Processed:** {len(results)}
- **Successful Conversions:** {success_count}
- **Failed Conversions:** {fail_count}

## Conversion Details

### Successfully Converted Files

| Original File | Output File | Type |
|---------------|-------------|------|
"""
    
    for r in results:
        if r['success']:
            report += f"| {r['filename']} | {r.get('output_file', 'N/A')} | {r['file_type']} |\n"
    
    if fail_count > 0:
        report += """

### Failed Conversions

| File | Error |
|------|-------|
"""
        for r in results:
            if not r['success']:
                error_msg = r.get('error', 'Unknown error').replace('|', '\\|')[:100]
                report += f"| {r['filename']} | {error_msg} |\n"
    
    report += """

## Directory Structure

```
/converted-documents/    - All converted markdown files
/converted-assets/       - Extracted images and assets
/visual-context/         - Visual element descriptions
/original-documents/     - Original source files (archived)
```

## Notes

- All files converted with UTF-8 encoding
- Front matter added with metadata, topics, and keywords
- Tables converted to markdown format where possible
"""
    
    return report


def main():
    parser = argparse.ArgumentParser(description='Convert documents to optimized markdown')
    parser.add_argument('--pdf-only', action='store_true', help='Only process PDF files')
    parser.add_argument('--md-only', action='store_true', help='Only process markdown files')
    parser.add_argument('--txt-only', action='store_true', help='Only process text files')
    parser.add_argument('--limit', type=int, default=0, help='Limit number of files to process')
    args = parser.parse_args()
    
    with open(MANIFEST_FILE, 'r') as f:
        manifest = json.load(f)

    results = []
    processed = 0

    for item in manifest:
        if args.limit > 0 and processed >= args.limit:
            break
            
        original_path = item['original_path']
        filename = item['filename']
        file_type = item['file_type']

        # Filter by type if specified
        if args.pdf_only and file_type != 'pdf':
            continue
        if args.md_only and file_type != 'markdown':
            continue
        if args.txt_only and file_type != 'text':
            continue

        print(f"Converting {filename}...")

        success = False
        error = None
        output_file = None

        if file_type == 'text':
            success, error = convert_txt(original_path, filename)
            output_file = os.path.splitext(filename)[0].lower().replace(' ', '-').replace('_', '-') + ".md"
        elif file_type == 'markdown':
            success, error = convert_md(original_path, filename)
            output_file = filename.lower().replace(' ', '-').replace('_', '-')
        elif file_type == 'pdf':
            success, error = process_pdf(original_path, filename)
            output_file = os.path.splitext(filename)[0].lower().replace(' ', '-').replace('_', '-') + ".md"
        else:
            continue

        results.append({
            'filename': filename,
            'file_type': file_type,
            'success': success,
            'error': error,
            'output_file': output_file
        })
        
        processed += 1

        if success:
            print(f"  ✓ Success: {filename}")
        else:
            print(f"  ✗ Failed: {filename} - {error}")
    
    # Generate report
    report = generate_report(results)
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n{'='*50}")
    print(f"Conversion complete!")
    print(f"  Processed: {processed}")
    print(f"  Success: {sum(1 for r in results if r['success'])}")
    print(f"  Failed: {sum(1 for r in results if not r['success'])}")
    print(f"  Report: {REPORT_FILE}")


if __name__ == "__main__":
    main()
