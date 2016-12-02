# -*- coding: utf-8 -*-

from .baserequest import BaseRequest
from oandapyV20.types import TradeID, PriceValue
from oandapyV20.definitions.orders import TimeInForce, OrderType


class TrailingStopLossOrderRequest(BaseRequest):
    """create a TrailingStopLossOrderRequest.

    TrailingStopLossOrderRequest is used to build the body for a
    TrailingStopLossOrder. The body can be used to pass to the
    OrderCreate endpoint.
    """

    def __init__(self,
                 tradeID,
                 distance,
                 clientTradeID=None,
                 timeInForce=TimeInForce.GTC,
                 gtdTime=None,
                 clientExtensions=None):
        """
        Instantiate a TrailingStopLossOrderRequest.

        Parameters
        ----------

        tradeID : string (required)
            the tradeID of an existing trade

        distance : float (required)
            the price distance

        Example
        -------

        >>> import json
        >>> from oandapyV20 import API
        >>> import oandapyV20.endpoints.orders as orders
        >>> from oandapyV20.contrib.requests import TrailingStopLossOrderRequest
        >>>
        >>> accountID = "..."
        >>> client = API(access_token=...)
        >>> ordr = TrailingStopLossOrderRequest(tradeID="1234", distance=20)
        >>> print(json.dumps(ordr.data, indent=4))
        {
            "order": {
                "type": "TRAILING_STOP_LOSS",
                "tradeID": "1234",
                "timeInForce": "GTC",
                "distance": "20.00000"
            }
        }
        >>> # now we have the order specification, create the order request
        >>> r = orders.OrderCreate(accountID, data=ordr.data)
        >>> # perform the request
        >>> rv = client.request(r)
        >>> print(json.dumps(rv, indent=4))
        >>> ...
        """
        super(TrailingStopLossOrderRequest, self).__init__()

        # allowed: GTC/GFD/GTD
        if timeInForce not in [TimeInForce.GTC,
                               TimeInForce.GTD,
                               TimeInForce.GFD]:
            raise ValueError("timeInForce: {}".format(timeInForce))

        # by default for a TRAILING_STOP_LOSS order
        self._data.update({"type": OrderType.TRAILING_STOP_LOSS})

        # required
        self._data.update({"tradeID": TradeID(tradeID).value})
        self._data.update({"distance": PriceValue(distance).value})

        # optional
        self._data.update({"clientExtensions": clientExtensions})
        self._data.update({"timeInForce": timeInForce})
        self._data.update({"gtdTime": gtdTime})

        if timeInForce == TimeInForce.GTD and not gtdTime:
            raise ValueError("gtdTime missing")

    @property
    def data(self):
        """data property.

        return the JSON body.
        """
        return dict({"order": super(TrailingStopLossOrderRequest, self).data})
