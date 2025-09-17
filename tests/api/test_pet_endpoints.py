import string
import pytest
import random
from api.error_messages import *
from api.clients.pet_client import *
from api.models.pet_status import * 

class TestPetEndpoints:

    # GET /pet/findByStatus?status={value}
    @pytest.mark.parametrize("status", [PetStatus.available, PetStatus.pending, PetStatus.sold])
    def test_get_pets_by_status_should_return_200_and_dataList_when_searchinBy_valid_status(self, status):       
        
        response = get_pets_by_status(status.name)

        assert response.status_code == 200        
        assert response.headers["Content-Type"] == "application/json"

        # check that the returned list is not empty and is a list
        actual_pets_list_data = response.json()
        assert actual_pets_list_data, "Pets list is None or empty"
        assert isinstance(actual_pets_list_data, list)

        # check response model: required fields, field types, field values
        required_fields = {"name", "photoUrls"}
        for pet in actual_pets_list_data:
            assert required_fields.issubset(pet.keys())
            assert isinstance(pet["name"], str), "Pet name field type is not a string"
            assert pet["status"] == status.name, "Pet status is not correct"

    # GET /pet/findByStatus?status={value}
    def test_get_pets_by_status_should_return_200_and_noData_when_searchingBy_invalid_status(self):       
        
        response = get_pets_by_status("invaliStatus")

        assert response.status_code == 200        
        assert response.headers["Content-Type"] == "application/json"

        # check that the returned list is empty
        actual_pets_list_data = response.json()
        assert not actual_pets_list_data, "Pets list is not empty"

    # GET /pet/{id}
    def test_get_pet_by_id_should_return_200(self):       
        
        existing_pet_id = 2
        response = get_pet_by_id(existing_pet_id)

        assert response.status_code == 200        
        assert response.headers["Content-Type"] == "application/json"

        actual_pet_data = response.json()
        assert actual_pet_data, "Pet data is empty"
        assert actual_pet_data["id"] == existing_pet_id, "Pet id is not correct"

    # GET /pet/{id}
    def test_get_pet_by_id_should_return_404_if_id_not_exists(self):       

        # Arrange
        non_existing_pet_id = 0

        # Act
        response = get_pet_by_id(non_existing_pet_id)

        # Assert
        assert response.status_code == 404     
        response_data = response.json()
        assert response_data["message"] == PET_NOT_FOUND_ERROR_MESSAGE