from typing import List

class Stream:
    expects: List[str]
    last_ch: int
    trunc: str

    def __init__(self) -> None: ...

    def complete(self, chunk: str) -> str: ...
