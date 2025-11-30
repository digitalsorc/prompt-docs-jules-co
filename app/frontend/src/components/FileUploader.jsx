import React, { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { Upload, FileText, File, AlertCircle } from 'lucide-react';

/**
 * FileUploader Component
 * Drag-and-drop file upload zone with visual feedback.
 */
export default function FileUploader({ onFilesSelected, disabled = false }) {
  const onDrop = useCallback((acceptedFiles, rejectedFiles) => {
    if (rejectedFiles.length > 0) {
      console.warn('Some files were rejected:', rejectedFiles);
    }
    if (acceptedFiles.length > 0) {
      onFilesSelected(acceptedFiles);
    }
  }, [onFilesSelected]);

  const { getRootProps, getInputProps, isDragActive, isDragReject } = useDropzone({
    onDrop,
    disabled,
    accept: {
      'application/pdf': ['.pdf'],
      'text/markdown': ['.md', '.markdown'],
      'text/plain': ['.txt']
    },
    multiple: true
  });

  return (
    <div
      {...getRootProps()}
      className={`
        relative border-2 border-dashed rounded-xl p-8 text-center
        transition-all duration-200 cursor-pointer
        ${disabled ? 'opacity-50 cursor-not-allowed' : ''}
        ${isDragActive && !isDragReject ? 'border-primary-500 bg-primary-50 dark:bg-primary-900/20 dropzone-active' : ''}
        ${isDragReject ? 'border-red-500 bg-red-50 dark:bg-red-900/20' : ''}
        ${!isDragActive ? 'border-slate-300 dark:border-slate-600 hover:border-primary-400 hover:bg-slate-50 dark:hover:bg-slate-800/50' : ''}
      `}
    >
      <input {...getInputProps()} />
      
      <div className="flex flex-col items-center gap-4">
        <div className={`
          p-4 rounded-full 
          ${isDragActive ? 'bg-primary-100 dark:bg-primary-800' : 'bg-slate-100 dark:bg-slate-700'}
        `}>
          {isDragReject ? (
            <AlertCircle className="w-10 h-10 text-red-500" />
          ) : (
            <Upload className={`w-10 h-10 ${isDragActive ? 'text-primary-600 dark:text-primary-400' : 'text-slate-400 dark:text-slate-500'}`} />
          )}
        </div>
        
        <div>
          <p className="text-lg font-medium text-slate-700 dark:text-slate-200">
            {isDragActive
              ? isDragReject
                ? 'Unsupported file type'
                : 'Drop files here'
              : 'Drag & drop files here'}
          </p>
          <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">
            or click to browse
          </p>
        </div>
        
        <div className="flex gap-2 mt-2">
          <span className="inline-flex items-center gap-1 px-2 py-1 bg-red-100 dark:bg-red-900/30 text-red-700 dark:text-red-300 rounded text-xs font-medium">
            <FileText className="w-3 h-3" />
            PDF
          </span>
          <span className="inline-flex items-center gap-1 px-2 py-1 bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300 rounded text-xs font-medium">
            <File className="w-3 h-3" />
            MD
          </span>
          <span className="inline-flex items-center gap-1 px-2 py-1 bg-slate-100 dark:bg-slate-700 text-slate-700 dark:text-slate-300 rounded text-xs font-medium">
            <File className="w-3 h-3" />
            TXT
          </span>
        </div>
      </div>
    </div>
  );
}
