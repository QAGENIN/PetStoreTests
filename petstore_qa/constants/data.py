BASE_URL = "https://petstore.swagger.io/v2/"
HTTP_MAX_RETRIES = 5


class HttpMethod:
    CONNECT = 'CONNECT'
    DELETE = 'DELETE'
    GET = 'GET'
    HEAD = 'HEAD'
    OPTIONS = 'OPTIONS'
    PATCH = 'PATCH'
    POST = 'POST'
    PUT = 'PUT'
    TRACE = 'TRACE'


class HTTPStatusCodes:
    # Informational (1xx)
    CONTINUE = 100
    SWITCHING_PROTOCOLS = 101

    # Success (2xx)
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    SUCCESS = [OK, CREATED, ACCEPTED, NO_CONTENT]

    # Redirection (3xx)
    MOVED_PERMANENTLY = 301
    FOUND = 302
    NOT_MODIFIED = 304

    # Client Errors (4xx)
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    CONFLICT = 409

    # Server Errors (5xx)
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
