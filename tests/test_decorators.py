import unittest
from oandapyV20.endpoints.decorators import extendargs, abstractclass
from abc import ABCMeta, abstractmethod
import six


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


    def test__abstractclass(self):

        @six.add_metaclass(ABCMeta)
        class Something(object):

            @abstractmethod
            def __init__(self, x=10):
                 self.x = x

        @abstractclass
        class SomethingElse(Something):
            # derived classes from this class make use
            # of this class __init__
            # since this __init__ overrides the parent's
            # @abstractmethod instances could be created,
            # by making the class abstract with @abstractclass
            # this can't be done, derived classes can
            # ... that is the goal

            def __init__(self, x=10, y=20):
                super(SomethingElse, self).__init__(x)
                self.y = y

        class ABCDerived(SomethingElse):
            pass

        with self.assertRaises(TypeError) as errAbstract:
            smth = Something(x=20)
        with self.assertRaises(TypeError) as errAbstractBase: 
            smthelse = SomethingElse(x=20, y=30)

        x = 20
        y = 30
        abcDerived = ABCDerived(x, y)
        self.assertEqual(abcDerived.x + abcDerived.y, x+y)



if __name__ == "__main__":

    unittest.main()
