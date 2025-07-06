import json
import re
from typing import Dict, Any, List, Optional
from datetime import datetime


class ResponseHelper:
    """
    Помощник для работы с ответами API
    """
    
    @staticmethod
    def extract_field(response_data: Dict[str, Any], field_path: str) -> Any:
        """
        Извлекает значение поля по пути (например, 'user.profile.name')
        """
        fields = field_path.split('.')
        current = response_data
        
        for field in fields:
            if isinstance(current, dict) and field in current:
                current = current[field]
            else:
                raise KeyError(f"Field '{field}' not found in path '{field_path}'")
        
        return current
    
    @staticmethod
    def find_by_field(items: List[Dict[str, Any]], field: str, value: Any) -> Optional[Dict[str, Any]]:
        """
        Находит элемент в списке по значению поля
        """
        for item in items:
            if item.get(field) == value:
                return item
        return None
    
    @staticmethod
    def filter_by_field(items: List[Dict[str, Any]], field: str, value: Any) -> List[Dict[str, Any]]:
        """
        Фильтрует список по значению поля
        """
        return [item for item in items if item.get(field) == value]
    
    @staticmethod
    def sort_by_field(items: List[Dict[str, Any]], field: str, reverse: bool = False) -> List[Dict[str, Any]]:
        """
        Сортирует список по полю
        """
        return sorted(items, key=lambda x: x.get(field, ''), reverse=reverse)


class ValidationHelper:
    """
    Помощник для валидации данных
    """

    @staticmethod
    def is_valid_date(date_string: str) -> bool:
        """Проверяет валидность даты в ISO формате"""
        try:
            datetime.fromisoformat(date_string.replace('Z', '+00:00'))
            return True
        except ValueError:
            return False
    
    @staticmethod
    def validate_required_fields(data: Dict[str, Any], required_fields: List[str]) -> List[str]:
        """
        Проверяет наличие обязательных полей и возвращает список отсутствующих
        """
        missing_fields = []
        for field in required_fields:
            if field not in data or data[field] is None:
                missing_fields.append(field)
        return missing_fields


class JsonHelper:
    """
    Помощник для работы с JSON
    """
    
    @staticmethod
    def pretty_print(data: Any, indent: int = 2) -> str:
        """Форматирует JSON для красивого вывода"""
        return json.dumps(data, indent=indent, ensure_ascii=False)
    
    @staticmethod
    def save_to_file(data: Any, filename: str, indent: int = 2):
        """Сохраняет данные в JSON файл"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
    
    @staticmethod
    def load_from_file(filename: str) -> Any:
        """Загружает данные из JSON файла"""
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    @staticmethod
    def compare_json(obj1: Any, obj2: Any, ignore_fields: Optional[List[str]] = None) -> bool:
        """
        Сравнивает два JSON объекта, игнорируя указанные поля
        """
        if ignore_fields is None:
            ignore_fields = []
        
        def clean_obj(obj):
            if isinstance(obj, dict):
                return {k: clean_obj(v) for k, v in obj.items() if k not in ignore_fields}
            elif isinstance(obj, list):
                return [clean_obj(item) for item in obj]
            else:
                return obj
        
        return clean_obj(obj1) == clean_obj(obj2) 