import os
import requests

from api_tests.features.steps.endpoints.endpoints_utils import base_url


class UserEndpoints:

    def __init__(self):
        self.login_endpoint = os.path.join(base_url, "user/login")

    def login_user(self, user, password):
        data = {"user_name": user, "password": password}
        response = requests.get(self.login_endpoint, params=data)
        return response

