# Document Converter User Guide

A comprehensive guide to using the Document Converter application.

## Getting Started

### Opening the Application

1. Start the application (see [SETUP.md](SETUP.md) for installation)
2. Open your browser to http://localhost:8000
3. The main interface will load automatically

### Interface Overview

The interface has three main sections:

1. **Header**: Title, settings toggle, and dark/light mode switch
2. **Main Area**: File upload zone and conversion queue
3. **Sidebar**: Settings panel and statistics (when settings are enabled)

## Uploading Documents

### Supported File Types

- **PDF** (.pdf) - Including text-based and scanned documents
- **Markdown** (.md, .markdown) - Existing markdown files
- **Text** (.txt) - Plain text documents

### How to Upload

**Method 1: Drag and Drop**
1. Drag files from your file explorer
2. Drop them onto the upload zone
3. Files are automatically added to the queue

**Method 2: Click to Browse**
1. Click anywhere on the upload zone
2. Select files from the file dialog
3. Click "Open" to add them to the queue

### Bulk Upload

You can upload multiple files at once:
- Select multiple files in the file dialog (Ctrl/Cmd + click)
- Drag multiple files together
- Files are added to the queue in order

## Managing the Conversion Queue

### Queue Status Bar

Shows real-time statistics:
- **Total**: All files in queue
- **Pending**: Waiting to be converted
- **Processing**: Currently being converted
- **Completed**: Successfully converted
- **Failed**: Conversion errors

### Queue Controls

| Button | Action |
|--------|--------|
| **Start** | Begin converting pending files |
| **Pause** | Pause the queue (in-progress jobs will complete) |
| **Resume** | Resume a paused queue |
| **Stop** | Stop and cancel pending jobs |
| **Download All** | Download all completed files as ZIP |
| **Clear** | Remove completed and failed jobs |
| **Refresh** | Manually refresh queue status |

### Job Actions

Each job in the queue has action buttons:

- **Preview** (👁): View converted content before downloading
- **Download** (⬇): Download the converted file
- **Retry** (🔄): Retry a failed conversion
- **Remove** (🗑): Remove job from queue

### Progress Tracking

For in-progress jobs:
- Progress bar shows completion percentage
- Status message indicates current step
- Updates automatically in real-time

## Preview and Download

### Previewing Converted Content

1. Click the **Preview** button on a completed job
2. A modal opens showing the rendered markdown
3. Features:
   - Rendered view with formatting
   - Copy to clipboard button
   - Direct download button

### Downloading Files

**Single File:**
- Click the **Download** button on any completed job

**All Files:**
- Click **Download All** in the queue controls
- Receives a ZIP file with all converted documents

## Configuration Settings

### Opening Settings

Click the **Settings** (⚙️) button in the header to show/hide the settings panel.

### Settings Categories

#### 1. Quality Settings

| Setting | Description | Options |
|---------|-------------|---------|
| Optimization Level | How aggressively to optimize | Minimal, Standard, Maximum |
| Preserve Tables | Convert tables to markdown format | On/Off |
| Preserve Code Blocks | Detect and format code | On/Off |
| Heading Structure | How to format headings | Auto-detect, Fixed |
| Max Heading Level | Maximum heading depth | 2-6 |

#### 2. Processing Settings

| Setting | Description | Options |
|---------|-------------|---------|
| Enable OCR | Use OCR for scanned PDFs | On/Off |
| Language | Text processing language | Auto, English, Spanish, etc. |
| Max File Size | Maximum file size in MB | 1-500 |
| Timeout | Maximum time per document | 30-3600 seconds |
| Error Handling | What to do on errors | Skip & Continue, Stop Queue |

#### 3. Output Settings

| Setting | Description | Options |
|---------|-------------|---------|
| Filename Pattern | How to name output files | Original, kebab-case, snake_case, Timestamp |
| Output Structure | Directory organization | Flat, Mirror input |
| Add Front Matter | Include YAML metadata | On/Off |
| Generate Summary | Auto-generate summary | On/Off |
| Extract Keywords | Auto-extract keywords | On/Off |

#### 4. Performance Settings

| Setting | Description | Options |
|---------|-------------|---------|
| Max Workers | Parallel conversion threads | 1-16 |
| Memory Limit | Memory per worker (MB) | 256-8192 |
| Cleanup Temp Files | Delete temp files after | On/Off |

### Saving Settings

1. Make changes to any settings
2. An "Unsaved changes" indicator appears
3. Click **Save** to apply changes
4. Settings persist for future sessions

### Reset to Defaults

Click the **Reset** (↺) button to restore default settings.

## Dark Mode

Toggle between light and dark themes:
- Click the **Sun/Moon** icon in the header
- Preference is saved for future sessions

## Tips and Best Practices

### For Best Conversion Quality

1. **Use text-based PDFs** when possible (better than scanned images)
2. **Enable OCR** only for scanned documents (slower but necessary)
3. **Use Standard optimization** for most documents
4. **Use Maximum optimization** for technical documents with complex structure

### For Faster Processing

1. **Increase Max Workers** for batch processing (if you have multiple CPU cores)
2. **Disable OCR** if documents are text-based
3. **Use Skip & Continue** error handling to avoid queue stalls

### For Large Batches

1. **Upload in batches** of 50-100 files for better progress tracking
2. **Monitor memory usage** if processing many large PDFs
3. **Use Download All** to get all results at once

### Output Organization

1. **Use kebab-case** for web-friendly filenames
2. **Enable Front Matter** for documents going into knowledge systems
3. **Enable Extract Keywords** for better searchability

## Troubleshooting

### Common Issues

**Files not converting:**
- Check file type is supported (.pdf, .md, .txt)
- Check file size is under the limit
- Try increasing timeout for large files

**Poor quality output:**
- For scanned PDFs, enable OCR
- For complex tables, check Preserve Tables is on
- Try increasing optimization level

**Slow performance:**
- Reduce Max Workers if running out of memory
- Process smaller batches
- Disable OCR for text-based PDFs

**Queue stuck:**
- Click Refresh to update status
- Use Stop if needed
- Check for failed jobs and retry

### Error Messages

| Error | Solution |
|-------|----------|
| "Unsupported file type" | Only .pdf, .md, .txt are supported |
| "File too large" | Increase Max File Size in settings |
| "Timeout" | Increase timeout or try smaller file |
| "No text extracted" | File may be image-only, enable OCR |
| "Connection error" | Check server is running |

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl/Cmd + U` | Focus upload zone |
| `Escape` | Close preview modal |
| `Ctrl/Cmd + D` | Toggle dark mode |

## Getting Help

- **API Documentation**: Visit `/docs` for full API reference
- **GitHub Issues**: Report bugs or request features
- **Setup Guide**: See [SETUP.md](SETUP.md) for installation help
