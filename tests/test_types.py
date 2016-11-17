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
       # AccountID
       (tp.AccountID,
           {"accountID": "001-011-5838423-001"},
           {"siteID": "001",
            "divisionID": "011",
            "userID": "5838423",
            "accountNumber": "001"}
        ),
       (tp.AccountID,
           {"accountID": "0010115838423001"},
           {"siteID": "001",
            "divisionID": "011",
            "userID": "5838423",
            "accountNumber": "001"},
        ValueError
        ),
       # OrderID
       (tp.OrderID,
           {"orderID": "1234"},
           "1234",
        ),
       (tp.OrderID,
           {"orderID": 1234},
           "1234",
        ),
       (tp.OrderID,
           {"orderID": -1234},
           "1234",
        ValueError
        ),
       # TradeID
       (tp.TradeID,
           {"tradeID": "1234"},
           "1234",
        ),
       (tp.TradeID,
           {"tradeID": 1234},
           "1234",
        ),
       (tp.TradeID,
           {"tradeID": -1234},
           "1234",
        ValueError
        ),
       # AccountUnits
       (tp.AccountUnits,
           {"units": 1234},
           "1234.00000",
        ),
       (tp.AccountUnits,
           {"units": "1234"},
           "1234.00000",
        ),
       # PriceValue
       (tp.PriceValue,
           {"priceValue": 1234},
           "1234.00000",
        ),
       (tp.PriceValue,
           {"priceValue": "1234"},
           "1234.00000",
        ),
       # Units
       (tp.Units,
           {"units": 1234},
           "1234",
        ),
       (tp.Units,
           {"units": "-1234"},
           "-1234",
        ),
       # ClientID
       (tp.ClientID,
           {"clientID": "my valid custom id"},
           "my valid custom id"
        ),
       (tp.ClientID,
           {"clientID": "to long"+"x"*125},
           "to long"+"x"*125,
        ValueError
        ),
       # ClientTag
       (tp.ClientTag,
           {"clientTag": "my valid custom tag"},
           "my valid custom tag"
        ),
       (tp.ClientTag,
           {"clientTag": "to long"+"x"*125},
           "to long"+"x"*125,
        ValueError
        ),
       # ClientComment
       (tp.ClientComment,
           {"clientComment": "my valid custom comment"},
           "my valid custom comment"
        ),
       (tp.ClientComment,
           {"clientComment": "to long"+"x"*125},
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
