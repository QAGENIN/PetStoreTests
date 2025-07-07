from api_client.client import ApiClient
from petstore_qa.petstore_asserts import PetstoreAssertions
from petstore_qa.petstore_steps import PetstoreSteps


class PetstoreAggregator:
    def __init__(self, base_url: str):
        self._base_url = base_url

        self.client = ApiClient(base_url=self._base_url)
        self.asserts = PetstoreAssertions(client=self.client)
        self.steps = PetstoreSteps(client=self.client)
