/**
 * API Service for Document Converter
 * Handles all HTTP requests to the backend API.
 */

const API_BASE = '/api';

/**
 * Generic fetch wrapper with error handling
 */
async function request(endpoint, options = {}) {
  const url = `${API_BASE}${endpoint}`;
  
  try {
    const response = await fetch(url, {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    });
    
    if (!response.ok) {
      const error = await response.json().catch(() => ({ detail: 'Unknown error' }));
      throw new Error(error.detail || `HTTP ${response.status}`);
    }
    
    // Handle empty responses
    const text = await response.text();
    return text ? JSON.parse(text) : {};
  } catch (error) {
    console.error(`API Error: ${endpoint}`, error);
    throw error;
  }
}

/**
 * Health check
 */
export async function healthCheck() {
  return request('/health');
}

/**
 * Get system info
 */
export async function getSystemInfo() {
  return request('/system/info');
}

/**
 * Upload files for conversion
 * @param {File[]} files - Array of files to upload
 * @returns {Promise<Object[]>} Array of created jobs
 */
export async function uploadFiles(files) {
  const formData = new FormData();
  files.forEach(file => formData.append('files', file));
  
  const response = await fetch(`${API_BASE}/upload`, {
    method: 'POST',
    body: formData,
  });
  
  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: 'Upload failed' }));
    throw new Error(error.detail);
  }
  
  return response.json();
}

/**
 * Get all jobs in queue
 */
export async function getQueue() {
  return request('/queue');
}

/**
 * Get queue status
 */
export async function getQueueStatus() {
  return request('/queue/status');
}

/**
 * Start queue processing
 */
export async function startQueue() {
  return request('/queue/start', { method: 'POST' });
}

/**
 * Pause queue processing
 */
export async function pauseQueue() {
  return request('/queue/pause', { method: 'POST' });
}

/**
 * Resume queue processing
 */
export async function resumeQueue() {
  return request('/queue/resume', { method: 'POST' });
}

/**
 * Stop queue processing
 */
export async function stopQueue() {
  return request('/queue/stop', { method: 'POST' });
}

/**
 * Clear all jobs from queue
 */
export async function clearQueue() {
  return request('/queue/clear', { method: 'DELETE' });
}

/**
 * Clear completed jobs
 */
export async function clearCompleted() {
  return request('/queue/clear-completed', { method: 'DELETE' });
}

/**
 * Get a specific job
 * @param {string} jobId - Job ID
 */
export async function getJob(jobId) {
  return request(`/jobs/${jobId}`);
}

/**
 * Delete a job
 * @param {string} jobId - Job ID
 */
export async function deleteJob(jobId) {
  return request(`/jobs/${jobId}`, { method: 'DELETE' });
}

/**
 * Retry a failed job
 * @param {string} jobId - Job ID
 */
export async function retryJob(jobId) {
  return request(`/jobs/${jobId}/retry`, { method: 'POST' });
}

/**
 * Download converted file
 * @param {string} jobId - Job ID
 */
export async function downloadResult(jobId) {
  const response = await fetch(`${API_BASE}/download/${jobId}`);
  if (!response.ok) {
    throw new Error('Download failed');
  }
  return response.blob();
}

/**
 * Download all completed conversions as zip
 */
export async function downloadAll() {
  const response = await fetch(`${API_BASE}/download/all`);
  if (!response.ok) {
    throw new Error('Download failed');
  }
  return response.blob();
}

/**
 * Get preview of converted content
 * @param {string} jobId - Job ID
 */
export async function getPreview(jobId) {
  return request(`/preview/${jobId}`);
}

/**
 * Get current configuration
 */
export async function getConfig() {
  return request('/config');
}

/**
 * Update configuration
 * @param {Object} updates - Configuration updates
 */
export async function updateConfig(updates) {
  return request('/config', {
    method: 'PUT',
    body: JSON.stringify(updates),
  });
}

/**
 * Get all configuration profiles
 */
export async function getProfiles() {
  return request('/config/profiles');
}

/**
 * Get a specific profile
 * @param {string} name - Profile name
 */
export async function getProfile(name) {
  return request(`/config/profiles/${name}`);
}

/**
 * Create a new profile
 * @param {string} name - Profile name
 * @param {Object} config - Configuration
 */
export async function createProfile(name, config) {
  return request('/config/profiles', {
    method: 'POST',
    body: JSON.stringify({ name, config }),
  });
}

/**
 * Delete a profile
 * @param {string} name - Profile name
 */
export async function deleteProfile(name) {
  return request(`/config/profiles/${name}`, { method: 'DELETE' });
}

/**
 * Apply a profile
 * @param {string} name - Profile name
 */
export async function applyProfile(name) {
  return request(`/config/profiles/${name}/apply`, { method: 'POST' });
}

/**
 * Get conversion history
 * @param {Object} params - Query parameters
 */
export async function getHistory(params = {}) {
  const query = new URLSearchParams(params).toString();
  return request(`/history${query ? `?${query}` : ''}`);
}

/**
 * Get statistics
 */
export async function getStatistics() {
  return request('/statistics');
}

/**
 * Clear history
 * @param {number} olderThanDays - Optional days filter
 */
export async function clearHistory(olderThanDays = null) {
  const query = olderThanDays ? `?older_than_days=${olderThanDays}` : '';
  return request(`/history${query}`, { method: 'DELETE' });
}

export default {
  healthCheck,
  getSystemInfo,
  uploadFiles,
  getQueue,
  getQueueStatus,
  startQueue,
  pauseQueue,
  resumeQueue,
  stopQueue,
  clearQueue,
  clearCompleted,
  getJob,
  deleteJob,
  retryJob,
  downloadResult,
  downloadAll,
  getPreview,
  getConfig,
  updateConfig,
  getProfiles,
  getProfile,
  createProfile,
  deleteProfile,
  applyProfile,
  getHistory,
  getStatistics,
  clearHistory,
};
