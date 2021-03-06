from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class BinTests(TranspileTestCase):
    def test_int_but_no_index(self):
        self.assertCodeExecution("""
            class IntLike:
                def __init__(self, val):
                    self.val = val
                def __int__(self):
                    return self.val

            x = IntLike(5)
            try:
                print(bin(x))
            except TypeError as err:
                print(err)
            """)


class BuiltinBinFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["bin"]

    not_implemented = [
        'test_class',
        'test_frozenset',
    ]
