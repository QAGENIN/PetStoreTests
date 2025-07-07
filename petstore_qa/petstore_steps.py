import allure
from requests import Response

from api_client.client import ApiClient
from petstore_qa.constants.dataclasses import UserModel
from petstore_qa.constants.endpoints import Endpoints


class PetstoreSteps:
    def __init__(self, client: ApiClient):
        self.client = client

    @allure.step
    def create_user(self, user_model: UserModel) -> Response:
        with allure.step("POST: Сreate user"):
            return self.client.post(Endpoints.USER, json=user_model.to_dict())

    @allure.step
    def delete_user(self, username: str) -> Response:
        with allure.step("POST: Delete user"):
            return self.client.delete(f"{Endpoints.USER}/{username}")
