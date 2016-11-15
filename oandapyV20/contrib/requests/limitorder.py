# -*- coding: utf-8 -*-

from .baserequest import BaseRequest
from oandapyV20.types import Units, PriceValue
import oandapyV20.definitions.orders as OD


class LimitOrderRequest(BaseRequest):
    """create a LimitOrderRequest.

    LimitOrderRequest is used to build the body for a LimitOrder.
    The body can be used to pass to the OrderCreate endpoint.
    """

    def __init__(self,
                 instrument,
                 units,
                 price,
                 positionFill=OD.OrderPositionFill.DEFAULT,
                 clientExtensions=None,
                 takeProfitOnFill=None,
                 stopLossOnFill=None,
                 trailingStopLossOnFill=None,
                 tradeClientExtensions=None):
        """
        Instantiate a LimitOrderRequest.

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
            >>> from oandapyV20.contrib.requests import LimitOrderRequest
            >>>
            >>> accountID = "..."
            >>> client = API(access_token=...)
            >>> mo = LimitOrderRequest(instrument="EUR_USD",
            >>>                        units=10000, price=1.08)
            >>> print(json.dumps(mo.data, indent=4))
            >>> ...
        """
        super(LimitOrderRequest, self).__init__()

        # by default for a LIMIT order
        self._data.update({"type": OD.OrderType.LIMIT})
        self._data.update({"timeInForce": OD.TimeInForce.GTC})

        # required
        self._data.update({"instrument": instrument})
        self._data.update({"units": Units(units).value})
        self._data.update({"price": PriceValue(price).value})

        # optional
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
        return dict({"order": super(LimitOrderRequest, self).data})
