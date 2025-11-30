import React, { useState, useEffect, useCallback } from 'react';
import { 
  Sun, Moon, Play, Pause, Square, Trash2, Download, 
  Settings, History, BarChart3, RefreshCw, ChevronDown
} from 'lucide-react';

import FileUploader from './components/FileUploader';
import JobQueue from './components/JobQueue';
import SettingsPanel from './components/SettingsPanel';
import PreviewModal from './components/PreviewModal';
import { ToastContainer, useToast } from './components/Toast';
import api from './services/api';

/**
 * Main Application Component
 */
export default function App() {
  // Theme state
  const [darkMode, setDarkMode] = useState(() => {
    if (typeof window !== 'undefined') {
      return localStorage.getItem('darkMode') === 'true' || 
        window.matchMedia('(prefers-color-scheme: dark)').matches;
    }
    return false;
  });

  // Application state
  const [jobs, setJobs] = useState([]);
  const [queueStatus, setQueueStatus] = useState({
    total_jobs: 0,
    pending: 0,
    in_progress: 0,
    completed: 0,
    failed: 0,
    is_paused: false,
    is_processing: false
  });
  const [config, setConfig] = useState(null);
  const [preview, setPreview] = useState(null);
  const [showSettings, setShowSettings] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [systemInfo, setSystemInfo] = useState(null);

  // Toast notifications
  const { toasts, success, error, warning, info, removeToast } = useToast();

  // Apply dark mode
  useEffect(() => {
    document.documentElement.classList.toggle('dark', darkMode);
    localStorage.setItem('darkMode', darkMode);
  }, [darkMode]);

  // Load initial data
  useEffect(() => {
    loadInitialData();
  }, []);

  // Poll for updates when processing
  useEffect(() => {
    let pollInterval;
    if (queueStatus.is_processing || queueStatus.in_progress > 0) {
      pollInterval = setInterval(refreshQueue, 1000);
    }
    return () => clearInterval(pollInterval);
  }, [queueStatus.is_processing, queueStatus.in_progress]);

  const loadInitialData = async () => {
    try {
      const [queueData, configData, statusData, systemData] = await Promise.all([
        api.getQueue(),
        api.getConfig(),
        api.getQueueStatus(),
        api.getSystemInfo()
      ]);
      setJobs(queueData);
      setConfig(configData);
      setQueueStatus(statusData);
      setSystemInfo(systemData);
    } catch (err) {
      error('Failed to load initial data', 'Connection Error');
      console.error(err);
    }
  };

  const refreshQueue = async () => {
    try {
      const [queueData, statusData] = await Promise.all([
        api.getQueue(),
        api.getQueueStatus()
      ]);
      setJobs(queueData);
      setQueueStatus(statusData);
    } catch (err) {
      console.error('Failed to refresh queue:', err);
    }
  };

  // File upload handler
  const handleFilesSelected = async (files) => {
    setIsLoading(true);
    try {
      const newJobs = await api.uploadFiles(files);
      setJobs(prev => [...prev, ...newJobs]);
      success(`Added ${files.length} file(s) to queue`, 'Files Uploaded');
      
      // Refresh status
      const statusData = await api.getQueueStatus();
      setQueueStatus(statusData);
    } catch (err) {
      error(err.message || 'Failed to upload files', 'Upload Error');
    } finally {
      setIsLoading(false);
    }
  };

  // Queue control handlers
  const handleStart = async () => {
    try {
      await api.startQueue();
      info('Conversion started', 'Queue');
      refreshQueue();
    } catch (err) {
      error(err.message, 'Start Error');
    }
  };

  const handlePause = async () => {
    try {
      await api.pauseQueue();
      warning('Queue paused', 'Queue');
      refreshQueue();
    } catch (err) {
      error(err.message, 'Pause Error');
    }
  };

  const handleResume = async () => {
    try {
      await api.resumeQueue();
      info('Queue resumed', 'Queue');
      refreshQueue();
    } catch (err) {
      error(err.message, 'Resume Error');
    }
  };

  const handleStop = async () => {
    try {
      await api.stopQueue();
      warning('Queue stopped', 'Queue');
      refreshQueue();
    } catch (err) {
      error(err.message, 'Stop Error');
    }
  };

  const handleClearQueue = async () => {
    try {
      await api.clearQueue();
      setJobs([]);
      success('Queue cleared', 'Queue');
      refreshQueue();
    } catch (err) {
      error(err.message, 'Clear Error');
    }
  };

  const handleClearCompleted = async () => {
    try {
      await api.clearCompleted();
      refreshQueue();
      success('Completed jobs cleared', 'Queue');
    } catch (err) {
      error(err.message, 'Clear Error');
    }
  };

  // Job handlers
  const handleRemoveJob = async (jobId) => {
    try {
      await api.deleteJob(jobId);
      setJobs(prev => prev.filter(j => j.job_id !== jobId));
    } catch (err) {
      error(err.message, 'Remove Error');
    }
  };

  const handleRetryJob = async (jobId) => {
    try {
      await api.retryJob(jobId);
      refreshQueue();
      info('Job queued for retry', 'Retry');
    } catch (err) {
      error(err.message, 'Retry Error');
    }
  };

  const handlePreviewJob = async (jobId) => {
    try {
      const previewData = await api.getPreview(jobId);
      setPreview(previewData);
    } catch (err) {
      error(err.message, 'Preview Error');
    }
  };

  const handleDownloadJob = async (jobId) => {
    try {
      const blob = await api.downloadResult(jobId);
      const job = jobs.find(j => j.job_id === jobId);
      const filename = job?.result?.output_path?.split('/').pop() || 'converted.md';
      
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    } catch (err) {
      error(err.message, 'Download Error');
    }
  };

  const handleDownloadAll = async () => {
    try {
      const blob = await api.downloadAll();
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'converted_documents.zip';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      success('Downloaded all conversions', 'Download');
    } catch (err) {
      error(err.message, 'Download Error');
    }
  };

  // Config handlers
  const handleSaveConfig = async (newConfig) => {
    try {
      const updated = await api.updateConfig(newConfig);
      setConfig(updated);
      success('Settings saved', 'Configuration');
    } catch (err) {
      error(err.message, 'Save Error');
    }
  };

  const handleResetConfig = async () => {
    try {
      const defaultConfig = await api.getConfig();
      setConfig(defaultConfig);
      info('Settings reset to defaults', 'Configuration');
    } catch (err) {
      error(err.message, 'Reset Error');
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-900 transition-colors">
      {/* Header */}
      <header className="bg-white dark:bg-slate-800 border-b border-slate-200 dark:border-slate-700 sticky top-0 z-40">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            {/* Logo */}
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-gradient-to-br from-primary-500 to-primary-700 rounded-xl flex items-center justify-center">
                <span className="text-white font-bold text-lg">DC</span>
              </div>
              <div>
                <h1 className="text-lg font-semibold text-slate-900 dark:text-white">
                  Document Converter
                </h1>
                <p className="text-xs text-slate-500 dark:text-slate-400">
                  Bulk PDF/MD to Optimized Markdown
                </p>
              </div>
            </div>

            {/* Header actions */}
            <div className="flex items-center gap-2">
              {/* System status indicator */}
              {systemInfo && (
                <span className={`hidden sm:flex items-center gap-1.5 px-2 py-1 rounded text-xs ${
                  systemInfo.pdf_support 
                    ? 'bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-300'
                    : 'bg-amber-100 dark:bg-amber-900/30 text-amber-700 dark:text-amber-300'
                }`}>
                  <span className={`w-1.5 h-1.5 rounded-full ${systemInfo.pdf_support ? 'bg-green-500' : 'bg-amber-500'}`} />
                  PDF {systemInfo.pdf_support ? 'Ready' : 'Limited'}
                </span>
              )}

              <button
                onClick={() => setShowSettings(!showSettings)}
                className={`p-2 rounded-lg transition-colors ${
                  showSettings 
                    ? 'bg-primary-100 dark:bg-primary-900/30 text-primary-600 dark:text-primary-400'
                    : 'text-slate-500 hover:text-slate-700 dark:hover:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700'
                }`}
                title="Settings"
              >
                <Settings className="w-5 h-5" />
              </button>

              <button
                onClick={() => setDarkMode(!darkMode)}
                className="p-2 text-slate-500 hover:text-slate-700 dark:hover:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700 rounded-lg transition-colors"
                title={darkMode ? 'Light mode' : 'Dark mode'}
              >
                {darkMode ? <Sun className="w-5 h-5" /> : <Moon className="w-5 h-5" />}
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Main content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Left column - Upload and Queue */}
          <div className="lg:col-span-2 space-y-6">
            {/* File uploader */}
            <section>
              <h2 className="text-lg font-medium text-slate-900 dark:text-slate-100 mb-4">
                Upload Documents
              </h2>
              <FileUploader 
                onFilesSelected={handleFilesSelected} 
                disabled={isLoading}
              />
            </section>

            {/* Queue status bar */}
            <section className="bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 p-4">
              <div className="flex items-center justify-between flex-wrap gap-4">
                {/* Status counts */}
                <div className="flex items-center gap-4 text-sm">
                  <StatusBadge label="Total" count={queueStatus.total_jobs} />
                  <StatusBadge label="Pending" count={queueStatus.pending} color="slate" />
                  <StatusBadge label="Processing" count={queueStatus.in_progress} color="blue" />
                  <StatusBadge label="Completed" count={queueStatus.completed} color="green" />
                  <StatusBadge label="Failed" count={queueStatus.failed} color="red" />
                </div>

                {/* Queue controls */}
                <div className="flex items-center gap-2">
                  {!queueStatus.is_processing ? (
                    <button
                      onClick={handleStart}
                      disabled={queueStatus.pending === 0}
                      className="flex items-center gap-1.5 px-3 py-1.5 bg-green-600 hover:bg-green-700 disabled:bg-slate-300 dark:disabled:bg-slate-700 text-white rounded-lg text-sm font-medium transition-colors"
                    >
                      <Play className="w-4 h-4" />
                      Start
                    </button>
                  ) : queueStatus.is_paused ? (
                    <button
                      onClick={handleResume}
                      className="flex items-center gap-1.5 px-3 py-1.5 bg-green-600 hover:bg-green-700 text-white rounded-lg text-sm font-medium transition-colors"
                    >
                      <Play className="w-4 h-4" />
                      Resume
                    </button>
                  ) : (
                    <button
                      onClick={handlePause}
                      className="flex items-center gap-1.5 px-3 py-1.5 bg-amber-600 hover:bg-amber-700 text-white rounded-lg text-sm font-medium transition-colors"
                    >
                      <Pause className="w-4 h-4" />
                      Pause
                    </button>
                  )}

                  {queueStatus.is_processing && (
                    <button
                      onClick={handleStop}
                      className="flex items-center gap-1.5 px-3 py-1.5 bg-red-600 hover:bg-red-700 text-white rounded-lg text-sm font-medium transition-colors"
                    >
                      <Square className="w-4 h-4" />
                      Stop
                    </button>
                  )}

                  <div className="h-6 w-px bg-slate-200 dark:bg-slate-700" />

                  {queueStatus.completed > 0 && (
                    <button
                      onClick={handleDownloadAll}
                      className="flex items-center gap-1.5 px-3 py-1.5 text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700 rounded-lg text-sm font-medium transition-colors"
                    >
                      <Download className="w-4 h-4" />
                      Download All
                    </button>
                  )}

                  <button
                    onClick={handleClearCompleted}
                    disabled={queueStatus.completed === 0 && queueStatus.failed === 0}
                    className="p-1.5 text-slate-500 hover:text-slate-700 dark:hover:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700 disabled:opacity-50 rounded-lg transition-colors"
                    title="Clear completed"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>

                  <button
                    onClick={refreshQueue}
                    className="p-1.5 text-slate-500 hover:text-slate-700 dark:hover:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700 rounded-lg transition-colors"
                    title="Refresh"
                  >
                    <RefreshCw className="w-4 h-4" />
                  </button>
                </div>
              </div>
            </section>

            {/* Job queue */}
            <section>
              <h2 className="text-lg font-medium text-slate-900 dark:text-slate-100 mb-4">
                Conversion Queue
              </h2>
              <JobQueue
                jobs={jobs}
                onRemove={handleRemoveJob}
                onRetry={handleRetryJob}
                onPreview={handlePreviewJob}
                onDownload={handleDownloadJob}
                isProcessing={queueStatus.is_processing}
              />
            </section>
          </div>

          {/* Right column - Settings */}
          <div className="space-y-6">
            {showSettings && config && (
              <SettingsPanel
                config={config}
                onSave={handleSaveConfig}
                onReset={handleResetConfig}
              />
            )}

            {/* Quick stats */}
            {systemInfo?.statistics && (
              <div className="bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 p-4">
                <div className="flex items-center gap-2 mb-4">
                  <BarChart3 className="w-5 h-5 text-slate-500" />
                  <h3 className="font-medium text-slate-900 dark:text-slate-100">Statistics</h3>
                </div>
                <div className="grid grid-cols-2 gap-4 text-sm">
                  <div>
                    <p className="text-slate-500 dark:text-slate-400">Total Conversions</p>
                    <p className="text-2xl font-semibold text-slate-900 dark:text-slate-100">
                      {systemInfo.statistics.total_conversions || 0}
                    </p>
                  </div>
                  <div>
                    <p className="text-slate-500 dark:text-slate-400">Avg Duration</p>
                    <p className="text-2xl font-semibold text-slate-900 dark:text-slate-100">
                      {formatDuration(systemInfo.statistics.average_duration_ms)}
                    </p>
                  </div>
                </div>
              </div>
            )}

            {/* Help text */}
            <div className="bg-primary-50 dark:bg-primary-900/20 rounded-xl p-4 border border-primary-200 dark:border-primary-800">
              <h3 className="font-medium text-primary-900 dark:text-primary-100 mb-2">
                Quick Start
              </h3>
              <ol className="text-sm text-primary-700 dark:text-primary-300 space-y-2 list-decimal list-inside">
                <li>Drag & drop files or click to upload</li>
                <li>Adjust settings if needed</li>
                <li>Click Start to begin conversion</li>
                <li>Preview or download completed files</li>
              </ol>
            </div>
          </div>
        </div>
      </main>

      {/* Preview modal */}
      {preview && (
        <PreviewModal
          preview={preview}
          onClose={() => setPreview(null)}
          onDownload={() => handleDownloadJob(preview.job_id)}
        />
      )}

      {/* Toast notifications */}
      <ToastContainer toasts={toasts} onRemove={removeToast} />
    </div>
  );
}

function StatusBadge({ label, count, color = 'primary' }) {
  const colors = {
    primary: 'bg-primary-100 dark:bg-primary-900/30 text-primary-700 dark:text-primary-300',
    slate: 'bg-slate-100 dark:bg-slate-700 text-slate-700 dark:text-slate-300',
    blue: 'bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300',
    green: 'bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-300',
    red: 'bg-red-100 dark:bg-red-900/30 text-red-700 dark:text-red-300'
  };

  return (
    <span className={`inline-flex items-center gap-1 px-2 py-0.5 rounded ${colors[color]}`}>
      <span className="font-medium">{count}</span>
      <span className="text-xs opacity-75">{label}</span>
    </span>
  );
}

function formatDuration(ms) {
  if (!ms || ms === 0) return '0s';
  if (ms < 1000) return `${Math.round(ms)}ms`;
  if (ms < 60000) return `${(ms / 1000).toFixed(1)}s`;
  return `${(ms / 60000).toFixed(1)}m`;
}
