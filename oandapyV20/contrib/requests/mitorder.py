# -*- coding: utf-8 -*-

from .baserequest import BaseRequest
from oandapyV20.types import Units, PriceValue
from oandapyV20.definitions.orders import (
    OrderType,
    OrderPositionFill,
    TimeInForce)


class MITOrderRequest(BaseRequest):
    """create a MarketIfTouched OrderRequest.

    MITOrderRequest is used to build the body for a MITOrder.
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
        Instantiate an MITOrderRequest.

        Parameters
        ----------

        instrument : string (required)
            the instrument to create the order for

        units: integer (required)
            the number of units. If positive the order results in a LONG
            order. If negative the order results in a SHORT order

        price: float (required)
            the price indicating the limit.

        Example
        -------

        >>> import json
        >>> from oandapyV20 import API
        >>> import oandapyV20.endpoints.orders as orders
        >>> from oandapyV20.contrib.requests import MITOrderRequest
        >>>
        >>> accountID = "..."
        >>> client = API(access_token=...)
        >>> ordr = MITOrderRequest(instrument="EUR_USD",
        ...                      units=10000, price=1.08)
        >>> print(json.dumps(ordr.data, indent=4))
        {
            "order": {
                "timeInForce": "GTC",
                "instrument": "EUR_USD",
                "units": "10000",
                "price": "1.08000",
                "type": "MARKET_IF_TOUCHED",
                "positionFill": "DEFAULT"
            }
        }
        >>> r = orders.OrderCreate(accountID, data=ordr.data)
        >>> rv = client.request(r)
        >>> ...
        """
        super(MITOrderRequest, self).__init__()

        # allowed: GTC/GFD/GTD
        if timeInForce not in [TimeInForce.GTC,
                               TimeInForce.GTD,
                               TimeInForce.GFD]:
            raise ValueError("timeInForce: {}".format(timeInForce))

        # by default for a MARKET_IF_TOUCHED order
        self._data.update({"type": OrderType.MARKET_IF_TOUCHED})

        # required
        self._data.update({"timeInForce": timeInForce})
        self._data.update({"instrument": instrument})
        self._data.update({"units": Units(units).value})
        self._data.update({"price": PriceValue(price).value})

        # optional, but required if
        self._data.update({"gtdTime": gtdTime})
        if timeInForce == TimeInForce.GTD and not gtdTime:
            raise ValueError("gtdTime missing")

        # optional
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

        return the JSON order body
        """
        return dict({"order": super(MITOrderRequest, self).data})
