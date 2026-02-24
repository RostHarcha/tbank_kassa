class ClientResponseError(Exception):
    def __init__(
        self,
        *args,
        status_code: int,
        content: bytes | None,
    ) -> None:
        super().__init__(*args)
        self.status_code = status_code
        self.content = content
