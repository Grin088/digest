class DataBaseObjectException(Exception):
    """Custom exception when fetch object from database or create row in database"""

    def __init__(self, status_code: int, content=None, headers=None) -> None:
        self.status_code = status_code
        self.content = content
        self.headers = headers

    def __repr__(self):
        kwargs = []
        for key, value in self.__dict__.items():
            if not key.startswith("_"):
                kwargs.append(f"{key}={value!r}")
        return f"{self.__class__.__name__}({', '.join(kwargs)})"
