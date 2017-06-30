import unittest

try:
    from nose_parameterized import parameterized
except ImportError:
    print("*** Please install 'nose_parameterized' to run these tests ***")
    exit(0)


import oandapyV20.contrib.generic as gen


class TestContribGeneric(unittest.TestCase):
    """Tests regarding contrib generic."""

    @parameterized.expand([
       (gen.granularity_to_time, "M1", 1*60),
       (gen.granularity_to_time, "M2", 2*60),
       (gen.granularity_to_time, "M5", 5*60),
       (gen.granularity_to_time, "M15", 15*60),
       (gen.granularity_to_time, "H1", 3600),
       (gen.granularity_to_time, "H4", 4*3600),
       (gen.granularity_to_time, "D", 86400),
       (gen.granularity_to_time, "D1", 86400),
       (gen.granularity_to_time, "K1", 86400, ValueError),
    ])
    def test__granularity_to_time(self, meth, granularity, refval, exc=None):
        """granularity_to_time."""
        if not exc:
            # run the factory
            r = meth(granularity)
            self.assertTrue(r == refval)

        else:
            with self.assertRaises(exc) as err:
                r = meth(granularity)


if __name__ == "__main__":

    unittest.main()
