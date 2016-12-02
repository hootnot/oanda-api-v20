# -*- coding: utf-8 -*-

from .baserequest import BaseRequest
from oandapyV20.types import TradeID, PriceValue
from oandapyV20.definitions.orders import TimeInForce, OrderType


class TakeProfitOrderRequest(BaseRequest):
    """create a TakeProfit OrderRequest.

    TakeProfitOrderRequest is used to build the body for a TakeProfitOrder.
    The body can be used to pass to the OrderCreate endpoint.
    """

    def __init__(self,
                 tradeID,
                 price,
                 clientTradeID=None,
                 timeInForce=TimeInForce.GTC,
                 gtdTime=None,
                 clientExtensions=None):
        """
        Instantiate a TakeProfitOrderRequest.

        Parameters
        ----------

        tradeID : string (required)
            the tradeID of an existing trade

        price: float (required)
            the price indicating the target price to close the order.

        Example
        -------

        >>> import json
        >>> from oandapyV20 import API
        >>> import oandapyV20.endpoints.orders as orders
        >>> from oandapyV20.contrib.requests import TakeProfitOrderRequest
        >>>
        >>> accountID = "..."
        >>> client = API(access_token=...)
        >>> ordr = TakeProfitOrderRequest(tradeID="1234",
        >>>                               price=1.22)
        >>> print(json.dumps(ordr.data, indent=4))
        {
            "order": {
                "timeInForce": "GTC",
                "price": "1.22000",
                "type": "TAKE_PROFIT",
                "tradeID": "1234"
            }
        }
        >>> r = orders.OrderCreate(accountID, data=ordr.data)
        >>> rv = client.request(r)
        >>> ...
        """
        super(TakeProfitOrderRequest, self).__init__()

        # allowed: GTC/GFD/GTD
        if timeInForce not in [TimeInForce.GTC,
                               TimeInForce.GTD,
                               TimeInForce.GFD]:
            raise ValueError("timeInForce: {}".format(timeInForce))

        # by default for a TAKE_PROFIT order
        self._data.update({"type": OrderType.TAKE_PROFIT})
        self._data.update({"timeInForce": timeInForce})

        # required
        self._data.update({"tradeID": TradeID(tradeID).value})
        self._data.update({"price": PriceValue(price).value})

        # optional, but required if
        self._data.update({"gtdTime": gtdTime})
        if timeInForce == TimeInForce.GTD and not gtdTime:
            raise ValueError("gtdTime missing")

        # optional
        self._data.update({"clientExtensions": clientExtensions})

    @property
    def data(self):
        """data property.

        return the JSON order body
        """
        return dict({"order": super(TakeProfitOrderRequest, self).data})
