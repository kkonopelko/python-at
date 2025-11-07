import json
from typing import Dict, Any
from pathlib import Path

class ConfigManager:
    """
    Configuration manager similar to C# IConfiguration.
    Loads settings from JSON files with environment-specific overrides.
    """
     
    _instance = None
    _config_data = None
    
    def __new__(cls):
        # Singleton pattern to ensure single config instance
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._config_data is None:
            self._load_config()
    
    def _load_config(self):
        """Load configuration from JSON file."""
        # Get project root directory
        project_root = Path(__file__).parent.parent
        config_file = project_root / "config" / "settings.json"
        
        try:
            with open(config_file, 'r', encoding='utf-8') as file:
                self._config_data = json.load(file)
                print(f"Configuration loaded from: {config_file}")
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found: {config_file}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in configuration file: {e}")
    
    def get_config_value(self, path: str, default: Any = None) -> Any:
        """
        Get configuration value using dot notation path.
        Examples:
            get_config_value('api.base_url')
            get_config_value('database.connection_string')
            get_config_value('driver_settings.browser')
        """
        try:
            # Navigate through nested dictionary using dot notation
            keys = path.split('.')
            value = self._config_data
            
            for key in keys:
                value = value[key]
            
            return value
        except KeyError:
            if default is not None:
                return default
            raise KeyError(f"Configuration key not found: {path}")
    
    @property
    def database_connection(self) -> str:
        """Get database connection string for current environment."""
        return self.get_config_value('database.connection_string')

    @property
    def store_api_base_url(self) -> str:
        """Get API base URL for store service."""
        return self.get_config_value('api.store_base_url')
    
    @property
    def user_api_base_url(self) -> str:
        """Get API base URL for user service."""
        return self.get_config_value('api.user_base_url')
    
    @property
    def api_timeout(self) -> int:
        """Get API timeout for current environment."""
        return self.get_config_value('api.timeout')
    
    @property
    def retry_attempts(self) -> int:
        """Get API retry attempts."""
        return self.get_config_value('api.retry_attempts')
    
    @property
    def web_base_url(self) -> str:
        """Get web base URL."""
        return self.get_config_value('web.base_url')
    
    @property
    def browser_type(self) -> str:
        """Get browser type setting."""
        return self.get_config_value('driver_settings.browser')
    
    @property
    def headless_mode(self) -> bool:
        """Get headless browser setting."""
        return self.get_config_value('driver_settings.headless')
    
    @property
    def slow_motion(self) -> int:
        """Get slow motion setting."""
        return self.get_config_value('driver_settings.slow_mo')
    
    @property
    def trace_directory(self) -> str:
        """Get trace directory setting."""
        return self.get_config_value('driver_settings.trace_report_directory')
    
    def get_all_config(self) -> Dict[str, Any]:
        """Get entire configuration."""
        return self._config_data
    
    @property
    def log_level(self) -> str:
        """Get logging level."""
        return self.get_config_value('logging.level')
    
    @property
    def log_file_path(self) -> str:
        """Get log file path."""
        return self.get_config_value('logging.file_path')
    
    def get_driver_setting(self, setting_key: str, default: Any = None) -> Any:
        """Get driver setting by key."""
        return self.get_config_value(f'driver_settings.{setting_key}', default)

# Global instance - similar to dependency injection in C#
config = ConfigManager()