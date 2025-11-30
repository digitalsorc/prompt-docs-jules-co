# Prompt Engineering Document Collection

A comprehensive collection of 219 documents on prompt engineering, LLMs, and AI agents, optimized for AI knowledge systems.

## Overview

This repository contains research papers, guides, and reference materials on:
- **Prompt Engineering** - Design patterns, techniques, and best practices
- **Large Language Models (LLMs)** - Architecture, evaluation, and deployment
- **AI Agents** - Autonomous agents, ReAct patterns, multi-agent systems
- **RAG Systems** - Retrieval augmented generation techniques
- **Fine-tuning** - LoRA, PEFT, and adapter methods

All documents have been converted to optimized markdown format with semantic metadata for use in AI knowledge systems like Perplexity Spaces.

## Quick Start

### For AI/RAG Systems

1. **Import the knowledge index:**
   ```
   _knowledge-index.md
   ```

2. **Point to converted documents:**
   ```
   converted-documents/*.md
   ```

3. **Each document includes front matter with:**
   - Title, topics, keywords
   - Summary for context
   - Related documents

### For Manual Browsing

1. Check `_knowledge-index.md` for topic categories
2. Browse `converted-documents/` for individual files
3. See `conversion-report.md` for conversion details

## Directory Structure

```
├── converted-documents/     # 219 optimized markdown files
│   ├── prompt-engineering-*.md
│   ├── llm-*.md
│   ├── rag-*.md
│   └── ...
├── converted-assets/        # Extracted images and assets
│   └── images/
├── visual-context/          # Visual element descriptions
├── original-documents/      # Archived source files
├── _knowledge-index.md      # Concept-to-document mapping
├── conversion-manifest.json # File inventory with metadata
├── conversion-report.md     # Conversion statistics
└── README.md               # This file
```

## Document Categories

### By Topic

| Topic | Description | Documents |
|-------|-------------|-----------|
| Prompt Engineering | Prompt design, patterns, optimization | 50+ |
| LLM Agents | ReAct, autonomous agents, multi-agent | 30+ |
| RAG Systems | Retrieval augmentation, embeddings | 25+ |
| Fine-tuning | LoRA, PEFT, adapters | 20+ |
| Evaluation | Benchmarks, metrics, testing | 20+ |
| Dialogue Systems | Chatbots, conversation design | 15+ |
| Code Generation | Copilot, code understanding | 15+ |
| Multimodal | Vision-language models | 15+ |

### Document Types

- **Research Papers**: Academic papers with methodology and results
- **Guides**: Practical how-to documentation
- **Reference**: Technical specifications and patterns

## Document Format

All converted documents include:

```yaml
---
title: "Document Title"
original_file: "./source.pdf"
document_type: "research|guide|reference"
conversion_date: "2025-11-29"
topics: ["topic1", "topic2"]
keywords: ["keyword1", "keyword2"]
summary: "Brief description..."
related_documents: []
---

# Document Title

Content with preserved structure...
```

## Using with AI Systems

### Perplexity Spaces
1. Upload all files from `converted-documents/`
2. Include `_knowledge-index.md` as a reference
3. System will index front matter for better retrieval

### Custom RAG Pipelines
1. Parse front matter for metadata indexing
2. Use topics/keywords for semantic routing
3. Chunk content respecting markdown structure

### LLM Knowledge Bases
1. Load documents with their summaries
2. Use knowledge index for concept mapping
3. Front matter provides structured context

## Conversion Details

### Processing Methods

| Source Type | Method | Files |
|-------------|--------|-------|
| PDF (text) | pdfplumber extraction | 208 |
| PDF (images) | OCR via Tesseract | 6 |
| Markdown | Optimization + front matter | 4 |
| Text | Structure + front matter | 1 |

### Quality Features

- ✓ UTF-8 encoding throughout
- ✓ Semantic heading hierarchy
- ✓ Table conversion to markdown
- ✓ Keyword/topic extraction
- ✓ Cross-document linking ready
- ✓ LLM-optimized structure

## Contributing

### Adding New Documents
1. Place PDF/MD/TXT in root directory
2. Run `python3 analyze_repo.py` to update manifest
3. Run `python3 convert_documents.py` to convert
4. Regenerate knowledge index

### Improving Conversions
1. Check `conversion-report.md` for any issues
2. Manual edits welcome in `converted-documents/`
3. Preserve front matter structure

## Tools Used

- **pdfplumber**: PDF text and table extraction
- **Tesseract OCR**: Image-based PDF processing
- **pypdf**: PDF metadata analysis
- **Python**: Conversion orchestration

## License

Documents retain their original licenses. See individual files for attribution.

## Stats

- **Total Documents**: 219
- **Topics Indexed**: 11
- **Keywords Extracted**: 409
- **Last Updated**: 2025-11-29

---

*Optimized for AI knowledge retrieval systems*
