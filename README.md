# API Client Framework с Allure

Универсальный API клиент с поддержкой Allure отчетов для автоматизированного тестирования.

## Установка

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Установите Allure Command Line Tool:
   - **Windows**: `scoop install allure` или скачайте с [официального сайта](https://docs.qameta.io/allure/#_installing_a_commandline)
   - **macOS**: `brew install allure`
   - **Linux**: `sudo apt-add-repository ppa:qameta/allure && sudo apt-get update && sudo apt-get install allure`

## Использование

### Базовое использование API клиента

```python
from api_client import ApiClient

# Создание клиента
client = ApiClient("https://api.example.com")

# Выполнение запросов
response = client.get("/users")
response = client.post("/users", json={"name": "John"})
```

### Запуск тестов с Allure

#### Автоматический запуск:
```bash
python run_tests_with_allure.py
```

#### Ручной запуск:
```bash
# Запуск тестов
pytest --alluredir=./allure-results --clean-alluredir -v

# Генерация отчета
allure generate ./allure-results --clean -o ./allure-report

# Открытие отчета
allure open ./allure-report
```

## Структура проекта

```
api_client/
├── client.py          # Основной API клиент
├── assertions.py      # Утилиты для проверок
├── utils.py          # Вспомогательные утилиты
├── allure_utils.py   # Утилиты для Allure
└── __init__.py

tests/
├── user_crud_tests.py # Тесты пользователей
└── conftest.py       # Конфигурация pytest

constants/
├── endpoints.py      # Константы эндпоинтов
└── hardcoded_data.py # Тестовые данные
```

## Allure Features

### Декораторы для тестов

```python
import allure

@allure.epic("API Testing")
@allure.feature("User Management")
@allure.story("Create User")
def test_create_user():
    with allure.step("Create new user"):
        # код теста
    pass
```

### Логирование в Allure

```python
from api_client import AllureSteps

# Логирование данных
AllureSteps.log_data(user_data, "User Data")

# Логирование проверок
AllureSteps.log_assertion("Status code", 200, response.status_code)
```

### Автоматическое логирование HTTP запросов

API клиент автоматически логирует все HTTP запросы и ответы в Allure с детальной информацией:
- URL и метод запроса
- Параметры запроса
- Тело запроса (JSON/Form data)
- Заголовки ответа
- Тело ответа

## Конфигурация

### pytest.ini
```ini
[tool:pytest]
addopts = 
    --alluredir=./allure-results
    --clean-alluredir
    -v
    --tb=short
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

## Зависимости

- `requests>=2.31.0` - HTTP клиент
- `pytest>=7.0.0` - фреймворк тестирования
- `allure-pytest>=2.13.0` - интеграция Allure с pytest
- `allure-python-commons>=2.13.0` - общие утилиты Allure

## Примеры отчетов

После запуска тестов с Allure вы получите детальный HTML отчет с:
- 📊 Статистикой выполнения тестов
- 🔍 Детальной информацией о каждом тесте
- 📝 Логами HTTP запросов и ответов
- 📋 Прикрепленными данными и скриншотами
- 📈 Графиками и диаграммами 