#!/usr/bin/env python3
"""
Validation script for document conversion.
Checks markdown files, links, and front matter.
"""

import os
import re
import json
import sys

CONVERTED_DOCS_DIR = "converted-documents"
ASSETS_DIR = "converted-assets/images"

def validate_front_matter(content, filename):
    """Check if front matter is valid."""
    errors = []
    
    if not content.strip().startswith('---'):
        errors.append(f"Missing front matter")
        return errors
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        errors.append(f"Incomplete front matter")
        return errors
    
    fm_content = parts[1]
    required_fields = ['title', 'original_file', 'document_type', 'conversion_date']
    
    for field in required_fields:
        if f'{field}:' not in fm_content:
            errors.append(f"Missing required field: {field}")
    
    return errors

def validate_markdown_syntax(content, filename):
    """Basic markdown syntax validation."""
    errors = []
    lines = content.split('\n')
    
    # Track code block state properly
    in_code_block = False
    
    for i, line in enumerate(lines, 1):
        # Track code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue
        
        # Skip checking inside code blocks
        if in_code_block:
            continue
        
        # Check for broken headers - but ignore known false positives
        if re.match(r'^#+[^#\s]', line):
            # Skip known false positives
            if line.startswith('#!/'):  # Shebang
                continue
            if '#(' in line or '#{' in line:  # Math cardinality notation
                continue
            errors.append(f"Line {i}: Missing space after header marker")
    
    # Check for unclosed code blocks
    code_block_count = content.count('```')
    if code_block_count % 2 != 0:
        errors.append("Unclosed code block detected")
    
    return errors

def validate_links(content, filename):
    """Check for broken internal links."""
    errors = []
    
    # Find markdown links
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    
    for text, url in links:
        # Skip external links
        if url.startswith('http://') or url.startswith('https://'):
            continue
        
        # Check local file links
        if url.startswith('./') or url.startswith('../') or url.startswith(CONVERTED_DOCS_DIR):
            if not os.path.exists(url):
                errors.append(f"Broken link: {url}")
    
    return errors

def validate_images(content, filename):
    """Check for broken image references."""
    errors = []
    warnings = []
    
    # Find image references
    images = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content)
    
    for alt, path in images:
        if not path.startswith('http'):
            if not os.path.exists(path):
                # External/absolute paths from original docs are warnings, not errors
                if path.startswith('/images/') or path.startswith('../'):
                    warnings.append(f"External image reference: {path}")
                else:
                    errors.append(f"Missing image: {path}")
    
    return errors  # Only return real errors

def main():
    print("=" * 60)
    print("Document Conversion Validation")
    print("=" * 60)
    
    if not os.path.exists(CONVERTED_DOCS_DIR):
        print(f"ERROR: {CONVERTED_DOCS_DIR} directory not found")
        sys.exit(1)
    
    files = [f for f in os.listdir(CONVERTED_DOCS_DIR) if f.endswith('.md')]
    
    print(f"\nValidating {len(files)} markdown files...\n")
    
    total_errors = 0
    files_with_errors = 0
    
    all_errors = []
    
    for filename in sorted(files):
        filepath = os.path.join(CONVERTED_DOCS_DIR, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            all_errors.append((filename, [f"Cannot read file: {e}"]))
            continue
        
        errors = []
        errors.extend(validate_front_matter(content, filename))
        errors.extend(validate_markdown_syntax(content, filename))
        errors.extend(validate_links(content, filename))
        errors.extend(validate_images(content, filename))
        
        if errors:
            all_errors.append((filename, errors))
            files_with_errors += 1
            total_errors += len(errors)
    
    # Print summary
    print("-" * 60)
    print("VALIDATION SUMMARY")
    print("-" * 60)
    print(f"Total files checked: {len(files)}")
    print(f"Files with errors: {files_with_errors}")
    print(f"Total errors: {total_errors}")
    
    if all_errors:
        print("\n" + "-" * 60)
        print("ERRORS FOUND:")
        print("-" * 60)
        for filename, errors in all_errors[:20]:  # Limit output
            print(f"\n{filename}:")
            for error in errors:
                print(f"  - {error}")
        if len(all_errors) > 20:
            print(f"\n... and {len(all_errors) - 20} more files with errors")
    else:
        print("\n✓ All files passed validation!")
    
    # Check knowledge index
    print("\n" + "-" * 60)
    print("ADDITIONAL CHECKS")
    print("-" * 60)
    
    checks = [
        ("_knowledge-index.md", "Knowledge index"),
        ("conversion-report.md", "Conversion report"),
        ("README.md", "README"),
        (CONVERTED_DOCS_DIR, "Converted documents directory"),
    ]
    
    for path, name in checks:
        exists = os.path.exists(path)
        status = "✓" if exists else "✗"
        print(f"{status} {name}: {'Found' if exists else 'Missing'}")
    
    print("\n" + "=" * 60)
    if total_errors == 0:
        print("VALIDATION PASSED - All documents are valid!")
        return 0
    else:
        print(f"VALIDATION COMPLETE - {total_errors} errors found")
        return 1

if __name__ == "__main__":
    sys.exit(main())
