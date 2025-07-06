import allure

from api_client.api_aggregator import ApiClientAggregator
from constants.endpoints import Endpoints
from constants.hardcoded_data import user_data

@allure.feature('User flow')
@allure.story('Send create user request')
def test_create_user(api_client: ApiClientAggregator):
    with allure.step("POST: create user"):
        response = api_client.client.post(Endpoints.USER, json=user_data.to_dict())
        api_client.asserts.assert_status_code(response, 200)

    with allure.step("GET: check user created"):
        response_get_user = api_client.client.get(f"{Endpoints.USER}/{user_data.username}")
        api_client.asserts.assert_status_code(response_get_user, 200)
