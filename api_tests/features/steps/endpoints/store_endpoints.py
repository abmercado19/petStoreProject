import os
import requests

from api_tests.features.steps.endpoints.endpoints_utils import base_url


class StoreEndpoints:

    def __init__(self):
        self.place_order_endpoint = os.path.join(base_url, "store/order")
        self.get_order_by_id_endpoint = os.path.join(base_url, "store/order/{}")

    def create_order(self, order_id, pet_id, order_quantity, order_ship_date, order_status, order_complete):
        data = {"id": order_id,
                "petId": pet_id,
                "quantity": order_quantity,
                "shipDate": order_ship_date,
                "status": order_status,
                "complete": order_complete
                }
        response = requests.post(self.place_order_endpoint, json=data)
        return response

    def get_order_by_id(self, order_id):
        response = requests.get(self.get_order_by_id_endpoint.format(order_id))
        return response

