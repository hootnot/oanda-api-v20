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
    for k in d.keys():
        if isinstance(d[k], int):
            d[k] = str(d[k])
        elif isinstance(d[k], float):
            d[k] = "{:.5f}".format(d[k])
        elif re.match("^\d+$", d[k]):
            d[k] = str(d[k])
        elif re.match("^\d+\.\d+$", d[k]):
            d[k] = "{:.5f}".format(float(d[k]))

    return d


class TestContribRequests(unittest.TestCase):
    """Tests regarding contrib requests."""

    @parameterized.expand([
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
            })
    ])
    def test__orders(self, cls, inpar, refpar):
        reference = dict({"order": refpar})
        reference['order'].update(to_str(inpar))

        r = cls(**inpar)
        self.assertTrue(r.data == reference)


if __name__ == "__main__":

    unittest.main()
