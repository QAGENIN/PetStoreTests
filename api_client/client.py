import functools
import time
from typing import Dict, Any, Optional, Union
from urllib.parse import urljoin

import allure
from requests import Response, RequestException
import requests


class ApiClient:
    """
    Универсальный API клиент
    """
    # Добавить ожидание ответа сервера
    
    def __init__(
        self,
        base_url: str,
        timeout: int = 30,
        cookie: Optional[Dict[str, str]] = None,
    ):
        self.base_url = base_url
        self.timeout = timeout
        self.cookie = cookie
        self._session = None

    @property
    def __session(self):
        """Ленивая инициализация сессии"""
        if self._session is None:
            self._session = requests.Session()
        return self._session

    def _build_url(self, endpoint: str) -> str:
        """Строит полный URL из базового URL и endpoint"""
        return urljoin(self.base_url, endpoint.lstrip("/"))

    @allure.step
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None, **kwargs) -> Response:
        url = self._build_url(endpoint)
        with allure.step(f'GET request to: {url}'):
            response = self.__session.get(url, params=params, timeout=self.timeout, **kwargs)
        return response

    @allure.step
    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None, json: Optional[Any] = None, **kwargs) -> Response:
        url = self._build_url(endpoint)
        with allure.step(f'POST request to: {url}'):
            response = self.__session.post(url, data=data, json=json, timeout=self.timeout, **kwargs)
        return response

    @allure.step
    def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None, json: Optional[Any] = None, **kwargs) -> Response:
        url = self._build_url(endpoint)
        with allure.step(f'PUT request to: {url}'):
            response = self.__session.put(url, data=data, json=json, timeout=self.timeout, **kwargs)
        return response

    @allure.step
    def delete(self, endpoint: str, **kwargs) -> Response:
        url = self._build_url(endpoint)
        with allure.step(f'DELETE request to: {url}'):
            response = self.__session.delete(url, timeout=self.timeout, **kwargs)
        return response

    @allure.step
    def patch(self, endpoint: str, data: Optional[Dict[str, Any]] = None, json: Optional[Any] = None, **kwargs) -> Response:
        url = self._build_url(endpoint)
        with allure.step(f'PATCH request to: {url}'):
            response = self.__session.patch(url, data=data, json=json, timeout=self.timeout, **kwargs)
        return response

    
