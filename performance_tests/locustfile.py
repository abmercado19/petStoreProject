from locust import HttpUser, task, between


class PetStore(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        print("*" * 40)
        print("Starting a new test run...")
        print("*" * 40)

    @task
    def test_get_pet(self):
        get_pet_by_id_endpoint = "/api/v3/pet/{}"
        self.client.get(get_pet_by_id_endpoint.format('5'))

    @task
    def test_create_pet(self):
        create_pet_endpoint = "/api/v3/pet/"
        data = {"id": 80,
                "name": 'Cangrejo',
                "category": {"id": 1, "name": 'Dogs'},
                "photoUrls": ['url1', 'url2'],
                "tags": [{'id': '1', 'name': 'tag1'}, {'id': '2', 'name': 'tag2'}],
                "status": 'available'
                }
        self.client.post(create_pet_endpoint, json=data)

    @task
    def test_create_order(self):
        create_order_endpoint = "/api/v3/store/order"
        data = {"id": 70,
                "pet_id": 5,
                "quantity": 50,
                "shipDate": "2024-05-31T12:00:00",
                "status": 'approved',
                "complete": 'true'
                }
        self.client.post(create_order_endpoint, json=data)

