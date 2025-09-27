import requests
from api.urls import *

# Represents store controller: https://petstore.swagger.io/         
class StoreClient:

    def get_store_order_by_id(self, order_id: int):
        response = requests.get(STORE_ORDER_BY_ID_URL(order_id))
        return response

    def delete_store_order_by_id(self, order_id: int):
        response = requests.delete(STORE_ORDER_BY_ID_URL(order_id))
        return response

    def add_store_order(self, order_data: dict):
        response = requests.post(STORE_ORDER_URL, json=order_data)
        return response