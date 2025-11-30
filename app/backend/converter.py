"""
Document Converter Module
Refactored from convert_documents.py to be used as a library module.
Converts PDF, MD, and TXT files to optimized markdown format with front matter.
"""

import os
import json
import re
import datetime
import tempfile
import shutil
from typing import Optional, Dict, Any, List, Tuple, Callable
from collections import Counter
from dataclasses import dataclass, field, asdict
from enum import Enum

try:
    import pdfplumber
    PDF_SUPPORT = True
except ImportError:
    PDF_SUPPORT = False
    pdfplumber = None


class DocumentType(str, Enum):
    """Supported document types."""
    PDF = "pdf"
    MARKDOWN = "markdown"
    TEXT = "text"
    UNKNOWN = "unknown"


class ConversionStatus(str, Enum):
    """Status of a conversion job."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class ConversionConfig:
    """Configuration for document conversion."""
    # Conversion Quality
    optimization_level: str = "standard"  # minimal, standard, maximum
    preserve_tables: bool = True
    preserve_code_blocks: bool = True
    heading_structure: str = "auto"  # auto, fixed
    max_heading_level: int = 4
    
    # Processing Options
    enable_ocr: bool = False
    language: str = "auto"
    max_file_size_mb: int = 100
    timeout_seconds: int = 300
    error_handling: str = "skip"  # skip, halt
    
    # Output Customization
    filename_pattern: str = "kebab"  # original, kebab, snake, timestamp
    output_structure: str = "flat"  # flat, mirrored
    add_front_matter: bool = True
    generate_summary: bool = True
    extract_keywords: bool = True
    
    # Performance
    max_workers: int = 4
    memory_limit_mb: int = 1024
    cleanup_temp_files: bool = True
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert config to dictionary."""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ConversionConfig":
        """Create config from dictionary."""
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


@dataclass
class ConversionResult:
    """Result of a single document conversion."""
    original_path: str
    filename: str
    file_type: str
    success: bool
    output_path: Optional[str] = None
    output_content: Optional[str] = None
    error: Optional[str] = None
    duration_ms: int = 0
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert result to dictionary."""
        return asdict(self)


class DocumentConverter:
    """Main document converter class."""
    
    # Common AI/ML terms to prioritize in keyword extraction
    DOMAIN_TERMS = {
        'prompt', 'llm', 'model', 'chain', 'agent', 'rag', 'retrieval',
        'reasoning', 'inference', 'training', 'fine-tuning', 'embedding',
        'transformer', 'attention', 'context', 'generation', 'evaluation',
        'benchmark', 'optimization', 'parameter', 'token', 'neural'
    }
    
    # Stop words for keyword extraction
    STOP_WORDS = {
        'the', 'and', 'for', 'are', 'with', 'that', 'this', 'from', 'can',
        'will', 'has', 'have', 'been', 'which', 'their', 'more', 'not',
        'also', 'such', 'use', 'using', 'about', 'each', 'they', 'some',
        'would', 'could', 'should', 'these', 'those', 'being', 'into'
    }
    
    # Topic patterns for content analysis
    TOPIC_PATTERNS = {
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
    
    def __init__(self, config: Optional[ConversionConfig] = None):
        """Initialize converter with optional configuration."""
        self.config = config or ConversionConfig()
        self._progress_callback: Optional[Callable[[float, str], None]] = None
    
    def set_progress_callback(self, callback: Callable[[float, str], None]) -> None:
        """Set a callback function for progress updates."""
        self._progress_callback = callback
    
    def _report_progress(self, progress: float, message: str) -> None:
        """Report progress to callback if set."""
        if self._progress_callback:
            self._progress_callback(progress, message)
    
    def detect_file_type(self, filename: str) -> DocumentType:
        """Detect document type from filename extension."""
        ext = os.path.splitext(filename)[1].lower()
        if ext == '.pdf':
            return DocumentType.PDF
        elif ext in ['.md', '.markdown']:
            return DocumentType.MARKDOWN
        elif ext == '.txt':
            return DocumentType.TEXT
        else:
            return DocumentType.UNKNOWN
    
    def extract_keywords(self, text: str, max_keywords: int = 10) -> List[str]:
        """Extract keywords from text using simple frequency analysis."""
        if not self.config.extract_keywords:
            return []
        
        # Clean and tokenize
        words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
        
        # Count frequency
        word_freq = Counter(words)
        
        keywords = []
        for word, _ in word_freq.most_common(50):
            if word not in self.STOP_WORDS and (word in self.DOMAIN_TERMS or len(keywords) < max_keywords):
                keywords.append(word)
                if len(keywords) >= max_keywords:
                    break
        
        return keywords
    
    def extract_topics(self, text: str, filename: str) -> List[str]:
        """Extract topics based on content analysis."""
        topics = []
        text_lower = text.lower()
        filename_lower = filename.lower()
        
        for topic, patterns in self.TOPIC_PATTERNS.items():
            if any(p in text_lower or p in filename_lower for p in patterns):
                topics.append(topic)
        
        return topics[:5]
    
    def generate_summary(self, text: str, max_sentences: int = 3) -> str:
        """Generate a simple summary from the first few meaningful sentences."""
        if not self.config.generate_summary:
            return ""
        
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
    
    def clean_title(self, filename: str) -> str:
        """Generate a clean title from filename."""
        title = filename.replace("-", " ").replace("_", " ")
        title = re.sub(r'\.(md|txt|pdf)$', '', title, flags=re.IGNORECASE)
        # Remove leading numbers like "01_" or "37_"
        title = re.sub(r'^\d+[\s_-]*', '', title)
        return title.strip()
    
    def generate_front_matter(self, metadata: Dict[str, Any], filename: str, content: str = "") -> str:
        """Generate YAML front matter for the markdown file."""
        if not self.config.add_front_matter:
            return ""
        
        today = datetime.date.today().strftime("%Y-%m-%d")
        title = metadata.get("title", self.clean_title(filename))
        
        # Extract keywords and topics from content
        keywords = self.extract_keywords(content) if content else []
        topics = self.extract_topics(content, filename) if content else []
        summary = self.generate_summary(content) if content else f"Converted from {filename}"
        
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
    
    def clean_text(self, text: str) -> str:
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
    
    def table_to_markdown(self, table: List[List[Any]]) -> str:
        """Convert a pdfplumber table to markdown format."""
        if not table or not table[0]:
            return ""
        
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
    
    def detect_headings(self, text: str, lines: List[str]) -> List[str]:
        """Detect and format headings based on text patterns."""
        formatted_lines = []
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            
            # Skip empty lines
            if not stripped:
                formatted_lines.append('')
                continue
            
            # Detect potential headings
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
                heading_level = min(dots + 1, self.config.max_heading_level)
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
    
    def process_pdf(self, filepath: str, filename: str) -> ConversionResult:
        """Extract and convert PDF to markdown."""
        import time
        start_time = time.time()
        
        if not PDF_SUPPORT:
            return ConversionResult(
                original_path=filepath,
                filename=filename,
                file_type="pdf",
                success=False,
                error="PDF support not available. Install pdfplumber: pip install pdfplumber"
            )
        
        try:
            self._report_progress(0.1, f"Opening PDF: {filename}")
            all_text = []
            tables_md = []
            
            with pdfplumber.open(filepath) as pdf:
                total_pages = len(pdf.pages)
                for page_num, page in enumerate(pdf.pages, 1):
                    self._report_progress(
                        0.1 + (0.7 * page_num / total_pages),
                        f"Processing page {page_num}/{total_pages}"
                    )
                    
                    # Extract text
                    text = page.extract_text()
                    if text:
                        all_text.append(f"\n<!-- Page {page_num} -->\n")
                        all_text.append(text)
                    
                    # Extract tables if configured
                    if self.config.preserve_tables:
                        tables = page.extract_tables()
                        for table in tables:
                            if table and len(table) > 1:
                                md_table = self.table_to_markdown(table)
                                if md_table:
                                    tables_md.append(f"\n**Table (Page {page_num}):**\n\n{md_table}\n")
            
            self._report_progress(0.8, "Processing extracted text")
            
            # Combine all text
            raw_text = '\n'.join(all_text)
            cleaned_text = self.clean_text(raw_text)
            
            if not cleaned_text:
                return ConversionResult(
                    original_path=filepath,
                    filename=filename,
                    file_type="pdf",
                    success=False,
                    error="No text extracted from PDF"
                )
            
            # Process text into markdown format
            lines = cleaned_text.split('\n')
            formatted_lines = self.detect_headings(cleaned_text, lines)
            
            # Add document title as H1
            title = self.clean_title(filename)
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
            
            front_matter = self.generate_front_matter(metadata, filename, body)
            
            # Create main heading
            main_content = f"# {title}\n\n{body}"
            final_content = front_matter + main_content
            
            self._report_progress(0.9, "Generating output filename")
            
            # Generate output filename
            output_filename = self._generate_output_filename(filename)
            
            duration_ms = int((time.time() - start_time) * 1000)
            
            return ConversionResult(
                original_path=filepath,
                filename=filename,
                file_type="pdf",
                success=True,
                output_path=output_filename,
                output_content=final_content,
                duration_ms=duration_ms,
                metadata={
                    "title": title,
                    "pages": total_pages,
                    "tables": len(tables_md)
                }
            )
            
        except Exception as e:
            return ConversionResult(
                original_path=filepath,
                filename=filename,
                file_type="pdf",
                success=False,
                error=str(e)
            )
    
    def convert_txt(self, filepath: str, filename: str) -> ConversionResult:
        """Convert text file to markdown."""
        import time
        start_time = time.time()
        
        try:
            self._report_progress(0.3, f"Reading text file: {filename}")
            
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Heuristic: If first line looks like a title, use it
            lines = content.splitlines()
            title = self.clean_title(filename)
            body = content
            if lines and len(lines[0]) < 100 and lines[0].strip():
                title = lines[0].strip()
            
            self._report_progress(0.6, "Generating metadata")
            
            metadata = {
                "title": title,
                "original_path": filepath,
                "document_type": "article"
            }
            
            front_matter = self.generate_front_matter(metadata, filename, content)
            
            # Add main heading if not present
            if not body.strip().startswith('#'):
                body = f"# {title}\n\n{body}"
            
            final_content = front_matter + body
            
            output_filename = self._generate_output_filename(filename)
            duration_ms = int((time.time() - start_time) * 1000)
            
            return ConversionResult(
                original_path=filepath,
                filename=filename,
                file_type="text",
                success=True,
                output_path=output_filename,
                output_content=final_content,
                duration_ms=duration_ms,
                metadata={"title": title, "line_count": len(lines)}
            )
            
        except Exception as e:
            return ConversionResult(
                original_path=filepath,
                filename=filename,
                file_type="text",
                success=False,
                error=str(e)
            )
    
    def convert_md(self, filepath: str, filename: str) -> ConversionResult:
        """Optimize existing markdown file."""
        import time
        start_time = time.time()
        
        try:
            self._report_progress(0.3, f"Reading markdown file: {filename}")
            
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Check if front matter exists
            has_front_matter = content.strip().startswith("---")
            
            # Extract content without front matter for analysis
            content_for_analysis = content
            if has_front_matter:
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    content_for_analysis = parts[2]
            
            title = self.clean_title(filename)
            
            # Try to extract title from first H1
            h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if h1_match:
                title = h1_match.group(1).strip()
            
            self._report_progress(0.6, "Generating metadata")
            
            metadata = {
                "title": title,
                "original_path": filepath,
                "document_type": "guide"
            }
            
            final_content = content
            if not has_front_matter and self.config.add_front_matter:
                front_matter = self.generate_front_matter(metadata, filename, content_for_analysis)
                final_content = front_matter + content
            
            output_filename = self._generate_output_filename(filename, is_md=True)
            duration_ms = int((time.time() - start_time) * 1000)
            
            return ConversionResult(
                original_path=filepath,
                filename=filename,
                file_type="markdown",
                success=True,
                output_path=output_filename,
                output_content=final_content,
                duration_ms=duration_ms,
                metadata={"title": title, "had_front_matter": has_front_matter}
            )
            
        except Exception as e:
            return ConversionResult(
                original_path=filepath,
                filename=filename,
                file_type="markdown",
                success=False,
                error=str(e)
            )
    
    def _generate_output_filename(self, filename: str, is_md: bool = False) -> str:
        """Generate output filename based on configuration."""
        if self.config.filename_pattern == "original":
            base = os.path.splitext(filename)[0] if not is_md else filename.replace('.md', '').replace('.markdown', '')
            return base + ".md"
        elif self.config.filename_pattern == "kebab":
            base = os.path.splitext(filename)[0] if not is_md else filename.replace('.md', '').replace('.markdown', '')
            base = base.lower().replace(' ', '-').replace('_', '-')
            base = re.sub(r'-+', '-', base)
            return base + ".md"
        elif self.config.filename_pattern == "snake":
            base = os.path.splitext(filename)[0] if not is_md else filename.replace('.md', '').replace('.markdown', '')
            base = base.lower().replace(' ', '_').replace('-', '_')
            base = re.sub(r'_+', '_', base)
            return base + ".md"
        elif self.config.filename_pattern == "timestamp":
            base = os.path.splitext(filename)[0] if not is_md else filename.replace('.md', '').replace('.markdown', '')
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            return f"{base}_{timestamp}.md"
        else:
            # Default to kebab
            base = os.path.splitext(filename)[0] if not is_md else filename.replace('.md', '').replace('.markdown', '')
            base = base.lower().replace(' ', '-').replace('_', '-')
            return re.sub(r'-+', '-', base) + ".md"
    
    def convert(self, filepath: str, filename: Optional[str] = None) -> ConversionResult:
        """Convert a single document to markdown.
        
        Args:
            filepath: Path to the file to convert
            filename: Optional filename override
            
        Returns:
            ConversionResult with conversion status and content
        """
        if filename is None:
            filename = os.path.basename(filepath)
        
        file_type = self.detect_file_type(filename)
        
        if file_type == DocumentType.PDF:
            return self.process_pdf(filepath, filename)
        elif file_type == DocumentType.MARKDOWN:
            return self.convert_md(filepath, filename)
        elif file_type == DocumentType.TEXT:
            return self.convert_txt(filepath, filename)
        else:
            return ConversionResult(
                original_path=filepath,
                filename=filename,
                file_type="unknown",
                success=False,
                error=f"Unsupported file type: {file_type}"
            )
    
    def convert_and_save(self, filepath: str, output_dir: str, filename: Optional[str] = None) -> ConversionResult:
        """Convert a document and save to output directory.
        
        Args:
            filepath: Path to the file to convert
            output_dir: Directory to save converted file
            filename: Optional filename override
            
        Returns:
            ConversionResult with conversion status
        """
        result = self.convert(filepath, filename)
        
        if result.success and result.output_content:
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, result.output_path)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result.output_content)
            
            result.output_path = output_path
        
        self._report_progress(1.0, "Conversion complete")
        return result


def get_pdf_support() -> bool:
    """Check if PDF support is available."""
    return PDF_SUPPORT
