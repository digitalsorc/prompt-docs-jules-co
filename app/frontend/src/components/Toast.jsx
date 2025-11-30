import React, { useEffect, useState } from 'react';
import { X, CheckCircle, XCircle, AlertTriangle, Info } from 'lucide-react';

/**
 * Toast notification component
 */
function Toast({ toast, onRemove }) {
  const [isExiting, setIsExiting] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => {
      setIsExiting(true);
      setTimeout(() => onRemove(toast.id), 300);
    }, toast.duration || 5000);

    return () => clearTimeout(timer);
  }, [toast, onRemove]);

  const icons = {
    success: <CheckCircle className="w-5 h-5 text-green-500" />,
    error: <XCircle className="w-5 h-5 text-red-500" />,
    warning: <AlertTriangle className="w-5 h-5 text-amber-500" />,
    info: <Info className="w-5 h-5 text-blue-500" />
  };

  const backgrounds = {
    success: 'bg-green-50 dark:bg-green-900/20 border-green-200 dark:border-green-800',
    error: 'bg-red-50 dark:bg-red-900/20 border-red-200 dark:border-red-800',
    warning: 'bg-amber-50 dark:bg-amber-900/20 border-amber-200 dark:border-amber-800',
    info: 'bg-blue-50 dark:bg-blue-900/20 border-blue-200 dark:border-blue-800'
  };

  return (
    <div
      className={`
        flex items-start gap-3 p-4 rounded-lg border shadow-lg
        ${backgrounds[toast.type] || backgrounds.info}
        ${isExiting ? 'toast-exit-active' : 'toast-enter-active'}
      `}
    >
      {icons[toast.type] || icons.info}
      <div className="flex-1">
        {toast.title && (
          <h4 className="font-medium text-slate-900 dark:text-slate-100">{toast.title}</h4>
        )}
        <p className="text-sm text-slate-700 dark:text-slate-300">{toast.message}</p>
      </div>
      <button
        onClick={() => onRemove(toast.id)}
        className="text-slate-400 hover:text-slate-600 dark:hover:text-slate-200"
      >
        <X className="w-4 h-4" />
      </button>
    </div>
  );
}

/**
 * Toast container component
 */
export function ToastContainer({ toasts, onRemove }) {
  if (!toasts || toasts.length === 0) return null;

  return (
    <div className="fixed bottom-4 right-4 z-50 flex flex-col gap-2 max-w-sm">
      {toasts.map(toast => (
        <Toast key={toast.id} toast={toast} onRemove={onRemove} />
      ))}
    </div>
  );
}

/**
 * Hook for managing toasts
 */
export function useToast() {
  const [toasts, setToasts] = useState([]);

  const addToast = (message, type = 'info', title = null, duration = 5000) => {
    const id = Date.now() + Math.random();
    setToasts(prev => [...prev, { id, message, type, title, duration }]);
    return id;
  };

  const removeToast = (id) => {
    setToasts(prev => prev.filter(t => t.id !== id));
  };

  const success = (message, title) => addToast(message, 'success', title);
  const error = (message, title) => addToast(message, 'error', title);
  const warning = (message, title) => addToast(message, 'warning', title);
  const info = (message, title) => addToast(message, 'info', title);

  return { toasts, addToast, removeToast, success, error, warning, info };
}

export default { ToastContainer, useToast };
