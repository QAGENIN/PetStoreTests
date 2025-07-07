import re
from typing import Any
from urllib.parse import urlparse


def has_scheme(url: str) -> bool:
    parsed_url = urlparse(url)
    return bool(parsed_url.scheme)


def url_join(*parts) -> str:
    url = "/".join([str(part) for part in parts if part])
    return re.sub(r"(?<!:)/{2,}", "/", url)


def compare_json(obj1: Any, obj2: Any) -> bool:
    return bool({k: v for k, v in obj1.items() if k in obj2 and obj2[k] == v})
