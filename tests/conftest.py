"""Pytest configuration and fixtures."""

import os
import sys
import tempfile

import pytest

# Add app to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up test environment
os.environ["UPLOAD_DIR"] = tempfile.mkdtemp()
os.environ["OUTPUT_DIR"] = tempfile.mkdtemp()
os.environ["CONFIG_DIR"] = tempfile.mkdtemp()
os.environ["DB_PATH"] = os.path.join(tempfile.mkdtemp(), "test.db")


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Set up test environment before running tests."""
    # Create necessary directories
    for env_var in ["UPLOAD_DIR", "OUTPUT_DIR", "CONFIG_DIR"]:
        os.makedirs(os.environ[env_var], exist_ok=True)
    
    yield
    
    # Cleanup is handled by tempfile module


@pytest.fixture
def sample_text_content():
    """Return sample text content for testing."""
    return """# Sample Document

This is a sample document for testing the document converter.

## Section 1

Content in section 1 about prompt engineering.

## Section 2

More content about LLM and RAG systems.

### Subsection 2.1

Detailed information here.
"""


@pytest.fixture
def sample_markdown_with_frontmatter():
    """Return sample markdown with front matter."""
    return """---
title: "Test Document"
author: "Test Author"
date: "2024-01-01"
---

# Test Document

This is a test document with front matter.
"""
