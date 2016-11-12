import sys
import unittest
import re

try:
    from nose_parameterized import parameterized
except:
    print("*** Please install 'nose_parameterized' to run these tests ***")
    exit(0)


import oandapyV20.contrib.requests as req


def to_str(d):
    """convert dictionary values to str."""
    # All values back from OANDA are strings, so int's and floats
    # need to be converted to strings for comparing the response with
    # the requested values
    for k in d.keys():
        s = str(d[k])
        if re.match("^\d+$", s):         # int as a string
            d[k] = "{:d}".format(int(s))
        elif re.match("^\d+\.\d+$", s):  # float as a string, reformat
            d[k] = "{:.5f}".format(float(s))

    return d


class TestContribRequests(unittest.TestCase):
    """Tests regarding contrib requests."""

    @parameterized.expand([
       # MO
       (req.MarketOrderRequest,
           {"instrument": "EUR_USD",
            "units": 10000},
           {'timeInForce': 'FOK',
            'positionFill': 'DEFAULT',
            'type': 'MARKET'}),
       (req.MarketOrderRequest,
           {"instrument": "EUR_USD",
            "units": "10000"},
           {'timeInForce': 'FOK',
            'positionFill': 'DEFAULT',
            'type': 'MARKET'}),
       # LO
       (req.LimitOrderRequest,
           {"instrument": "EUR_USD",
            "units": 10000,
            "price": 1.08},
           {'timeInForce': 'GTC',
            'positionFill': 'DEFAULT',
            'type': 'LIMIT'
            }),
       (req.LimitOrderRequest,
           {"instrument": "EUR_USD",
            "units": "10000",
            "price": "1.08"},
           {'timeInForce': 'GTC',
            'positionFill': 'DEFAULT',
            'type': 'LIMIT'
            }),
       # MIT
       (req.MITOrderRequest,
           {"instrument": "EUR_USD",
            "units": 10000,
            "price": 1.08},
           {'timeInForce': 'GTC',
            'positionFill': 'DEFAULT',
            'type': 'MARKET_IF_TOUCHED'}
            ),
       # ... GTD, should raise a ValueError with missing date
       (req.MITOrderRequest,
           {"instrument": "EUR_USD",
            'timeInForce': 'GTD',
            "units": 10000,
            "price": 1.08},
           {'timeInForce': 'GTD',
            'positionFill': 'DEFAULT',
            'type': 'MARKET_IF_TOUCHED'},
            ValueError
            ),
       # TPO
       (req.TakeProfitOrderRequest,
           {"tradeID": "1234",
            "price": 1.22},
           {'timeInForce': 'GTC',
            'type': 'TAKE_PROFIT'}
            ),
       # ... GTD, should raise a ValueError with missing date
       (req.TakeProfitOrderRequest,
           {"tradeID": "1234",
            "timeInForce": "GTD",
            "price": 1.22},
           {'timeInForce': 'GTD',
            'type': 'TAKE_PROFIT'},
            ValueError
            ),
    ])
    def test__orders(self, cls, inpar, refpar, exc=None):
        reference = dict({"order": refpar})
        reference['order'].update(to_str(inpar))

        if not exc:
            r = cls(**inpar)
            self.assertTrue(r.data == reference)
        else:
            with self.assertRaises(exc) as err:
                r = cls(**inpar)


if __name__ == "__main__":

    unittest.main()
