import os
import requests

from api_tests.features.steps.steps_utils import tags_mapping
from api_tests.features.steps.endpoints.endpoints_utils import base_url


class PetEndpoints:

    def __init__(self):
        self.get_pet_by_id_endpoint = os.path.join(base_url, "pet/{}")
        self.pet_endpoint = os.path.join(base_url, "pet/")

    def get_pet_by_id(self, pet_id):
        response = requests.get(self.get_pet_by_id_endpoint.format(pet_id))
        return response

    def create_pet(self, pet_id, pet_name, pet_category_id, pet_category_name, pet_status, pet_photo_urls, pet_tags):
        data = {"id": pet_id,
                "name": pet_name,
                "category": {"id": pet_category_id, "name": pet_category_name},
                "photoUrls": pet_photo_urls,
                "tags": pet_tags,
                "status": pet_status
                }
        response = requests.post(self.pet_endpoint, json=data)
        return response

    def update_pet(self, pet_id, pet_name, pet_category_id, pet_category_name, pet_status, pet_photo_urls, pet_tags):
        data = {"id": pet_id,
                "name": pet_name,
                "category": {"id": pet_category_id, "name": pet_category_name},
                "photoUrls": pet_photo_urls,
                "tags": pet_tags,
                "status": pet_status
                }
        response = requests.put(self.pet_endpoint, json=data)
        return response

    @staticmethod
    def get_pet_tags_with_ids(pet_tags_names):
        pet_tags = []
        for tag in pet_tags_names:
            pet_tags.append({"id": tags_mapping[tag], "name": tag})
        return pet_tags

