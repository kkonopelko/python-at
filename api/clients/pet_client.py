import requests
from api.urls import *

# Represents pet controller: https://petstore.swagger.io/
class PetClient:

    def get_pets_by_status(self, status: str):
        response = requests.get(GET_PETS_BY_STATUS_URL(status))
        return response

    def get_pet_by_id(self, pet_id: int):
        response = requests.get(GET_PET_BY_ID_URL(pet_id))
        return response