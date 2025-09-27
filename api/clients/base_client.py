import requests
from config.config_manager import config

"""
Base client class with common functionality for API clients.
Handles authentication, common headers, CRUD operations and base URL management.

"""
class BaseClient:
    
    def __init__(self, base_url: str):
        self.base_url = base_url # change setup?
        self.timeout = config.api_timeout
        self.retry_attempts = config.retry_attempts
        self.session = requests.Session()

    def get(self, endpoint: str, **kwargs):
        url = self.build_url(endpoint)
        return self.session.get(url, **kwargs)

    def authenticate(self):
        """Attach the API key header to the session (once)."""
        self.session.headers.update({"x-api-key": "reqres-free-v1"})

    def build_url(self, endpoint: str) -> str:
        """Build full URL for endpoint."""
        return f"{self.base_url}/{endpoint.lstrip('/')}"