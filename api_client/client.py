from requests import Response, Request, Session
from requests.adapters import HTTPAdapter

from api_client.report import attach_request, attach_response
from api_client.utils import url_join, has_scheme
from petstore_qa.constants.data import HttpMethod, HTTP_MAX_RETRIES, HTTPStatusCodes


class ApiClient:
    def __init__(self, base_url: str, timeout: int = 30,):
        self._base_url = base_url
        self._timeout = timeout
        self._session = self._session = self.init_session()

    @staticmethod
    def init_session() -> Session:
        session = Session()
        session.mount('https://', HTTPAdapter(max_retries=HTTP_MAX_RETRIES))
        return session

    def _prepare_request(self, method: str, url: str, raise_for_status: bool = True, **kwargs) -> Response:
        request = Request(method=method, url=url, **kwargs)

        if has_scheme(request.url):
            raise ValueError(f'request.url must be relative, but got: {request.url}')

        request.url = url_join(self._base_url, request.url)

        prepared_request = self._session.prepare_request(request)
        attach_request(prepared_request)
        for attempt in range(HTTP_MAX_RETRIES):
            response = self._session.send(prepared_request, timeout=self._timeout, verify=False)
            if response.status_code in HTTPStatusCodes.SUCCESS:
                break

        attach_response(response)
        if raise_for_status:
            response.raise_for_status()
        return response

    def delete(self, path: str, raise_for_status: bool = True, **kwargs) -> Response:
        return self._prepare_request(method=HttpMethod.DELETE, url=path, raise_for_status=raise_for_status, **kwargs)

    def get(self, path: str, raise_for_status: bool = True, **kwargs) -> Response:
        return self._prepare_request(method=HttpMethod.GET, url=path, raise_for_status=raise_for_status, **kwargs)

    def patch(self, path: str, raise_for_status: bool = True, **kwargs) -> Response:
        return self._prepare_request(method=HttpMethod.PATCH, url=path, raise_for_status=raise_for_status, **kwargs)

    def post(self, path: str, raise_for_status: bool = True, **kwargs) -> Response:
        return self._prepare_request(method=HttpMethod.POST, url=path, raise_for_status=raise_for_status, **kwargs)

    def put(self, path: str, raise_for_status: bool = True, **kwargs) -> Response:
        return self._prepare_request(method=HttpMethod.PUT, url=path, raise_for_status=raise_for_status, **kwargs)

    def options(self, path: str, raise_for_status: bool = True, **kwargs) -> Response:
        return self._prepare_request(method=HttpMethod.OPTIONS, url=path, raise_for_status=raise_for_status, **kwargs)
