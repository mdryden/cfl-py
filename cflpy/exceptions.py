from typing import Optional


class ApiException(BaseException):
    def __init__(self, message: str, url: Optional[str] = None):
        self.message = message
        self.url = url


class InvalidParameters(BaseException):
    def __init__(self, message: str):
        self.message = message
