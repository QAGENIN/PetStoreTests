import pytest

from api_client.api_aggregator import ApiClientAggregator
from constants.data import BASE_URL


@pytest.fixture(scope="session", autouse=True)
def api_client():
    return ApiClientAggregator(base_url=BASE_URL)