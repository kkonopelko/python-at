import pytest
from api.clients.user_client import UserClient
from api.error_messages import *
from api.clients.pet_client import *
from api.models.pet_status import *

@pytest.mark.api
@pytest.mark.regression
class TestUserEndpoints:

    # GET /users/{id}
    def test_get_user_by_id_should_return_200(self):
        
        # arrange
        existing_user_id = 1
        user_client = UserClient()
        user_client.authenticate()

        #act
        response = user_client.get_user_by_id(existing_user_id)

        #assert
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    # GET /users/{id}
    def test_get_user_by_id_should_return_401_for_not_authenticated_user(self):
        
        # arrange
        existing_user_id = 1
        user_client = UserClient()

        #act
        response = user_client.get_user_by_id(existing_user_id)

        #assert
        assert response.status_code == 401, f"Expected status code 401 but got {response.status_code}"