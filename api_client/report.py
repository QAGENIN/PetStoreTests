import functools
import json
from typing import Union

import allure
from requests import PreparedRequest, Response

_pretty_json = functools.partial(json.dumps, ensure_ascii=True, indent=4, sort_keys=True)


def _dump_request_body(request: PreparedRequest) -> str:
    if request.body is None:
        return ''
    try:
        request_body = request.body.decode() if isinstance(request.body, bytes) else request.body
        body = _pretty_json(json.loads(request_body))
    except ValueError:
        body = request.body
    return f'Body:\n{body}\n'


def _dump_response_body(response: Response) -> str:
    try:
        body = _pretty_json(response.json())
    except ValueError:
        body = response.content
    return f'Body:\n{body}\n'


def _dump_headers(obj: Union[PreparedRequest, Response]) -> str:
    return f'Headers:\n{_pretty_json(dict(obj.headers))}\n'


def _dump_method(obj: Union[PreparedRequest, Response]) -> str:
    return f'Method: {obj.method}\n'


def _dump_status(response: Response) -> str:
    return f'Status: {response.status_code} {response.reason}\n'


def _dump_url(obj: Union[PreparedRequest, Response]) -> str:
    return f'Url: "{obj.url}"\n'


def attach_request(request: PreparedRequest) -> None:
    request_dump = ''.join([
        _dump_method(request),
        _dump_url(request),
        _dump_headers(request),
        _dump_request_body(request)
    ])
    allure.attach(request_dump,
                  name=f'Request - {request.method} {request.path_url}',
                  attachment_type=allure.attachment_type.JSON)


def attach_response(response: Response) -> None:
    response_dump = ''.join([
        _dump_url(response),
        _dump_status(response),
        _dump_headers(response),
        _dump_response_body(response)
    ])
    allure.attach(response_dump,
                  name=f'Response - {response.status_code} {response.request.path_url}',
                  attachment_type=allure.attachment_type.JSON)

    content_type = response.headers.get('Content-Type')
    if content_type and content_type.startswith('text/html'):
        allure.attach(response.text,
                      name=f'Response (as HTML) - {response.status_code} {response.request.path_url}',
                      attachment_type=allure.attachment_type.HTML)
