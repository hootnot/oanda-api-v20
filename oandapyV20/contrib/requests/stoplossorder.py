# -*- coding: utf-8 -*-

from .baserequest import BaseRequest
from oandapyV20.types import TradeID, PriceValue
from oandapyV20.definitions.orders import TimeInForce, OrderType


class StopLossOrderRequest(BaseRequest):
    """create a StopLossOrderRequest.

    StopLossOrderRequest is used to build the body for a StopLossOrder.
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
        Instantiate a StopLossOrderRequest.

        Parameters
        ----------

        tradeID : string (required)
            the tradeID of an existing trade

        price : float (required)
            the treshold price indicating the price to close the order

        Example
        -------

        >>> import json
        >>> from oandapyV20 import API
        >>> import oandapyV20.endpoints.orders as orders
        >>> from oandapyV20.contrib.requests import StopLossOrderRequest
        >>>
        >>> accountID = "..."
        >>> client = API(access_token=...)
        >>> ordr = StopLossOrderRequest(tradeID="1234", price=1.07)
        >>> print(json.dumps(ordr.data, indent=4))
        {
            "order": {
                "type": "STOP_LOSS",
                "tradeID": "1234",
                "price": "1.07000",
                "timeInForce": "GTC",
            }
        }
        >>> # now we have the order specification, create the order request
        >>> r = orders.OrderCreate(accountID, data=ordr.data)
        >>> # perform the request
        >>> rv = client.request(r)
        >>> print(json.dumps(rv, indent=4))
        >>> ...
        """
        super(StopLossOrderRequest, self).__init__()

        # allowed: GTC/GFD/GTD
        if timeInForce not in [TimeInForce.GTC,
                               TimeInForce.GTD,
                               TimeInForce.GFD]:
            raise ValueError("timeInForce: {}".format(timeInForce))

        # by default for a STOP_LOSS order
        self._data.update({"type": OrderType.STOP_LOSS})

        # required
        self._data.update({"tradeID": TradeID(tradeID).value})
        self._data.update({"price": PriceValue(price).value})

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
        return dict({"order": super(StopLossOrderRequest, self).data})
