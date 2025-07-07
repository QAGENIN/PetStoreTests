from typing import Optional, NoReturn

import allure

from api_client.client import ApiClient
from api_client.utils import compare_json
from petstore_qa.constants.data import HTTPStatusCodes
from petstore_qa.constants.endpoints import Endpoints
from petstore_qa.constants.generated_data import user_data


class PetstoreAssertions:
    def __init__(self, client: ApiClient):
        self.client = client


    @allure.step
    def check_user_are_created(self, username: str) -> Optional[NoReturn]:
        with allure.step("GET: Сheck user created"):
            response_get_user = self.client.get(f"{Endpoints.USER}/{username}")
            if not compare_json(user_data.to_dict(), response_get_user.json()):
                raise AssertionError("User creation dict do not match")

    @allure.step("")
    def check_user_does_not_exist(self, username: str) -> Optional[NoReturn]:
        with allure.step("GET: Сheck user does not exist"):
            response_get_user = self.client.get(f"{Endpoints.USER}/{username}", raise_for_status=False)
            if response_get_user.status_code != HTTPStatusCodes.NOT_FOUND:
                raise AssertionError(f"Еhe user exists, but should not. Get user response status code {response_get_user.status_code}")

