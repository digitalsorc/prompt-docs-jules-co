import React from 'react';
import { 
  FileText, Trash2, RefreshCw, Download, Eye, Loader2,
  CheckCircle, XCircle, Clock, AlertCircle
} from 'lucide-react';

/**
 * JobQueue Component
 * Displays the conversion queue with status, progress, and actions.
 */
export default function JobQueue({ 
  jobs, 
  onRemove, 
  onRetry, 
  onPreview, 
  onDownload,
  isProcessing 
}) {
  if (!jobs || jobs.length === 0) {
    return (
      <div className="text-center py-12 text-slate-500 dark:text-slate-400">
        <FileText className="w-12 h-12 mx-auto mb-3 opacity-50" />
        <p>No files in queue</p>
        <p className="text-sm mt-1">Upload files to get started</p>
      </div>
    );
  }

  return (
    <div className="space-y-2">
      {jobs.map((job) => (
        <JobItem
          key={job.job_id}
          job={job}
          onRemove={() => onRemove(job.job_id)}
          onRetry={() => onRetry(job.job_id)}
          onPreview={() => onPreview(job.job_id)}
          onDownload={() => onDownload(job.job_id)}
        />
      ))}
    </div>
  );
}

function JobItem({ job, onRemove, onRetry, onPreview, onDownload }) {
  const statusConfig = {
    pending: {
      icon: Clock,
      color: 'text-slate-500',
      bg: 'bg-slate-100 dark:bg-slate-700',
      label: 'Pending'
    },
    in_progress: {
      icon: Loader2,
      color: 'text-primary-500',
      bg: 'bg-primary-100 dark:bg-primary-900/30',
      label: 'Converting',
      spin: true
    },
    completed: {
      icon: CheckCircle,
      color: 'text-green-500',
      bg: 'bg-green-100 dark:bg-green-900/30',
      label: 'Completed'
    },
    failed: {
      icon: XCircle,
      color: 'text-red-500',
      bg: 'bg-red-100 dark:bg-red-900/30',
      label: 'Failed'
    },
    cancelled: {
      icon: AlertCircle,
      color: 'text-amber-500',
      bg: 'bg-amber-100 dark:bg-amber-900/30',
      label: 'Cancelled'
    }
  };

  const status = statusConfig[job.status] || statusConfig.pending;
  const StatusIcon = status.icon;

  const formatFileSize = (bytes) => {
    if (bytes < 1024) return bytes + ' B';
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
    return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
  };

  return (
    <div className={`
      p-4 rounded-lg border transition-colors
      ${job.status === 'in_progress' ? 'border-primary-200 dark:border-primary-800' : 'border-slate-200 dark:border-slate-700'}
      bg-white dark:bg-slate-800
    `}>
      <div className="flex items-start gap-3">
        {/* File icon */}
        <div className={`p-2 rounded-lg ${status.bg}`}>
          <FileText className={`w-5 h-5 ${status.color}`} />
        </div>

        {/* File info */}
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2">
            <h4 className="font-medium text-slate-900 dark:text-slate-100 truncate">
              {job.filename}
            </h4>
            <span className="text-xs text-slate-500 dark:text-slate-400">
              {formatFileSize(job.file_size)}
            </span>
          </div>
          
          <div className="flex items-center gap-2 mt-1">
            <StatusIcon className={`w-4 h-4 ${status.color} ${status.spin ? 'animate-spin' : ''}`} />
            <span className={`text-sm ${status.color}`}>
              {job.message || status.label}
            </span>
          </div>

          {/* Progress bar for in-progress jobs */}
          {job.status === 'in_progress' && (
            <div className="mt-2">
              <div className="h-2 bg-slate-200 dark:bg-slate-700 rounded-full overflow-hidden">
                <div 
                  className="h-full bg-primary-500 rounded-full progress-bar"
                  style={{ width: `${job.progress * 100}%` }}
                />
              </div>
              <p className="text-xs text-slate-500 mt-1">
                {Math.round(job.progress * 100)}% complete
              </p>
            </div>
          )}

          {/* Error message */}
          {job.error && (
            <p className="mt-2 text-sm text-red-600 dark:text-red-400">
              {job.error}
            </p>
          )}
        </div>

        {/* Actions */}
        <div className="flex items-center gap-1">
          {job.status === 'completed' && (
            <>
              <button
                onClick={onPreview}
                className="p-2 text-slate-500 hover:text-primary-600 hover:bg-slate-100 dark:hover:bg-slate-700 rounded-lg transition-colors"
                title="Preview"
              >
                <Eye className="w-4 h-4" />
              </button>
              <button
                onClick={onDownload}
                className="p-2 text-slate-500 hover:text-green-600 hover:bg-slate-100 dark:hover:bg-slate-700 rounded-lg transition-colors"
                title="Download"
              >
                <Download className="w-4 h-4" />
              </button>
            </>
          )}
          
          {(job.status === 'failed' || job.status === 'cancelled') && (
            <button
              onClick={onRetry}
              className="p-2 text-slate-500 hover:text-amber-600 hover:bg-slate-100 dark:hover:bg-slate-700 rounded-lg transition-colors"
              title="Retry"
            >
              <RefreshCw className="w-4 h-4" />
            </button>
          )}
          
          {job.status !== 'in_progress' && (
            <button
              onClick={onRemove}
              className="p-2 text-slate-500 hover:text-red-600 hover:bg-slate-100 dark:hover:bg-slate-700 rounded-lg transition-colors"
              title="Remove"
            >
              <Trash2 className="w-4 h-4" />
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
