from typing import List
from .truncjson import Expect, get_expects, get_completion


class Stream:
    expects: List[Expect]
    last_ch: int
    trunc: str

    def __init__(self):
        self.expects = []
        self.last_ch = 0
        self.trunc = ''
    
    def complete(self, chunk: str) -> str:
        self.expects = get_expects(chunk, self.expects, self.last_ch)
        self.last_ch = ord(chunk[-1])
        completion = get_completion(self.expects)
        self.trunc += chunk
        return self.trunc + completion
