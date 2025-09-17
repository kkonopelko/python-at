import string
from api.error_messages import *
from api.clients.task_client import *


class TestTaskEndpoints: 
    def test_create_task_should_return_200(self):

        # Arrange
        expected_data = {
            "content": string.ascii_lowercase,
            "user_id": string.ascii_lowercase,
            "is_done": False
        }

        # Act
        response = create_task(expected_data)

        # Assert
        assert response.status_code == 200

        actual_data = response.json()
        assert actual_data["task"]["user_id"] == expected_data["user_id"]
        assert actual_data["task"]["content"] == expected_data["content"]


    def test_get_task_by_id_should_return_200(self):

        # Arrange
        expected_data = {
            "content": string.ascii_lowercase,
            "user_id": string.ascii_lowercase,
            "is_done": False
        }

        create_response = create_task(expected_data)
        task_id = create_response.json()["task"]["task_id"]

        # Act
        response = get_task_by_id(task_id)

        # Assert
        assert response.status_code == 200

        actual_data = response.json()
        assert actual_data["user_id"] == expected_data["user_id"]
        assert actual_data["content"] == expected_data["content"]


    def test_get_task_by_id_should_return_404_if_task_id_not_exists(self):

        # Arrange
        task_id = string.ascii_lowercase
         
        # Act
        response = get_task_by_id(task_id)

        # Assert
        assert response.status_code == 404

        actual_data = response.json()
        assert actual_data["detail"] == task_not_found(task_id)
