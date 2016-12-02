# -*- coding: utf-8 -*-

from .baserequest import BaseRequest
from oandapyV20.types import Units, PriceValue
from oandapyV20.definitions.orders import (
    OrderType,
    OrderPositionFill,
    TimeInForce)


class StopOrderRequest(BaseRequest):
    """create a StopOrderRequest.

    StopOrderRequest is used to build the body for an StopOrder.
    The body can be used to pass to the OrderCreate endpoint.
    """

    def __init__(self,
                 instrument,
                 units,
                 price,
                 priceBound=None,
                 positionFill=OrderPositionFill.DEFAULT,
                 timeInForce=TimeInForce.GTC,
                 gtdTime=None,
                 clientExtensions=None,
                 takeProfitOnFill=None,
                 stopLossOnFill=None,
                 trailingStopLossOnFill=None,
                 tradeClientExtensions=None):
        """
        Instantiate a StopOrderRequest.

        Parameters
        ----------

        instrument : string (required)
            the instrument to create the order for

        units : integer (required)
            the number of units. If positive the order results in a LONG
            order. If negative the order results in a SHORT order

        price : float (required)
            the treshold price indicating the price to activate the order

        Example
        -------

        >>> import json
        >>> from oandapyV20 import API
        >>> import oandapyV20.endpoints.orders as orders
        >>> from oandapyV20.contrib.requests import StopOrderRequest
        >>>
        >>> accountID = "..."
        >>> client = API(access_token=...)
        >>> ordr = StopOrderRequest(instrument="EUR_USD",
        ...                         units=10000, price=1.07)
        >>> print(json.dumps(ordr.data, indent=4))
        {
            "order": {
                "type": "STOP",
                "price": "1.07000",
                "positionFill": "DEFAULT",
                "instrument": "EUR_USD",
                "timeInForce": "GTC",
                "units": "10000"
            }
        }
        >>> # now we have the order specification, create the order request
        >>> r = orders.OrderCreate(accountID, data=ordr.data)
        >>> # perform the request
        >>> rv = client.request(r)
        >>> print(json.dumps(rv, indent=4))
        >>> ...
        """
        super(StopOrderRequest, self).__init__()

        # by default for a STOP order
        self._data.update({"type": OrderType.STOP})

        # required
        self._data.update({"instrument": instrument})
        self._data.update({"units": Units(units).value})
        self._data.update({"price": PriceValue(price).value})

        # optional, but required if timeInForce.GTD
        self._data.update({"gtdTime": gtdTime})
        if timeInForce == TimeInForce.GTD and not gtdTime:
            raise ValueError("gtdTime missing")

        # optional
        self._data.update({"timeInForce": timeInForce})
        self._data.update({"priceBound": priceBound})
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
        return dict({"order": super(StopOrderRequest, self).data})
