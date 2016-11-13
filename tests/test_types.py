import sys
import unittest

try:
    from nose_parameterized import parameterized
except:
    print("*** Please install 'nose_parameterized' to run these tests ***")
    exit(0)


import oandapyV20.types as tp


class TestTypes(unittest.TestCase):
    """Tests types."""

    @parameterized.expand([
       # OrderID
       (tp.OrderID,
           {"v": "1234"},
           "1234",
        ),
       (tp.OrderID,
           {"v": 1234},
           "1234",
        ),
       (tp.OrderID,
           {"v": -1234},
           "1234",
        ValueError
        ),
       # OrderID
       (tp.TradeID,
           {"v": "1234"},
           "1234",
        ),
       (tp.TradeID,
           {"v": 1234},
           "1234",
        ),
       (tp.TradeID,
           {"v": -1234},
           "1234",
        ValueError
        ),
       # AccountUnits
       (tp.AccountUnits,
           {"v": 1234},
           "1234.00000",
        ),
       (tp.AccountUnits,
           {"v": "1234"},
           "1234.00000",
        ),
       # PriceValue
       (tp.PriceValue,
           {"v": 1234},
           "1234.00000",
        ),
       (tp.PriceValue,
           {"v": "1234"},
           "1234.00000",
        ),
       # Units
       (tp.Units,
           {"v": 1234},
           "1234",
        ),
       (tp.Units,
           {"v": "-1234"},
           "-1234",
        ),
       # ClientID
       (tp.ClientID,
           {"v": "my valid custom id"},
           "my valid custom id"
        ),
       (tp.ClientID,
           {"v": "to long"+"x"*125},
           "to long"+"x"*125,
        ValueError
        ),
       # OrderIdentifier
       (tp.OrderIdentifier,
           {"orderID": 1234,
            "clientID": "my valid custom id"},
           {"orderID": "1234",
            "clientOrderID": "my valid custom id"},
        ),
       (tp.OrderIdentifier,
           {"orderID": "X1234",
            "clientID": "my valid custom id"},
           {"orderID": "1234",
            "clientOrderID": "my valid custom id"},
        ValueError
        ),
       (tp.OrderIdentifier,
           {"orderID": "1234",
            "clientID": "to long"+"x"*125},
           {"orderID": "1234",
            "clientOrderID": "to long"+"x"*125},
        ValueError
        ),
       # OrderSpecifier
       (tp.OrderSpecifier,
           {"specifier": 1234},
           "1234",
        ),
       (tp.OrderSpecifier,
           {"specifier": "1234"},
           "1234",
        ),
       (tp.OrderSpecifier,
           {"specifier": "@"},
           "@",
        ValueError
        ),
       (tp.OrderSpecifier,
           {"specifier": "@my valid custom id"},
           "my valid custom id",
        ),
       (tp.OrderSpecifier,
           {"specifier": "@"+"to long"+"x"*125},
           "to long"+"x"*125,
        ValueError
        ),
    ])
    def test__types(self, cls, inpar, reference, exc=None):

        if not exc:
            r = cls(**inpar)
            self.assertTrue(r.value == reference)
        else:
            with self.assertRaises(exc) as err:
                r = cls(**inpar)


if __name__ == "__main__":

    unittest.main()
