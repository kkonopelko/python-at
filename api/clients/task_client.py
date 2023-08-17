import requests
from api.urls import *


def create_task(body):
    response = requests.put(CREATE_TASK_URL, json=body)
    return response


def get_task_by_id(task_id):
    response = requests.get(GET_TASK_BY_ID_URL(task_id))
    return response
