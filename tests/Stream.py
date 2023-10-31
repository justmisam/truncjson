from typing import List
import unittest
from truncjson.Stream import Stream


class TestStream(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_extract_method(self) -> None:
        stream = Stream()
        chunks: List[str] = [
            'Here yo',
            'u go {"k1":"v1","k2":2',
            '0.5,"k3":[12,34,"56",tr',
            'ue,{"k31":"v31","k32":false,"k33":n',
            'ull}]}\nAnd ano',
            'ther one {"k',
            'ey":1.',
            '12} {"a',
            'b":"cd"}'
        ]
        objs: List[List[str]] = [
            [],
            ['{"k1":"v1","k2":2}'],
            ['{"k1":"v1","k2":20.5,"k3":[12,34,"56",true]}'],
            ['{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"v31","k32":false,"k33":null}]}'],
            ['{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"v31","k32":false,"k33":null}]}'],
            ['{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"v31","k32":false,"k33":null}]}', '{"k":null}'],
            ['{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"v31","k32":false,"k33":null}]}', '{"key":1.0}'],
            ['{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"v31","k32":false,"k33":null}]}', '{"key":1.12}', '{"a":null}'],
            ['{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"v31","k32":false,"k33":null}]}', '{"key":1.12}', '{"ab":"cd"}']
        ]
        for i in range(len(chunks)):
            extracted_objs = stream.extract(chunks[i])
            for j in range(len(extracted_objs)):
                assert extracted_objs[j] == objs[i][j]

if __name__ == '__main__':
    unittest.main()
