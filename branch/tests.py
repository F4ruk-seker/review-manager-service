from rest_framework.test import APITestCase
from django.urls import reverse


class BranchTestCase(APITestCase):
    url_create = reverse("api:branch:create")
    temp_branch_data: dict = {
            "name": "test branch",
            "url": "https://test.test/",
            "explanation": "test explanation"
        }
    temp_invalid_branch_data: dict = {
            "name": "test branch",
            "url": "invalid",
            "explanation": "test explanation"
        }

    def test_create_branch(self):
        response = self.client.post(self.url_create, self.temp_branch_data)
        self.assertEquals(201, response.status_code)

    def test_create_invalid_branch(self):
        response = self.client.post(self.url_create, self.temp_invalid_branch_data)
        self.assertEquals(400, response.status_code)

    def test_create_duplicate_branch(self):
        self.client.post(self.url_create, self.temp_branch_data)  # new branch
        response = self.client.post(self.url_create, self.temp_branch_data)  # duplicate branch
        self.assertEquals(400, response.status_code)

    def test_update_branch(self):
        response = self.client.post(self.url_create, self.temp_branch_data)  # new branch
        new_branch_id = response.data.get('id')
        url_path = reverse("api:branch:update_destroy_retrieve", kwargs={'id': new_branch_id})
        response = self.client.put(url_path, self.temp_branch_data)
        self.assertEquals(200, response.status_code)

    def test_update_invalid_data_branch(self):
        response = self.client.post(self.url_create, self.temp_branch_data)
        new_branch_id = response.data.get('id')
        url_path = reverse("api:branch:update_destroy_retrieve", kwargs={'id': new_branch_id})
        response = self.client.put(url_path, self.temp_invalid_branch_data)
        self.assertEquals(400, response.status_code)

    def test_update_invalid_id_branch(self):
        invalid_id: str = "invalid_id"
        url_path = reverse("api:branch:update_destroy_retrieve", kwargs={'id': invalid_id})
        response = self.client.put(url_path, self.temp_invalid_branch_data)
        self.assertEquals(404, response.status_code)

    def test_branch_destroy(self):
        response = self.client.post(self.url_create, self.temp_branch_data)  # new branch
        self.assertEquals(201, response.status_code)
        new_branch_id = response.data.get('id')
        url_path = reverse("api:branch:update_destroy_retrieve", kwargs={'id': new_branch_id})
        response = self.client.delete(url_path, self.temp_branch_data)
        self.assertEquals(204, response.status_code)

    def test_branch_invalid_id_destroy(self):
        invalid_id: str = "invalid_id"
        url_path = reverse("api:branch:update_destroy_retrieve", kwargs={'id': invalid_id})
        response = self.client.delete(url_path, self.temp_branch_data)
        self.assertEquals(404, response.status_code)

    def test_branch_retrieve(self):
        response = self.client.post(self.url_create, self.temp_branch_data)  # new branch
        self.assertEquals(201, response.status_code)
        new_branch_id = response.data.get('id')
        url_path = reverse("api:branch:update_destroy_retrieve", kwargs={'id': new_branch_id})
        response = self.client.get(url_path, self.temp_branch_data)
        self.assertEquals(200, response.status_code)

    def test_branch_invalid_id_retrieve(self):
        invalid_id: str = "invalid_id"
        url_path = reverse("api:branch:update_destroy_retrieve", kwargs={'id': invalid_id})
        response = self.client.get(url_path, self.temp_branch_data)
        self.assertEquals(404, response.status_code)


