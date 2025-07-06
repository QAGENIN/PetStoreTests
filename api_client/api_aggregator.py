from api_client import ApiAssertions, ApiClient, ResponseHelper


class ApiClientAggregator:
    def __init__(self, base_url: str):
        self._base_url = base_url

        self.client = ApiClient(base_url=self._base_url)
        self.asserts = ApiAssertions()
