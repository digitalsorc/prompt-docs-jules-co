"""Tests for the document converter module."""

import os
import pytest
import tempfile
from pathlib import Path

from app.backend.converter import (
    DocumentConverter,
    ConversionConfig,
    ConversionResult,
    DocumentType,
    ConversionStatus,
    get_pdf_support
)


class TestConversionConfig:
    """Tests for ConversionConfig dataclass."""
    
    def test_default_values(self):
        """Test that default config has expected values."""
        config = ConversionConfig()
        
        assert config.optimization_level == "standard"
        assert config.preserve_tables is True
        assert config.preserve_code_blocks is True
        assert config.max_workers == 4
        assert config.add_front_matter is True
    
    def test_custom_values(self):
        """Test config with custom values."""
        config = ConversionConfig(
            optimization_level="maximum",
            max_workers=8,
            enable_ocr=True
        )
        
        assert config.optimization_level == "maximum"
        assert config.max_workers == 8
        assert config.enable_ocr is True
    
    def test_to_dict(self):
        """Test conversion to dictionary."""
        config = ConversionConfig()
        data = config.to_dict()
        
        assert isinstance(data, dict)
        assert "optimization_level" in data
        assert "max_workers" in data
    
    def test_from_dict(self):
        """Test creation from dictionary."""
        data = {
            "optimization_level": "minimal",
            "max_workers": 2
        }
        config = ConversionConfig.from_dict(data)
        
        assert config.optimization_level == "minimal"
        assert config.max_workers == 2


class TestDocumentConverter:
    """Tests for DocumentConverter class."""
    
    @pytest.fixture
    def converter(self):
        """Create a converter instance."""
        return DocumentConverter()
    
    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for tests."""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield tmpdir
    
    def test_detect_file_type_pdf(self, converter):
        """Test PDF file type detection."""
        assert converter.detect_file_type("document.pdf") == DocumentType.PDF
        assert converter.detect_file_type("Document.PDF") == DocumentType.PDF
    
    def test_detect_file_type_markdown(self, converter):
        """Test Markdown file type detection."""
        assert converter.detect_file_type("readme.md") == DocumentType.MARKDOWN
        assert converter.detect_file_type("doc.markdown") == DocumentType.MARKDOWN
    
    def test_detect_file_type_text(self, converter):
        """Test text file type detection."""
        assert converter.detect_file_type("notes.txt") == DocumentType.TEXT
    
    def test_detect_file_type_unknown(self, converter):
        """Test unknown file type detection."""
        assert converter.detect_file_type("image.jpg") == DocumentType.UNKNOWN
        assert converter.detect_file_type("script.py") == DocumentType.UNKNOWN
    
    def test_clean_title(self, converter):
        """Test title cleaning from filename."""
        assert converter.clean_title("my-document.pdf") == "my document"
        assert converter.clean_title("01_document_name.md") == "document name"
        assert converter.clean_title("test_file.txt") == "test file"
    
    def test_extract_keywords(self, converter):
        """Test keyword extraction."""
        text = "This is about prompt engineering and LLM models with transformers."
        keywords = converter.extract_keywords(text, max_keywords=5)
        
        assert isinstance(keywords, list)
        assert len(keywords) <= 5
        # Should find domain terms
        assert any(k in keywords for k in ['prompt', 'llm', 'model', 'transformer'])
    
    def test_extract_topics(self, converter):
        """Test topic extraction."""
        text = "This document covers prompt engineering techniques for LLM applications."
        topics = converter.extract_topics(text, "prompt_guide.pdf")
        
        assert isinstance(topics, list)
        assert "prompt-engineering" in topics
        assert "llm" in topics
    
    def test_generate_summary(self, converter):
        """Test summary generation."""
        text = "This is the first sentence of the document. It explains something important. Here is more content."
        summary = converter.generate_summary(text, max_sentences=2)
        
        assert isinstance(summary, str)
        assert len(summary) > 0
    
    def test_convert_txt(self, converter, temp_dir):
        """Test text file conversion."""
        # Create test file
        test_file = os.path.join(temp_dir, "test.txt")
        with open(test_file, 'w') as f:
            f.write("# Test Document\n\nThis is test content.")
        
        result = converter.convert(test_file)
        
        assert result.success is True
        assert result.output_content is not None
        assert "Test Document" in result.output_content
    
    def test_convert_md(self, converter, temp_dir):
        """Test markdown file conversion."""
        # Create test file
        test_file = os.path.join(temp_dir, "test.md")
        with open(test_file, 'w') as f:
            f.write("# Markdown Test\n\nSome markdown content.")
        
        result = converter.convert(test_file)
        
        assert result.success is True
        assert result.output_content is not None
        assert "Markdown Test" in result.output_content
    
    def test_convert_md_preserves_front_matter(self, converter, temp_dir):
        """Test that existing front matter is preserved."""
        test_file = os.path.join(temp_dir, "test.md")
        content = """---
title: "Existing Title"
author: "Test Author"
---

# Content Here
"""
        with open(test_file, 'w') as f:
            f.write(content)
        
        result = converter.convert(test_file)
        
        assert result.success is True
        # Should not add duplicate front matter
        assert result.output_content.count("---") == 2  # Only original front matter
    
    def test_convert_and_save(self, converter, temp_dir):
        """Test conversion with file save."""
        # Create test file
        test_file = os.path.join(temp_dir, "input.txt")
        with open(test_file, 'w') as f:
            f.write("Test content for saving")
        
        output_dir = os.path.join(temp_dir, "output")
        result = converter.convert_and_save(test_file, output_dir)
        
        assert result.success is True
        assert os.path.exists(result.output_path)
        
        # Verify content was saved
        with open(result.output_path, 'r') as f:
            saved_content = f.read()
        assert "Test content" in saved_content
    
    def test_convert_nonexistent_file(self, converter):
        """Test conversion of non-existent file."""
        result = converter.convert("/nonexistent/path/file.txt")
        
        assert result.success is False
        assert result.error is not None
    
    def test_convert_unsupported_type(self, converter, temp_dir):
        """Test conversion of unsupported file type."""
        test_file = os.path.join(temp_dir, "test.jpg")
        with open(test_file, 'w') as f:
            f.write("not an image")
        
        result = converter.convert(test_file)
        
        assert result.success is False
        assert "Unsupported" in result.error
    
    def test_generate_output_filename_kebab(self, converter):
        """Test kebab-case filename generation."""
        converter.config.filename_pattern = "kebab"
        
        filename = converter._generate_output_filename("My Document.pdf")
        
        assert filename == "my-document.md"
    
    def test_generate_output_filename_snake(self, converter):
        """Test snake_case filename generation."""
        converter.config.filename_pattern = "snake"
        
        filename = converter._generate_output_filename("My Document.pdf")
        
        assert filename == "my_document.md"
    
    def test_generate_output_filename_original(self, converter):
        """Test original filename preservation."""
        converter.config.filename_pattern = "original"
        
        filename = converter._generate_output_filename("My-Document.pdf")
        
        assert filename == "My-Document.md"
    
    def test_table_to_markdown(self, converter):
        """Test table conversion to markdown."""
        table = [
            ["Header 1", "Header 2"],
            ["Cell 1", "Cell 2"],
            ["Cell 3", "Cell 4"]
        ]
        
        markdown = converter.table_to_markdown(table)
        
        assert "| Header 1 | Header 2 |" in markdown
        assert "| Cell 1 | Cell 2 |" in markdown
        assert "|---|---|" in markdown
    
    def test_progress_callback(self, converter, temp_dir):
        """Test progress callback is called during conversion."""
        progress_updates = []
        
        def callback(progress, message):
            progress_updates.append((progress, message))
        
        converter.set_progress_callback(callback)
        
        # Create test file
        test_file = os.path.join(temp_dir, "test.txt")
        with open(test_file, 'w') as f:
            f.write("Test content")
        
        converter.convert_and_save(test_file, temp_dir)
        
        assert len(progress_updates) > 0
        # Final progress should be 1.0
        assert any(p[0] == 1.0 for p in progress_updates)


class TestConversionResult:
    """Tests for ConversionResult dataclass."""
    
    def test_successful_result(self):
        """Test creating a successful result."""
        result = ConversionResult(
            original_path="/path/to/file.pdf",
            filename="file.pdf",
            file_type="pdf",
            success=True,
            output_path="file.md",
            output_content="# Content"
        )
        
        assert result.success is True
        assert result.error is None
    
    def test_failed_result(self):
        """Test creating a failed result."""
        result = ConversionResult(
            original_path="/path/to/file.pdf",
            filename="file.pdf",
            file_type="pdf",
            success=False,
            error="Failed to extract text"
        )
        
        assert result.success is False
        assert result.error == "Failed to extract text"
    
    def test_to_dict(self):
        """Test conversion to dictionary."""
        result = ConversionResult(
            original_path="/path/to/file.txt",
            filename="file.txt",
            file_type="text",
            success=True
        )
        
        data = result.to_dict()
        
        assert isinstance(data, dict)
        assert data["filename"] == "file.txt"
        assert data["success"] is True


class TestPDFSupport:
    """Tests for PDF support detection."""
    
    def test_get_pdf_support(self):
        """Test PDF support detection function."""
        result = get_pdf_support()
        assert isinstance(result, bool)
