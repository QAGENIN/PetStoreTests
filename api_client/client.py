from typing import Dict, Any, Optional, Union
from urllib.parse import urljoin
from requests import Response
import requests


class ApiClient:
    """
    Универсальный API клиент
    """
    
    def __init__(
        self,
        base_url: str,
        connect_timeout: int = 30,
        read_timeout: int = 10,
        cookie: Optional[Dict[str, str]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
    ):
        self.base_url = base_url
        self.timeout = (connect_timeout, read_timeout)
        self.cookie = cookie
        self.extra_headers = extra_headers
        self._session = None

    @property
    def session(self):
        """Ленивая инициализация сессии"""
        if self._session is None:
            self._session = requests.Session()
            if self.extra_headers:
                self._session.headers.update(self.extra_headers)
        return self._session

    def add_headers(self, headers: Dict[str, str]):
        """Добавляет заголовки к сессии"""
        self.session.headers.update(headers)

    def _build_url(self, endpoint: str) -> str:
        """Строит полный URL из базового URL и endpoint"""
        return urljoin(self.base_url, endpoint.lstrip("/"))

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None, **kwargs) -> Response:
        url = self._build_url(endpoint)
        response = self.session.get(url, params=params, timeout=self.timeout, **kwargs)
        return response

    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None, json: Optional[Any] = None, **kwargs) -> Response:
        url = self._build_url(endpoint)
        response = self.session.post(url, data=data, json=json, timeout=self.timeout, **kwargs)
        return response

    def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None, json: Optional[Any] = None, **kwargs) -> Response:
        url = self._build_url(endpoint)
        response = self.session.put(url, data=data, json=json, timeout=self.timeout, **kwargs)
        return response

    def delete(self, endpoint: str, **kwargs) -> Response:
        url = self._build_url(endpoint)
        response = self.session.delete(url, timeout=self.timeout, **kwargs)
        return response

    def patch(self, endpoint: str, data: Optional[Dict[str, Any]] = None, json: Optional[Any] = None, **kwargs) -> Response:
        url = self._build_url(endpoint)
        response = self.session.patch(url, data=data, json=json, timeout=self.timeout, **kwargs)
        return response

    
