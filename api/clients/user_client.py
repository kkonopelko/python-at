from api.clients.base_client import BaseClient
from config.config_manager import config
from api.urls import *

# Represents user controller: https://reqres.in/api-docs/     
class UserClient(BaseClient):

    def __init__(self):
        # Call BaseClient constructor with the base_url for users
        super().__init__(base_url=config.user_api_base_url)

    def get_user_by_id(self, id: int):
        response = self.get(USER_BY_ID_URL(id))
        return response