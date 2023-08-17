import string
from api.error_messages import *
from api.clients.task_client import *


def test_create_task_should_return_200():
    expected_data = {
        "content": string.ascii_lowercase,
        "user_id": string.ascii_lowercase,
        "is_done": False
    }
    response = create_task(expected_data)
    assert response.status_code == 200
    actual_data = response.json()
    assert actual_data["task"]["user_id"] == expected_data["user_id"]
    assert actual_data["task"]["content"] == expected_data["content"]


def test_get_task_by_id_should_return_200():
    expected_data = {
        "content": string.ascii_lowercase,
        "user_id": string.ascii_lowercase,
        "is_done": False
    }
    create_response = create_task(expected_data)
    task_id = create_response.json()["task"]["task_id"]

    response = get_task_by_id(task_id)
    assert response.status_code == 200
    actual_data = response.json()
    assert actual_data["user_id"] == expected_data["user_id"]
    assert actual_data["content"] == expected_data["content"]


def test_get_task_by_id_should_return_404_if_task_id_not_exists():
    task_id = string.ascii_lowercase

    response = get_task_by_id(task_id)
    assert response.status_code == 404
    actual_data = response.json()
    assert actual_data["detail"] == task_not_found(task_id)
