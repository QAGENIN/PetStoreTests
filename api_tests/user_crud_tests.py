import allure
import pytest

from petstore_qa.api_aggregator import PetstoreAggregator
from petstore_qa.constants.annotations import YieldFixture
from petstore_qa.constants.dataclasses import UserModel
from petstore_qa.constants.generated_data import user_data


@pytest.mark.parametrize('deleting_user', [user_data], indirect=True, ids=["yield delete_user"])
@allure.feature('User flow')
@allure.story('Send create user request')
def test_create_user(petstore: PetstoreAggregator, deleting_user:  YieldFixture[None]):
    petstore.steps.create_user(user_data)
    petstore.asserts.check_user_are_created(username=user_data.username)


@allure.feature('User flow')
@allure.story('Send delete user request')
def test_delete_user(petstore: PetstoreAggregator, creating_default_user: UserModel):
    user = creating_default_user
    petstore.steps.delete_user(username=user.username)
    petstore.asserts.check_user_does_not_exist(username=user.username)
