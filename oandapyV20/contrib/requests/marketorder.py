# -*- coding: utf-8 -*-

from .baserequest import BaseRequest
from oandapyV20.types import Units, PriceValue
from oandapyV20.definitions.orders import (
    OrderType,
    TimeInForce,
    OrderPositionFill)


class MarketOrderRequest(BaseRequest):
    """create a MarketOrderRequest.

    MarketOrderRequest is used to build the body for a MarketOrder.
    The body can be used to pass to the OrderCreate endpoint.
    """

    def __init__(self,
                 instrument,
                 units,
                 priceBound=None,
                 positionFill=OrderPositionFill.DEFAULT,
                 clientExtensions=None,
                 takeProfitOnFill=None,
                 timeInForce=TimeInForce.FOK,
                 stopLossOnFill=None,
                 trailingStopLossOnFill=None,
                 tradeClientExtensions=None):
        """
        Instantiate a MarketOrderRequest.

        Parameters
        ----------

        instrument : string (required)
            the instrument to create the order for

        units: integer (required)
            the number of units. If positive the order results in a LONG
            order. If negative the order results in a SHORT order


        Example
        -------

        >>> import json
        >>> from oandapyV20 import API
        >>> import oandapyV20.endpoints.orders as orders
        >>> from oandapyV20.contrib.requests import MarketOrderRequest
        >>>
        >>> accountID = "..."
        >>> client = API(access_token=...)
        >>> mo = MarketOrderRequest(instrument="EUR_USD", units=10000)
        >>> print(json.dumps(mo.data, indent=4))
        {
            "order": {
                "type": "MARKET",
                "positionFill": "DEFAULT",
                "instrument": "EUR_USD",
                "timeInForce": "FOK",
                "units": "10000"
            }
        }
        >>> # now we have the order specification, create the order request
        >>> r = orders.OrderCreate(accountID, data=mo.data)
        >>> # perform the request
        >>> rv = client.request(r)
        >>> print(rv)
        >>> print(json.dumps(rv, indent=4))
        {
            "orderFillTransaction": {
                "reason": "MARKET_ORDER",
                "pl": "0.0000",
                "accountBalance": "97864.8813",
                "units": "10000",
                "instrument": "EUR_USD",
                "accountID": "101-004-1435156-001",
                "time": "2016-11-11T19:59:43.253587917Z",
                "type": "ORDER_FILL",
                "id": "2504",
                "financing": "0.0000",
                "tradeOpened": {
                    "tradeID": "2504",
                    "units": "10000"
                },
                "orderID": "2503",
                "userID": 1435156,
                "batchID": "2503",
                "price": "1.08463"
            },
            "lastTransactionID": "2504",
            "relatedTransactionIDs": [
                "2503",
                "2504"
            ],
            "orderCreateTransaction": {
                "type": "MARKET_ORDER",
                "reason": "CLIENT_ORDER",
                "id": "2503",
                "timeInForce": "FOK",
                "units": "10000",
                "time": "2016-11-11T19:59:43.253587917Z",
                "positionFill": "DEFAULT",
                "accountID": "101-004-1435156-001",
                "instrument": "EUR_USD",
                "batchID": "2503",
                "userID": 1435156
            }
        }
        >>>
        """
        super(MarketOrderRequest, self).__init__()

        # allowed: FOK/IOC
        if timeInForce not in [TimeInForce.FOK,
                               TimeInForce.IOC]:
            raise ValueError("timeInForce: {}".format(timeInForce))

        # by default for a MARKET order
        self._data.update({"type": OrderType.MARKET})
        self._data.update({"timeInForce": timeInForce})

        # required
        self._data.update({"instrument": instrument})
        self._data.update({"units": Units(units).value})

        # optional
        if priceBound:
            self._data.update({"priceBound": PriceValue(priceBound).value})

        if not hasattr(OrderPositionFill, positionFill):
            raise ValueError("positionFill {}".format(positionFill))

        self._data.update({"positionFill": positionFill})

        self._data.update({"clientExtensions": clientExtensions})
        self._data.update({"takeProfitOnFill": takeProfitOnFill})
        self._data.update({"stopLossOnFill": stopLossOnFill})
        self._data.update({"trailingStopLossOnFill": trailingStopLossOnFill})
        self._data.update({"tradeClientExtensions": tradeClientExtensions})

    @property
    def data(self):
        """data property.

        return the JSON body.
        """
        return dict({"order": super(MarketOrderRequest, self).data})
