import requests
from api.urls import *

# Pet controller: https://petstore.swagger.io/

def get_pets_by_status(status: str):
    response = requests.get(GET_PETS_BY_STATUS_URL(status))
    return response


def get_pet_by_id(pet_id: int):
    response = requests.get(GET_PET_BY_ID_URL(pet_id))
    return response