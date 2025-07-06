import pytest

from api_client.api_aggregator import ApiClientAggregator
from constants.data import BASE_URL, HTTPStatusCodes
from constants.dataclasses import UserModel
from constants.endpoints import Endpoints
from constants.hardcoded_data import user_data


@pytest.fixture(scope="session", autouse=True)
def api_client():
    return ApiClientAggregator(base_url=BASE_URL)

@pytest.fixture
def create_default_user(api_client: ApiClientAggregator) -> UserModel:
    response = api_client.client.post(Endpoints.USER, json=user_data.to_dict())
    api_client.asserts.assert_status_code(response, HTTPStatusCodes.OK)
    return user_data