import sys
import unittest
import re

try:
    from nose_parameterized import parameterized
except:
    print("*** Please install 'nose_parameterized' to run these tests ***")
    exit(0)


import oandapyV20.contrib.requests as req
import oandapyV20.definitions.orders as OD


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
            'type': 'MARKET'}
        ),
       (req.MarketOrderRequest,
           {"instrument": "EUR_USD",
            "units": "10000"},
           {'timeInForce': 'FOK',
            'positionFill': 'DEFAULT',
            'type': 'MARKET'}
        ),
       # LO
       (req.LimitOrderRequest,
           {"instrument": "EUR_USD",
            "units": 10000,
            "price": 1.08},
           {'timeInForce': 'GTC',
            'positionFill': 'DEFAULT',
            'type': 'LIMIT'
            }
        ),
       (req.LimitOrderRequest,
           {"instrument": "EUR_USD",
            "units": "10000",
            "price": "1.08"},
           {'timeInForce': 'GTC',
            'positionFill': 'DEFAULT',
            'type': 'LIMIT'
            }
        ),
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
       # SLO
       (req.StopLossOrderRequest,
           {"tradeID": "1234",
            "price": 1.07},
           {'timeInForce': 'GTC',
            'type': 'STOP_LOSS'}
        ),
       # ... GTD, should raise a ValueError with missing date
       (req.StopLossOrderRequest,
           {"tradeID": "1234",
            "timeInForce": "GTD",
            "price": 1.07},
           {'timeInForce': 'GTD',
            'type': 'STOP_LOSS'},
           ValueError
        ),
       # TSLO
       (req.TrailingStopLossOrderRequest,
           {"tradeID": "1234",
            "distance": 20.5},
           {'timeInForce': 'GTC',
            'type': 'TRAILING_STOP_LOSS'}
        ),
       # ... GTD, should raise a ValueError with missing date
       (req.TrailingStopLossOrderRequest,
           {"tradeID": "1234",
            "timeInForce": "GTD",
            "distance": 20.5},
           {'timeInForce': 'GTD',
            'type': 'TRAILING_STOP_LOSS'},
           ValueError
        ),
       # SO
       (req.StopOrderRequest,
           {"instrument": "EUR_USD",
            "units": 10000,
            "price": 1.07},
           {'timeInForce': 'GTC',
            'positionFill': 'DEFAULT',
            'type': 'STOP'}
        ),
       # ... GTD, should raise a ValueError with missing date
       (req.StopOrderRequest,
           {"instrument": "EUR_USD",
            "units": 10000,
            "timeInForce": "GTD",
            "price": 1.07},
           {'timeInForce': 'GTD',
            'positionFill': 'DEFAULT',
            'type': 'STOP'},
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

    @parameterized.expand([
       # regular
       (req.PositionCloseRequest,
           {"longUnits": 10000,
            "shortUnits": 2000},
           {"longUnits": "10000",
            "shortUnits": "2000"},
        ),
       # nothing
       (req.PositionCloseRequest,
           {},
           {},
           ValueError
        ),
       # client ext
       (req.PositionCloseRequest,
           {"longUnits": 10000,
            "shortUnits": 2000,
            "longClientExtensions": {"key": "val"}
            },
           {"longUnits": "10000",
            "shortUnits": "2000",
            "longClientExtensions": {"key": "val"}
            },
        ),
       # regular
       (req.TradeCloseRequest,
           {"units": 10000},
           {"units": "10000"}
        ),
       # default
       (req.TradeCloseRequest,
           {},
           {"units": "ALL"}
        ),
       # TakeProfitDetails
       (req.TakeProfitDetails,
           {"price": 1.10},
           {'timeInForce': 'GTC',
            'price': '1.10000'}
        ),
       # .. raises ValueError because GTD required gtdTime
       (req.TakeProfitDetails,
           {"price": 1.10,
            "timeInForce": OD.TimeInForce.GTD},
           {'timeInForce': 'GTD',
            'price': '1.10000'},
           ValueError
        ),
       # .. raises ValueError because timeInForce must be GTC/GTD/GFD
       (req.TakeProfitDetails,
           {"price": 1.10,
            "timeInForce": OD.TimeInForce.FOK},
           {'timeInForce': 'FOK',
            'price': '1.10000'},
           ValueError
        ),
       # StopLossDetails
       (req.StopLossDetails,
           {"price": 1.10},
           {'timeInForce': 'GTC',
            'price': '1.10000'}
        ),
       # .. raises ValueError because GTD required gtdTime
       (req.StopLossDetails,
           {"price": 1.10,
            "timeInForce": OD.TimeInForce.GTD},
           {'timeInForce': 'GTD',
            'price': '1.10000'},
           ValueError
        ),
       # .. raises ValueError because timeInForce must be GTC/GTD/GFD
       (req.StopLossDetails,
           {"price": 1.10,
            "timeInForce": OD.TimeInForce.FOK},
           {'timeInForce': 'FOK',
            'price': '1.10000'},
           ValueError
        ),
       # TrailingStopLossDetails
       (req.TrailingStopLossDetails,
           {"distance": 25},
           {'timeInForce': 'GTC',
            'distance': '25.00000'}
        ),
       # .. raises ValueError because GTD required gtdTime
       (req.TrailingStopLossDetails,
           {"distance": 100,
            "timeInForce": OD.TimeInForce.GTD},
           {'timeInForce': 'GTD',
            'distance': '100.00000'},
           ValueError
        ),
       # .. raises ValueError because timeInForce must be GTC/GTD/GFD
       (req.TrailingStopLossDetails,
           {"distance": 100,
            "timeInForce": OD.TimeInForce.FOK},
           {'timeInForce': 'FOK',
            'distance': '100.00000'},
           ValueError
        ),
    ])
    def test__anonymous_body(self, cls, inpar, refpar, exc=None):
        reference = to_str(refpar)

        if not exc:
            r = cls(**inpar) if inpar else cls()
            self.assertTrue(r.data == reference)
        else:
            with self.assertRaises(exc) as err:
                r = cls(**inpar)


if __name__ == "__main__":

    unittest.main()
