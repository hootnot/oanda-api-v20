import unittest
from oandapyV20.endpoints.decorators import extendargs


class TestDecorators(unittest.TestCase):
    """Tests decorators ."""

    def test__extendargs(self):

        class Something(object):
            def __init__(self, x=10):
                self.x = x

        @extendargs("y")
        class SomethingExtra(Something):

            def add(self):
                return self.x + self.y

        tst = SomethingExtra(x=10, y=20)
        self.assertEqual(tst.add(), 30)


if __name__ == "__main__":

    unittest.main()
