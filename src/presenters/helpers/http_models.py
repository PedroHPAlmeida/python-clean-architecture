from typing import Dict, Any


class HttpRequest:
    """Class HttpRequest representation"""

    def __init__(
        self, header: Dict = None, body: Dict = None, query: Dict = None
    ) -> None:
        self.header = header
        self.body = body
        self.query = query

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (header={self.header}, body={self.body}, query={self.query})"


class HttpResponse:
    """Class HttpResponse representation"""

    def __init__(self, status_code: int, body: Any) -> None:
        self.status_code = status_code
        self.body = body

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (status_code={self.status_code}, body={self.body})"
