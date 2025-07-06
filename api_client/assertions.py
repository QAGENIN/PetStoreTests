from typing import Any, Dict, List, Optional, Union
from requests import Response
import json


class ApiAssertions:
    """
    Базовые утверждения для тестирования API
    """
    
    @staticmethod
    def assert_status_code(response: Response, expected_code: Union[int, List[int]]):
        """
        Проверяет статус код ответа
        """
        if isinstance(expected_code, list):
            assert response.status_code in expected_code, \
                f"Expected status code {expected_code}, got {response.status_code}, \n text: {response.text}"
        else:
            assert response.status_code == expected_code, \
                f"Expected status code {expected_code}, got {response.status_code}, \n text: {response.text}"
