from time import sleep

import allure

from api_client.api_aggregator import ApiClientAggregator
from api_client.utils import JsonHelper, ResponseHelper
from constants.data import HTTPStatusCodes
from constants.dataclasses import UserModel
from constants.endpoints import Endpoints
from constants.hardcoded_data import user_data


@allure.feature('User flow')
@allure.story('Send create user request')
def test_create_user(api_client: ApiClientAggregator):
    with allure.step("POST: Сreate user"):
        response = api_client.client.post(Endpoints.USER, json=user_data.to_dict())
        api_client.asserts.assert_status_code(response, HTTPStatusCodes.OK)
    sleep(5) # sleep бесит
    with allure.step("GET: Сheck user created"):
        response_get_user = api_client.client.get(f"{Endpoints.USER}/{user_data.username}")
        api_client.asserts.assert_status_code(response_get_user, HTTPStatusCodes.OK)
        JsonHelper.compare_json(user_data.to_dict(), response_get_user.json())


@allure.feature('User flow')
@allure.story('Send delete user request')
def test_delete_user(api_client: ApiClientAggregator, create_default_user: UserModel):
    with allure.step("POST: Delete user"):
        user = create_default_user
        response = api_client.client.delete(f"{Endpoints.USER}/{user.username}")
        api_client.asserts.assert_status_code(response, HTTPStatusCodes.OK)
