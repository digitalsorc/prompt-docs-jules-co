"""
Configuration Management Module
Handles loading, saving, and managing conversion configuration profiles.
"""

import os
import json
import yaml
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path
from dataclasses import asdict

from .converter import ConversionConfig


class ConfigManager:
    """Manages conversion configuration profiles."""
    
    DEFAULT_CONFIG_DIR = "config_profiles"
    DEFAULT_PROFILE_NAME = "default"
    
    def __init__(self, config_dir: Optional[str] = None):
        """Initialize config manager.
        
        Args:
            config_dir: Directory to store configuration profiles
        """
        self.config_dir = config_dir or self.DEFAULT_CONFIG_DIR
        os.makedirs(self.config_dir, exist_ok=True)
        
        # Ensure default profile exists
        self._ensure_default_profile()
    
    def _ensure_default_profile(self) -> None:
        """Create default profile if it doesn't exist."""
        default_path = self._get_profile_path(self.DEFAULT_PROFILE_NAME)
        if not os.path.exists(default_path):
            default_config = ConversionConfig()
            self.save_profile(self.DEFAULT_PROFILE_NAME, default_config)
    
    def _get_profile_path(self, name: str, format: str = "json") -> str:
        """Get the file path for a profile."""
        return os.path.join(self.config_dir, f"{name}.{format}")
    
    def list_profiles(self) -> List[Dict[str, Any]]:
        """List all available configuration profiles.
        
        Returns:
            List of profile metadata dictionaries
        """
        profiles = []
        
        for filename in os.listdir(self.config_dir):
            if filename.endswith('.json') or filename.endswith('.yaml') or filename.endswith('.yml'):
                name = filename.rsplit('.', 1)[0]
                path = os.path.join(self.config_dir, filename)
                
                try:
                    stat = os.stat(path)
                    profiles.append({
                        "name": name,
                        "filename": filename,
                        "format": filename.rsplit('.', 1)[1],
                        "size": stat.st_size,
                        "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                        "is_default": name == self.DEFAULT_PROFILE_NAME
                    })
                except OSError:
                    continue
        
        return sorted(profiles, key=lambda x: (not x["is_default"], x["name"]))
    
    def load_profile(self, name: str) -> ConversionConfig:
        """Load a configuration profile by name.
        
        Args:
            name: Profile name
            
        Returns:
            ConversionConfig instance
            
        Raises:
            FileNotFoundError: If profile doesn't exist
            ValueError: If profile format is invalid
        """
        # Try JSON first, then YAML
        for ext in ['json', 'yaml', 'yml']:
            path = self._get_profile_path(name, ext)
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    if ext == 'json':
                        data = json.load(f)
                    else:
                        data = yaml.safe_load(f)
                
                return ConversionConfig.from_dict(data)
        
        raise FileNotFoundError(f"Configuration profile '{name}' not found")
    
    def save_profile(self, name: str, config: ConversionConfig, format: str = "json") -> str:
        """Save a configuration profile.
        
        Args:
            name: Profile name
            config: ConversionConfig instance
            format: File format ('json' or 'yaml')
            
        Returns:
            Path to saved profile
        """
        path = self._get_profile_path(name, format)
        data = config.to_dict()
        
        with open(path, 'w', encoding='utf-8') as f:
            if format == 'json':
                json.dump(data, f, indent=2)
            else:
                yaml.dump(data, f, default_flow_style=False)
        
        return path
    
    def delete_profile(self, name: str) -> bool:
        """Delete a configuration profile.
        
        Args:
            name: Profile name
            
        Returns:
            True if deleted, False if not found
            
        Raises:
            ValueError: If trying to delete default profile
        """
        if name == self.DEFAULT_PROFILE_NAME:
            raise ValueError("Cannot delete the default profile")
        
        for ext in ['json', 'yaml', 'yml']:
            path = self._get_profile_path(name, ext)
            if os.path.exists(path):
                os.remove(path)
                return True
        
        return False
    
    def duplicate_profile(self, source_name: str, target_name: str) -> str:
        """Duplicate a configuration profile.
        
        Args:
            source_name: Name of profile to duplicate
            target_name: Name for new profile
            
        Returns:
            Path to new profile
        """
        config = self.load_profile(source_name)
        return self.save_profile(target_name, config)
    
    def export_profile(self, name: str, output_path: str) -> str:
        """Export a profile to a specific location.
        
        Args:
            name: Profile name
            output_path: Where to save the export
            
        Returns:
            Path to exported file
        """
        config = self.load_profile(name)
        
        # Determine format from output path
        if output_path.endswith('.yaml') or output_path.endswith('.yml'):
            format = 'yaml'
        else:
            format = 'json'
        
        data = config.to_dict()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            if format == 'json':
                json.dump(data, f, indent=2)
            else:
                yaml.dump(data, f, default_flow_style=False)
        
        return output_path
    
    def import_profile(self, file_path: str, name: Optional[str] = None) -> str:
        """Import a profile from a file.
        
        Args:
            file_path: Path to profile file
            name: Optional name for imported profile
            
        Returns:
            Name of imported profile
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            if file_path.endswith('.yaml') or file_path.endswith('.yml'):
                data = yaml.safe_load(f)
            else:
                data = json.load(f)
        
        config = ConversionConfig.from_dict(data)
        
        if name is None:
            name = Path(file_path).stem
        
        self.save_profile(name, config)
        return name
    
    def get_default_config(self) -> ConversionConfig:
        """Get the default configuration.
        
        Returns:
            ConversionConfig instance
        """
        return self.load_profile(self.DEFAULT_PROFILE_NAME)
    
    def update_default_config(self, config: ConversionConfig) -> str:
        """Update the default configuration.
        
        Args:
            config: New default configuration
            
        Returns:
            Path to saved profile
        """
        return self.save_profile(self.DEFAULT_PROFILE_NAME, config)


# Singleton instance for convenience
_config_manager: Optional[ConfigManager] = None


def get_config_manager(config_dir: Optional[str] = None) -> ConfigManager:
    """Get or create the config manager singleton.
    
    Args:
        config_dir: Optional config directory (only used on first call)
        
    Returns:
        ConfigManager instance
    """
    global _config_manager
    if _config_manager is None:
        _config_manager = ConfigManager(config_dir)
    return _config_manager
