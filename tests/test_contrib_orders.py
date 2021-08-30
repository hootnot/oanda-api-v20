import unittest

try:
    from nose_parameterized import parameterized
except:
    print("*** Please install 'nose_parameterized' to run these tests ***")
    exit(0)


import oandapyV20.contrib.requests as req
import oandapyV20.definitions.orders as OD
import oandapyV20.types as types


class TestContribRequests(unittest.TestCase):
    """Tests regarding contrib requests.

    The reference is created using the second dict parameter. The
    first dict parameter is merge with this, but only for the keys
    that do NOT exist. That allows us to override parameters.
    The result should reflect the data constructed by the class

    """

    @parameterized.expand([
       # MO
       (req.MarketOrderRequest,
           {"instrument": "EUR_USD",
            "units": 10000},         # integer!
           {'timeInForce': 'FOK',    # the default
            'units': '10000',        # override, should be the str equiv.
            'positionFill': 'DEFAULT',
            'type': 'MARKET'}
        ),
       (req.MarketOrderRequest,
           {"instrument": "EUR_USD",
            "priceBound": 12345,     # integer
            "units": "10000"},
           {'timeInForce': 'FOK',
            "priceBound": types.PriceValue(12345).value,
            'positionFill': 'DEFAULT',
            'type': 'MARKET'}
        ),
       (req.MarketOrderRequest,
           {"instrument": "EUR_USD",
            'timeInForce': 'GFD',     # should result in a ValueError
            "units": "10000"},
           {'positionFill': 'DEFAULT',
            'type': 'MARKET'},
           ValueError
        ),
       (req.MarketOrderRequest,
           {"instrument": "EUR_USD",
            'timeInForce': 'FOK',
            'positionFill': 'WRONG',
            "units": "10000"},
           {'positionFill': 'WRONG',
            'type': 'MARKET'},
           ValueError
        ),
       # LO
       (req.LimitOrderRequest,
           {"instrument": "EUR_USD",
            "units": 10000,     # integer
            "price": 1.08},
           {'timeInForce': 'GTC',
            "price": '1.08000',
            'positionFill': 'DEFAULT',
            'type': 'LIMIT'
            }
        ),
       (req.LimitOrderRequest,
           {"instrument": "EUR_USD",
            "units": "10000",    # string
            "price": "1.08"},
           {'timeInForce': 'GTC',
            "price": '1.08000',
            'positionFill': 'DEFAULT',
            'type': 'LIMIT'
            }
        ),
       # ... GTD, should raise a ValueError with missing date
       (req.LimitOrderRequest,
           {"instrument": "EUR_USD",
            'timeInForce': 'GTD',
            "units": 10000,
            "price": 1.08},
           {'timeInForce': 'GTD',
            "price": '1.08000',
            'positionFill': 'DEFAULT',
            'type': 'LIMIT'},
           ValueError
        ),
       # MIT
       (req.MITOrderRequest,
           {"instrument": "EUR_USD",
            "units": 10000,
            "price": 1.08},
           {'timeInForce': 'GTC',
            "price": '1.08000',
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
            "price": '1.08000',
            'positionFill': 'DEFAULT',
            'type': 'MARKET_IF_TOUCHED'},
           ValueError
        ),
       # ... FOK, should raise a ValueError (not allowed)
       (req.MITOrderRequest,
           {"instrument": "EUR_USD",
            'timeInForce': 'FOK',
            "units": 10000,
            "price": 1.08},
           {'timeInForce': 'FOK',
            "price": '1.08000',
            'positionFill': 'DEFAULT',
            'type': 'MARKET_IF_TOUCHED'},
           ValueError
        ),
       # TPO
       (req.TakeProfitOrderRequest,
           {"tradeID": "1234",
            "price": 1.22},
           {'timeInForce': 'GTC',
            "price": '1.22000',
            'type': 'TAKE_PROFIT'}
        ),
       # ... GTD, should raise a ValueError with missing date
       (req.TakeProfitOrderRequest,
           {"tradeID": "1234",
            "timeInForce": "GTD",
            "price": 1.22},
           {'timeInForce': 'GTD',
            "price": '1.22000',
            'type': 'TAKE_PROFIT'},
           ValueError
        ),
       # ... FOK, should raise a ValueError (not allowed)
       (req.TakeProfitOrderRequest,
           {"tradeID": "1234",
            "timeInForce": "FOK",
            "price": 1.22},
           {'timeInForce': 'FOK',
            "price": '1.22000',
            'type': 'TAKE_PROFIT'},
           ValueError
        ),
       # SLO
       (req.StopLossOrderRequest,
           {"tradeID": "1234",
            "price": 1.07},
           {'timeInForce': 'GTC',
            'type': 'STOP_LOSS',
            'price': '1.07000'}
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
       # SLO: distance instead of price
       (req.StopLossOrderRequest,
           {"tradeID": "1234",
            "timeInForce": "GTC",
            "distance": 50},
           {'timeInForce': 'GTC',
            'type': 'STOP_LOSS',
            'distance': '50'},
        ),
       # ... no price and no distance, should raise a ValueError
       (req.StopLossOrderRequest,
           {"tradeID": "1234"},
           {'timeInForce': 'GTC',
            'type': 'STOP_LOSS'},
           ValueError
        ),
       # ... price and distance, should raise a ValueError
       (req.StopLossOrderRequest,
           {"tradeID": "1234",
            "price": 1.10,
            "distance": 40},
           {'timeInForce': 'GTC',
            'price': 1.10,
            'distance': 40,
            'type': 'STOP_LOSS'},
           ValueError
        ),
       # ... FOK, should raise a ValueError
       (req.StopLossOrderRequest,
           {"tradeID": "1234",
            "timeInForce": "FOK",
            "price": 1.07},
           {'timeInForce': 'FOK',
            'type': 'STOP_LOSS'},
           ValueError
        ),
       # TSLO
       (req.TrailingStopLossOrderRequest,
           {"tradeID": "1234",
            "distance": 20.5},
           {'timeInForce': 'GTC',
            "distance": '20.50000',
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
       # ... FOK, should raise a ValueError (not allowed)
       (req.TrailingStopLossOrderRequest,
           {"tradeID": "1234",
            "timeInForce": "FOK",
            "distance": 20.5},
           {'timeInForce': 'FOK',
            "distance": "20.50000",
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
            "price": "1.07000",
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
            "price": "1.07000",
            'type': 'STOP'},
           ValueError
        ),
    ])
    def test__orders(self, cls, inpar, refpar, exc=None):
        reference = dict({"order": refpar})

        # update in reference all keys if they do not exists
        for k in inpar.keys():
            if k not in reference['order']:
                reference['order'][k] = str(inpar[k])

        if not exc:
            r = cls(**inpar)
            print("*************")
            print(r.data)
            print(refpar)
            self.assertTrue(r.data == reference)
        else:
            with self.assertRaises(exc):
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
       # client ext
       (req.PositionCloseRequest,
           {"longUnits": 10000,
            "shortUnits": 2000,
            "shortClientExtensions": {"key": "val"}
            },
           {"longUnits": "10000",
            "shortUnits": "2000",
            "shortClientExtensions": {"key": "val"}
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
       # ... distance instead of price
       (req.StopLossDetails,
           {"distance": 40},
           {'timeInForce': 'GTC',
            'distance': '40.00000'}
        ),
       # .. raises ValueError because price and distance
       (req.StopLossDetails,
           {"distance": 40,
            "price": 1.10},
           {'timeInForce': 'GTC',
            'price': '1.10000',
            'distance': '40.00000'},
           ValueError
        ),
       # .. raises ValueError because no price and no distance
       (req.StopLossDetails,
           {"timeInForce": OD.TimeInForce.GTC},
           {'timeInForce': 'GTC'},
           ValueError
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
       # ClientExtensions
       (req.ClientExtensions,
           {"clientID": "myID"},
           {"id": "myID"},
        ),
       (req.ClientExtensions,
           {"clientTag": "myTag"},
           {"tag": "myTag"},
        ),
       (req.ClientExtensions,
           {"clientComment": "myComment"},
           {"comment": "myComment"},
        ),
       # .. raises ValueError because no values were set
       (req.ClientExtensions,
           {},
           {},
           ValueError
        ),
    ])
    def test__anonymous_body(self, cls, inpar, refpar, exc=None):

        if not exc:
            r = cls(**inpar) if inpar else cls()
            print("*************")
            print(r.data)
            print(refpar)
            self.assertTrue(r.data == refpar)
        else:
            with self.assertRaises(exc):
                r = cls(**inpar)


if __name__ == "__main__":

    unittest.main()
