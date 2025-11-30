import React from 'react';
import ReactMarkdown from 'react-markdown';
import { X, Download, Copy, Check, FileText } from 'lucide-react';

/**
 * PreviewModal Component
 * Shows a preview of the converted markdown content.
 */
export default function PreviewModal({ preview, onClose, onDownload }) {
  const [copied, setCopied] = React.useState(false);

  if (!preview) return null;

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(preview.content);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (error) {
      console.error('Failed to copy:', error);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm">
      <div className="relative w-full max-w-4xl max-h-[90vh] bg-white dark:bg-slate-800 rounded-xl shadow-2xl flex flex-col">
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-slate-200 dark:border-slate-700">
          <div className="flex items-center gap-3">
            <div className="p-2 bg-primary-100 dark:bg-primary-900/30 rounded-lg">
              <FileText className="w-5 h-5 text-primary-600 dark:text-primary-400" />
            </div>
            <div>
              <h2 className="font-semibold text-slate-900 dark:text-slate-100">
                {preview.filename}
              </h2>
              <p className="text-sm text-slate-500 dark:text-slate-400">
                Preview converted markdown
              </p>
            </div>
          </div>
          
          <div className="flex items-center gap-2">
            <button
              onClick={handleCopy}
              className="p-2 text-slate-500 hover:text-slate-700 dark:hover:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700 rounded-lg transition-colors"
              title="Copy to clipboard"
            >
              {copied ? <Check className="w-5 h-5 text-green-500" /> : <Copy className="w-5 h-5" />}
            </button>
            <button
              onClick={onDownload}
              className="p-2 text-slate-500 hover:text-green-600 hover:bg-slate-100 dark:hover:bg-slate-700 rounded-lg transition-colors"
              title="Download"
            >
              <Download className="w-5 h-5" />
            </button>
            <button
              onClick={onClose}
              className="p-2 text-slate-500 hover:text-red-600 hover:bg-slate-100 dark:hover:bg-slate-700 rounded-lg transition-colors"
              title="Close"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Tabs */}
        <div className="flex px-6 border-b border-slate-200 dark:border-slate-700">
          <Tab active>Rendered</Tab>
          <Tab>Source</Tab>
        </div>

        {/* Content */}
        <div className="flex-1 overflow-auto p-6">
          <div className="markdown-preview">
            <ReactMarkdown>{preview.content}</ReactMarkdown>
          </div>
        </div>

        {/* Metadata footer */}
        {preview.metadata && Object.keys(preview.metadata).length > 0 && (
          <div className="px-6 py-3 bg-slate-50 dark:bg-slate-900/50 border-t border-slate-200 dark:border-slate-700">
            <div className="flex flex-wrap gap-4 text-sm text-slate-500 dark:text-slate-400">
              {preview.metadata.pages && (
                <span>📄 {preview.metadata.pages} pages</span>
              )}
              {preview.metadata.tables !== undefined && (
                <span>📊 {preview.metadata.tables} tables</span>
              )}
              {preview.metadata.title && (
                <span>📝 {preview.metadata.title}</span>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

function Tab({ children, active }) {
  return (
    <button
      className={`px-4 py-3 text-sm font-medium transition-colors ${
        active
          ? 'text-primary-600 dark:text-primary-400 border-b-2 border-primary-600 dark:border-primary-400'
          : 'text-slate-500 hover:text-slate-700 dark:hover:text-slate-300'
      }`}
    >
      {children}
    </button>
  );
}
