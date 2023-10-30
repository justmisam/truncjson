from typing import List
import unittest
from truncjson.Stream import Stream


class TestStream(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_complete_method(self) -> None:
        stream = Stream()
        chunks: List[str] = [
            '{"k1":"v1","k2":2',
            '0.5,"k3":[12,34,"56",tr',
            'ue,{"k31":"v31","k32":false,"k33":n'
        ]
        completions: List[str] = [
            '}',
            'ue]}',
            'ull}]}'
        ]
        for i in range(len(chunks)):
            assert stream.complete(chunks[i]) == ''.join(chunks[:i + 1]) + completions[i]

if __name__ == '__main__':
    unittest.main()
