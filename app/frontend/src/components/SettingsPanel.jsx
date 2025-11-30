import React, { useState, useEffect } from 'react';
import { Settings, Save, RotateCcw, Info } from 'lucide-react';

/**
 * SettingsPanel Component
 * Comprehensive settings panel for conversion configuration.
 */
export default function SettingsPanel({ config, onSave, onReset }) {
  const [localConfig, setLocalConfig] = useState(config || {});
  const [activeTab, setActiveTab] = useState('quality');
  const [isDirty, setIsDirty] = useState(false);

  useEffect(() => {
    if (config) {
      setLocalConfig(config);
      setIsDirty(false);
    }
  }, [config]);

  const handleChange = (key, value) => {
    setLocalConfig(prev => ({ ...prev, [key]: value }));
    setIsDirty(true);
  };

  const handleSave = () => {
    onSave(localConfig);
    setIsDirty(false);
  };

  const handleReset = () => {
    onReset();
    setIsDirty(false);
  };

  const tabs = [
    { id: 'quality', label: 'Quality', icon: '✨' },
    { id: 'processing', label: 'Processing', icon: '⚙️' },
    { id: 'output', label: 'Output', icon: '📄' },
    { id: 'performance', label: 'Performance', icon: '🚀' }
  ];

  return (
    <div className="bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 overflow-hidden">
      {/* Header */}
      <div className="px-4 py-3 bg-slate-50 dark:bg-slate-900/50 border-b border-slate-200 dark:border-slate-700 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <Settings className="w-5 h-5 text-slate-500" />
          <h3 className="font-medium text-slate-900 dark:text-slate-100">Settings</h3>
        </div>
        <div className="flex items-center gap-2">
          {isDirty && (
            <span className="text-xs text-amber-600 dark:text-amber-400 bg-amber-100 dark:bg-amber-900/30 px-2 py-1 rounded">
              Unsaved changes
            </span>
          )}
          <button
            onClick={handleReset}
            className="p-2 text-slate-500 hover:text-slate-700 dark:hover:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700 rounded-lg transition-colors"
            title="Reset to defaults"
          >
            <RotateCcw className="w-4 h-4" />
          </button>
          <button
            onClick={handleSave}
            disabled={!isDirty}
            className={`px-3 py-1.5 rounded-lg text-sm font-medium flex items-center gap-1.5 transition-colors ${
              isDirty
                ? 'bg-primary-600 text-white hover:bg-primary-700'
                : 'bg-slate-100 dark:bg-slate-700 text-slate-400 cursor-not-allowed'
            }`}
          >
            <Save className="w-4 h-4" />
            Save
          </button>
        </div>
      </div>

      {/* Tabs */}
      <div className="flex border-b border-slate-200 dark:border-slate-700 overflow-x-auto">
        {tabs.map(tab => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            className={`px-4 py-3 text-sm font-medium whitespace-nowrap transition-colors ${
              activeTab === tab.id
                ? 'text-primary-600 dark:text-primary-400 border-b-2 border-primary-600 dark:border-primary-400'
                : 'text-slate-500 hover:text-slate-700 dark:hover:text-slate-300'
            }`}
          >
            <span className="mr-1.5">{tab.icon}</span>
            {tab.label}
          </button>
        ))}
      </div>

      {/* Content */}
      <div className="p-4 space-y-4">
        {activeTab === 'quality' && (
          <QualitySettings config={localConfig} onChange={handleChange} />
        )}
        {activeTab === 'processing' && (
          <ProcessingSettings config={localConfig} onChange={handleChange} />
        )}
        {activeTab === 'output' && (
          <OutputSettings config={localConfig} onChange={handleChange} />
        )}
        {activeTab === 'performance' && (
          <PerformanceSettings config={localConfig} onChange={handleChange} />
        )}
      </div>
    </div>
  );
}

function SettingRow({ label, description, children }) {
  return (
    <div className="flex items-start justify-between gap-4 py-3 border-b border-slate-100 dark:border-slate-700 last:border-0">
      <div className="flex-1">
        <label className="text-sm font-medium text-slate-700 dark:text-slate-200">{label}</label>
        {description && (
          <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">{description}</p>
        )}
      </div>
      <div className="flex-shrink-0">{children}</div>
    </div>
  );
}

function Toggle({ checked, onChange }) {
  return (
    <button
      onClick={() => onChange(!checked)}
      className={`relative w-11 h-6 rounded-full transition-colors ${
        checked ? 'bg-primary-600' : 'bg-slate-300 dark:bg-slate-600'
      }`}
    >
      <span
        className={`absolute top-1 w-4 h-4 bg-white rounded-full transition-transform ${
          checked ? 'left-6' : 'left-1'
        }`}
      />
    </button>
  );
}

function Select({ value, onChange, options }) {
  return (
    <select
      value={value}
      onChange={(e) => onChange(e.target.value)}
      className="px-3 py-1.5 bg-slate-100 dark:bg-slate-700 border-0 rounded-lg text-sm text-slate-700 dark:text-slate-200 focus:ring-2 focus:ring-primary-500"
    >
      {options.map(opt => (
        <option key={opt.value} value={opt.value}>{opt.label}</option>
      ))}
    </select>
  );
}

function NumberInput({ value, onChange, min, max }) {
  return (
    <input
      type="number"
      value={value}
      onChange={(e) => onChange(parseInt(e.target.value, 10))}
      min={min}
      max={max}
      className="w-20 px-3 py-1.5 bg-slate-100 dark:bg-slate-700 border-0 rounded-lg text-sm text-slate-700 dark:text-slate-200 focus:ring-2 focus:ring-primary-500"
    />
  );
}

function QualitySettings({ config, onChange }) {
  return (
    <>
      <SettingRow
        label="Optimization Level"
        description="How aggressively to optimize the output"
      >
        <Select
          value={config.optimization_level || 'standard'}
          onChange={(v) => onChange('optimization_level', v)}
          options={[
            { value: 'minimal', label: 'Minimal' },
            { value: 'standard', label: 'Standard' },
            { value: 'maximum', label: 'Maximum' }
          ]}
        />
      </SettingRow>

      <SettingRow
        label="Preserve Tables"
        description="Convert tables to markdown format"
      >
        <Toggle
          checked={config.preserve_tables !== false}
          onChange={(v) => onChange('preserve_tables', v)}
        />
      </SettingRow>

      <SettingRow
        label="Preserve Code Blocks"
        description="Detect and format code blocks"
      >
        <Toggle
          checked={config.preserve_code_blocks !== false}
          onChange={(v) => onChange('preserve_code_blocks', v)}
        />
      </SettingRow>

      <SettingRow
        label="Heading Structure"
        description="How to detect and format headings"
      >
        <Select
          value={config.heading_structure || 'auto'}
          onChange={(v) => onChange('heading_structure', v)}
          options={[
            { value: 'auto', label: 'Auto-detect' },
            { value: 'fixed', label: 'Fixed levels' }
          ]}
        />
      </SettingRow>

      <SettingRow
        label="Max Heading Level"
        description="Maximum heading depth (H2, H3, H4...)"
      >
        <NumberInput
          value={config.max_heading_level || 4}
          onChange={(v) => onChange('max_heading_level', v)}
          min={2}
          max={6}
        />
      </SettingRow>
    </>
  );
}

function ProcessingSettings({ config, onChange }) {
  return (
    <>
      <SettingRow
        label="Enable OCR"
        description="Use OCR for scanned PDFs (slower)"
      >
        <Toggle
          checked={config.enable_ocr === true}
          onChange={(v) => onChange('enable_ocr', v)}
        />
      </SettingRow>

      <SettingRow
        label="Language"
        description="Language for text processing"
      >
        <Select
          value={config.language || 'auto'}
          onChange={(v) => onChange('language', v)}
          options={[
            { value: 'auto', label: 'Auto-detect' },
            { value: 'en', label: 'English' },
            { value: 'es', label: 'Spanish' },
            { value: 'fr', label: 'French' },
            { value: 'de', label: 'German' },
            { value: 'zh', label: 'Chinese' }
          ]}
        />
      </SettingRow>

      <SettingRow
        label="Max File Size (MB)"
        description="Maximum file size to process"
      >
        <NumberInput
          value={config.max_file_size_mb || 100}
          onChange={(v) => onChange('max_file_size_mb', v)}
          min={1}
          max={500}
        />
      </SettingRow>

      <SettingRow
        label="Timeout (seconds)"
        description="Maximum time per document"
      >
        <NumberInput
          value={config.timeout_seconds || 300}
          onChange={(v) => onChange('timeout_seconds', v)}
          min={30}
          max={3600}
        />
      </SettingRow>

      <SettingRow
        label="Error Handling"
        description="How to handle conversion errors"
      >
        <Select
          value={config.error_handling || 'skip'}
          onChange={(v) => onChange('error_handling', v)}
          options={[
            { value: 'skip', label: 'Skip & Continue' },
            { value: 'halt', label: 'Stop Queue' }
          ]}
        />
      </SettingRow>
    </>
  );
}

function OutputSettings({ config, onChange }) {
  return (
    <>
      <SettingRow
        label="Filename Pattern"
        description="How to name output files"
      >
        <Select
          value={config.filename_pattern || 'kebab'}
          onChange={(v) => onChange('filename_pattern', v)}
          options={[
            { value: 'original', label: 'Keep Original' },
            { value: 'kebab', label: 'kebab-case' },
            { value: 'snake', label: 'snake_case' },
            { value: 'timestamp', label: 'Add Timestamp' }
          ]}
        />
      </SettingRow>

      <SettingRow
        label="Output Structure"
        description="Directory structure for output"
      >
        <Select
          value={config.output_structure || 'flat'}
          onChange={(v) => onChange('output_structure', v)}
          options={[
            { value: 'flat', label: 'Flat (all in one folder)' },
            { value: 'mirrored', label: 'Mirror input structure' }
          ]}
        />
      </SettingRow>

      <SettingRow
        label="Add Front Matter"
        description="Include YAML metadata at top"
      >
        <Toggle
          checked={config.add_front_matter !== false}
          onChange={(v) => onChange('add_front_matter', v)}
        />
      </SettingRow>

      <SettingRow
        label="Generate Summary"
        description="Auto-generate document summary"
      >
        <Toggle
          checked={config.generate_summary !== false}
          onChange={(v) => onChange('generate_summary', v)}
        />
      </SettingRow>

      <SettingRow
        label="Extract Keywords"
        description="Auto-extract topic keywords"
      >
        <Toggle
          checked={config.extract_keywords !== false}
          onChange={(v) => onChange('extract_keywords', v)}
        />
      </SettingRow>
    </>
  );
}

function PerformanceSettings({ config, onChange }) {
  return (
    <>
      <SettingRow
        label="Max Workers"
        description="Parallel conversion threads"
      >
        <NumberInput
          value={config.max_workers || 4}
          onChange={(v) => onChange('max_workers', v)}
          min={1}
          max={16}
        />
      </SettingRow>

      <SettingRow
        label="Memory Limit (MB)"
        description="Maximum memory usage per worker"
      >
        <NumberInput
          value={config.memory_limit_mb || 1024}
          onChange={(v) => onChange('memory_limit_mb', v)}
          min={256}
          max={8192}
        />
      </SettingRow>

      <SettingRow
        label="Cleanup Temp Files"
        description="Delete temporary files after conversion"
      >
        <Toggle
          checked={config.cleanup_temp_files !== false}
          onChange={(v) => onChange('cleanup_temp_files', v)}
        />
      </SettingRow>
    </>
  );
}
