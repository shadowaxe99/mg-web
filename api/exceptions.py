```python
class APIException(Exception):
    """Base exception class for API-related errors."""
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class NotFoundException(APIException):
    """Exception class for not found errors."""
    status_code = 404

    def __init__(self, message="Resource not found", payload=None):
        APIException.__init__(self, message, self.status_code, payload)


class BadRequestException(APIException):
    """Exception class for bad request errors."""
    status_code = 400

    def __init__(self, message="Bad request", payload=None):
        APIException.__init__(self, message, self.status_code, payload)


class UnauthorizedException(APIException):
    """Exception class for unauthorized access errors."""
    status_code = 401

    def __init__(self, message="Unauthorized access", payload=None):
        APIException.__init__(self, message, self.status_code, payload)


class ForbiddenException(APIException):
    """Exception class for forbidden access errors."""
    status_code = 403

    def __init__(self, message="Forbidden access", payload=None):
        APIException.__init__(self, message, self.status_code, payload)


class InternalServerErrorException(APIException):
    """Exception class for internal server errors."""
    status_code = 500

    def __init__(self, message="Internal server error", payload=None):
        APIException.__init__(self, message, self.status_code, payload)
```