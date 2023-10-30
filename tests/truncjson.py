import unittest
from truncjson.truncjson import complete


class TestTruncjson(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_complete_function_case_1(self) -> None:
        assert complete('{') == '{}'

    def test_complete_function_case_2(self) -> None:
        assert complete('{"') == '{"":null}'

    def test_complete_function_case_3(self) -> None:
        assert complete('{"k') == '{"k":null}'

    def test_complete_function_case_4(self) -> None:
        assert complete('{"k1"') == '{"k1":null}'

    def test_complete_function_case_5(self) -> None:
        assert complete('{"k1\\""') == '{"k1\\"":null}'

    def test_complete_function_case_6(self) -> None:
        assert complete('{"k1":') == '{"k1":null}'

    def test_complete_function_case_7(self) -> None:
        assert complete('{"k1":"') == '{"k1":""}'

    def test_complete_function_case_8(self) -> None:
        assert complete('{"k1":"v\\"') == '{"k1":"v\\""}'

    def test_complete_function_case_9(self) -> None:
        assert complete('{"k1":"v\}') == '{"k1":"v\}"}'

    def test_complete_function_case_10(self) -> None:
        assert complete('{"k1":"v\[') == '{"k1":"v\["}'

    def test_complete_function_case_11(self) -> None:
        assert complete('{"k1":"v1"') == '{"k1":"v1"}'

    def test_complete_function_case_12(self) -> None:
        assert complete('{"k1":"v1"}') == '{"k1":"v1"}'

    def test_complete_function_case_13(self) -> None:
        assert complete('{"k1":"v1",') == '{"k1":"v1","":null}'

    def test_complete_function_case_14(self) -> None:
        assert complete('{"k1":"v1","') == '{"k1":"v1","":null}'

    def test_complete_function_case_15(self) -> None:
        assert complete('{"k1":"v1","k') == '{"k1":"v1","k":null}'

    def test_complete_function_case_16(self) -> None:
        assert complete('{"k1":"v1","k2"') == '{"k1":"v1","k2":null}'

    def test_complete_function_case_17(self) -> None:
        assert complete('{"k1":"v1","k2":') == '{"k1":"v1","k2":null}'

    def test_complete_function_case_18(self) -> None:
        assert complete('{"k1":"v1","k2":2') == '{"k1":"v1","k2":2}'

    def test_complete_function_case_19(self) -> None:
        assert complete('{"k1":"v1","k2":20.5') == '{"k1":"v1","k2":20.5}'

    def test_complete_function_case_20(self) -> None:
        assert complete('{"k1":"v1","k2":20.5}') == '{"k1":"v1","k2":20.5}'

    def test_complete_function_case_21(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,') == '{"k1":"v1","k2":20.5,"":null}'

    def test_complete_function_case_22(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[') == '{"k1":"v1","k2":20.5,"k3":[]}'

    def test_complete_function_case_23(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[1') == '{"k1":"v1","k2":20.5,"k3":[1]}'

    def test_complete_function_case_24(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[12') == '{"k1":"v1","k2":20.5,"k3":[12]}'

    def test_complete_function_case_25(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[12,') == '{"k1":"v1","k2":20.5,"k3":[12,null]}'

    def test_complete_function_case_26(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[12,3') == '{"k1":"v1","k2":20.5,"k3":[12,3]}'

    def test_complete_function_case_27(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[12,34') == '{"k1":"v1","k2":20.5,"k3":[12,34]}'

    def test_complete_function_case_28(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[12,34,"') == '{"k1":"v1","k2":20.5,"k3":[12,34,""]}'

    def test_complete_function_case_29(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[12,34,"56') == '{"k1":"v1","k2":20.5,"k3":[12,34,"56"]}'

    def test_complete_function_case_30(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[12,34,"56"') == '{"k1":"v1","k2":20.5,"k3":[12,34,"56"]}'

    def test_complete_function_case_31(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[12,34,"56",t') == '{"k1":"v1","k2":20.5,"k3":[12,34,"56",true]}'

    def test_complete_function_case_32(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[12,34,"56",true]') == '{"k1":"v1","k2":20.5,"k3":[12,34,"56",true]}'

    def test_complete_function_case_33(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[12,34,"56",true]}') == '{"k1":"v1","k2":20.5,"k3":[12,34,"56",true]}'

    def test_complete_function_case_34(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{') == '{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{}]}'

    def test_complete_function_case_35(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"') == '{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"":null}]}'

    def test_complete_function_case_36(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31') == '{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":null}]}'

    def test_complete_function_case_37(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31"') == '{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":null}]}'

    def test_complete_function_case_38(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":') == '{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":null}]}'

    def test_complete_function_case_39(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"') == '{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":""}]}'

    def test_complete_function_case_40(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"v31') == '{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"v31"}]}'

    def test_complete_function_case_41(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"v31"') == '{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"v31"}]}'

    def test_complete_function_case_42(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"v31","k32":f') == '{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"v31","k32":false}]}'

    def test_complete_function_case_43(self) -> None:
        assert complete('{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"v31","k32":false,"k33":n') == '{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"v31","k32":false,"k33":null}]}'


if __name__ == '__main__':
    unittest.main()
