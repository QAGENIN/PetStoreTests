import pytest
from _pytest.fixtures import SubRequest

from petstore_qa.api_aggregator import PetstoreAggregator
from petstore_qa.constants.annotations import YieldFixture
from petstore_qa.constants.data import BASE_URL
from petstore_qa.constants.dataclasses import UserModel
from petstore_qa.constants.generated_data import user_data


@pytest.fixture(scope="session")
def petstore():
    return PetstoreAggregator(base_url=BASE_URL)


@pytest.fixture
def creating_default_user(petstore: PetstoreAggregator) -> UserModel:
    petstore.steps.create_user(user_data)
    return user_data


@pytest.fixture
def deleting_user(request: SubRequest, petstore: PetstoreAggregator) -> YieldFixture[None]:
    user = request.param
    yield
    petstore.steps.delete_user(user.username)
