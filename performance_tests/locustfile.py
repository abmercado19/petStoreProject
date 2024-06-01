from locust import HttpUser, task, between
from api_tests.features.steps.endpoints.store_endpoints import StoreEndpoints
from api_tests.features.steps.endpoints.user_endpoints import UserEndpoints
from api_tests.features.steps.endpoints.pet_endpoints import PetEndpoints
from api_tests.features.steps.steps_utils import get_config


class PetStore(HttpUser):
    wait_time = between(1, 3)
    store_endpoint = StoreEndpoints()
    user_endpoint = UserEndpoints()
    pet_endpoint = PetEndpoints()

    def on_start(self):
        print("*" * 40)
        print("Starting a new test run...")
        print("*" * 40)

    ''' PETS MANAGEMENT TESTS '''

    @task
    def test_get_existent_pet(self):
        get_pet_by_id_endpoint = self.pet_endpoint.get_pet_by_id_endpoint
        self.client.get(get_pet_by_id_endpoint.format('5'))

    @task
    def test_get_non_existent_pet(self):
        get_pet_by_id_endpoint = self.pet_endpoint.get_pet_by_id_endpoint
        with self.client.get(get_pet_by_id_endpoint.format('150'), catch_response=True) as response:
            if response.status_code == 404:
                response.success()

    @task
    def test_create_pet(self):
        create_pet_endpoint = self.pet_endpoint.pet_endpoint
        data = {"id": 80,
                "name": 'Cangrejo',
                "category": {"id": 1, "name": 'Dogs'},
                "photoUrls": ['url1', 'url2'],
                "tags": [{'id': '1', 'name': 'tag1'}, {'id': '2', 'name': 'tag2'}],
                "status": 'available'
                }
        self.client.post(create_pet_endpoint, json=data)

    @task
    def test_udpate_pet(self):
        update_pet_endpoint = self.pet_endpoint.pet_endpoint
        data = {"id": 53,
                "name": 'Cangrejo',
                "category": {"id": 1, "name": 'Dogs'},
                "photoUrls": ['url1', 'url2'],
                "tags": [{'id': '1', 'name': 'tag1'}, {'id': '2', 'name': 'tag2'}],
                "status": 'sold'
                }
        self.client.put(update_pet_endpoint, json=data)

    ''' STORE TRANSACTIONS TESTS '''

    @task
    def test_create_order(self):
        create_order_endpoint = self.store_endpoint.place_order_endpoint
        data = {"id": 70,
                "pet_id": 5,
                "quantity": 50,
                "shipDate": "2024-05-31T12:00:00",
                "status": 'approved',
                "complete": 'true'
                }
        self.client.post(create_order_endpoint, json=data)

    @task
    def get_order_by_existent_id(self):
        get_order_by_id_endpoint = self.store_endpoint.get_order_by_id_endpoint
        self.client.get(get_order_by_id_endpoint.format('70'))

    @task
    def get_order_by_non_existent_id(self):
        get_order_by_id_endpoint = self.store_endpoint.get_order_by_id_endpoint
        with self.client.get(get_order_by_id_endpoint.format('6'), catch_response=True) as response:
            if response.status_code == 404:
                response.success()

    @task
    def get_order_by_invalid_id(self):
        get_order_by_id_endpoint = self.store_endpoint.get_order_by_id_endpoint
        with self.client.get(get_order_by_id_endpoint.format('a'), catch_response=True) as response:
            if response.status_code == 400:
                response.success()

    ''' User management tests '''

    @task
    def login_with_valid_user_and_password(self):
        login_endpoint = self.user_endpoint.login_endpoint
        config = get_config()
        user_name = config['valid_user']['user_name']
        password = config['valid_user']['password']
        self.client.get(login_endpoint.format(user_name, password))

    @task
    def login_with_invalid_user_and_password(self):
        login_endpoint = self.user_endpoint.login_endpoint
        config = get_config()
        user_name = config['invalid_user']['user_name']
        password = config['invalid_user']['password']
        with self.client.get(login_endpoint.format(user_name, password), catch_response=True) as response:
            if response.status_code == 400:
                response.success()



