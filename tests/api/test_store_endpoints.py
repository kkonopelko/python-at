import random
from api.error_messages import *
from api.clients.store_client import *

class TestStoreEndpoints:

    # POST /store/order
    def test_add_order_should_return_200_and_placed_order_data(self):       
        
        # arrange
        test_order_data = {
            "id": 11,
            "petId": 22,
            "quantity": 1,
            "shipDate": "2025-09-19T12:30:16.212Z",
            "status": "placed",
            "complete": "true"
        }

        # act
        response = add_store_order(test_order_data)

        #assert
        assert response.status_code == 200        
        assert response.headers["Content-Type"] == "application/json"

        actual_order_data = response.json()
        assert actual_order_data, "Order data is not placed"
        assert actual_order_data["id"] == test_order_data["id"], "Order id is not correct"
        assert actual_order_data["petId"] == test_order_data["petId"], "Order petId is not correct"
        assert actual_order_data["quantity"] == test_order_data["quantity"], "Order quantity is not correct"


     # POST /st0re/order
    
    # POST /store/order
    def test_add_order_should_return_200_and_complete_false_order_status_if_no_data_was_passed(self):       
        
        # arrange
        empty_order_data = {}

        # act
        response = add_store_order(empty_order_data)

        #assert
        assert response.status_code == 200

        actual_order_data = response.json()
        assert actual_order_data["complete"] == False, "Order complete status is not correct"

    # GET /store/order/{id}
    def test_get_store_order_by_id_should_return_200(self):       
        
        existing_order_id = random.randint(1, 10)
        response = get_store_order_by_id(existing_order_id)

        assert response.status_code == 200        
        assert response.headers["Content-Type"] == "application/json"

        actual_order_data = response.json()
        assert actual_order_data, "Order data is empty"
        assert actual_order_data["id"] == existing_order_id, "Order id is not correct"

    # GET /store/order/{id}
    def test_get_store_order_by_id_should_return_404_if_id_not_exist(self):       
        
        not_existing_order_id = 1500

        response = get_store_order_by_id(not_existing_order_id)

        assert response.status_code == 404
        response_data = response.json()
        assert response_data["message"] == ORDER_NOT_FOUND_ERROR_MESSAGE

    # DELETE /store/order/{id}
    def test_delete_store_order_by_id_should_return_200(self):       
        
        # arrange
        test_order_data = {
            "id": 13,
            "petId": 22,
            "quantity": 1,
            "shipDate": "2025-09-19T12:30:16.212Z",
            "status": "placed",
            "complete": "true"
        }
         
        add_order_response = add_store_order(test_order_data)
        assert add_order_response.status_code == 200

        # act
        response = delete_store_order_by_id(test_order_data["id"])

        # assert
        assert response.status_code == 200        
        assert response.headers["Content-Type"] == "application/json"

        response_order_data = response.json()
        assert response_order_data["message"] == str(test_order_data["id"]), "Deleted order id is not correct"

        # check if order was deleted (can be checkd via DB)
        get_order_response = get_store_order_by_id(test_order_data["id"])
        assert get_order_response.status_code == 404

    # DELETE /store/order/{id}
    def test_delete_store_order_by_id_should_return_404_if_id_not_exist(self):       
        
        # arrange
        not_exist_order_id = 2000

        # act
        response = delete_store_order_by_id(not_exist_order_id)

        # assert
        assert response.status_code == 404
        response_data = response.json()
        assert response_data["message"].lower() == ORDER_NOT_FOUND_ERROR_MESSAGE.lower()