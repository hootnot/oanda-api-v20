# -*- coding: utf-8 -*-
import six
from abc import ABCMeta, abstractmethod

from .baserequest import BaseRequest
from oandapyV20.types import PriceValue
import oandapyV20.definitions.orders as OD


@six.add_metaclass(ABCMeta)
class OnFill(BaseRequest):
    """baseclass for onFill requests."""

    @abstractmethod
    def __init__(self,
                 timeInForce=OD.TimeInForce.GTC,
                 gtdTime=None,
                 clientExtensions=None):
        super(OnFill, self).__init__()

        if timeInForce not in [OD.TimeInForce.GTC,
                               OD.TimeInForce.GTD,
                               OD.TimeInForce.GFD]:
            raise ValueError("timeInForce: {} invalid".format(timeInForce))

        self._data.update({"timeInForce": timeInForce})

        # optional, but required if
        if timeInForce == OD.TimeInForce.GTD and not gtdTime:
            raise ValueError("gtdTime: value required when timeInForce is GTD")
        self._data.update({"gtdTime": gtdTime})
        self._data.update({"clientExtensions": clientExtensions})


class TakeProfitDetails(OnFill):
    """Representation of the specification for a TakeProfitOrder.

    It is typically used to specify 'take profit details' for the
    'takeProfitOnFill' parameter of an OrderRequest. This way one
    can create the Take Profit Order as a dependency when an order
    gets filled.

    The other way to create a TakeProfitOrder is to create it afterwards
    on an existing trade. In that case you use TakeProfitOrderRequest on
    the trade.
    """

    def __init__(self,
                 price,
                 timeInForce=OD.TimeInForce.GTC,
                 gtdTime=None,
                 clientExtensions=None):
        """Instantiate TakeProfitDetails.

        Parameters
        ----------

        price : float or string (required)
            the price to trigger take profit order

        timeInForce : TimeInForce (required), default TimeInForce.GTC
            the time in force

        gtdTime : DateTime (optional)
            gtdTime is required in case timeInForce == TimeInForce.GTD

        Example
        -------

        >>> import json
        >>> from oandapyV20 import API
        >>> import oandapyV20.endpoints.orders as orders
        >>> from oandapyV20.contrib.requests import (
        >>>     MarketOrderRequest, TakeProfitDetails)
        >>>
        >>> accountID = "..."
        >>> client = API(access_token=...)
        >>> # at time of writing EUR_USD = 1.0740
        >>> # let us take profit at 1.10, GoodTillCancel (default)
        >>> takeProfitOnFillOrder = TakeProfitDetails(price=1.10)
        >>> print(takeProfitOnFillOrder.data)
        {
            "timeInForce": "GTC",
            "price": "1.10000"
        }
        >>> ordr = MarketOrderRequest(
        >>>     instrument="EUR_USD",
        >>>     units=10000,
        >>>     takeProfitOnFill=takeProfitOnFillOrder.data
        >>> )
        >>> # or as shortcut ...
        >>> #   takeProfitOnFill=TakeProfitDetails(price=1.10).data
        >>> print(json.dumps(ordr.data, indent=4))
        {
            "order": {
                "timeInForce": "FOK",
                "instrument": "EUR_USD",
                "units": "10000",
                "positionFill": "DEFAULT",
                "type": "MARKET",
                "takeProfitOnFill": {
                    "timeInForce": "GTC",
                    "price": "1.10000"
                }
            }
        }
        >>> r = orders.OrderCreate(accountID, data=ordr.data)
        >>> rv = client.request(r)
        >>> ...
        """
        super(TakeProfitDetails, self).__init__(
            timeInForce=timeInForce,
            gtdTime=gtdTime,
            clientExtensions=clientExtensions)
        self._data.update({"price": PriceValue(price).value})


class StopLossDetails(OnFill):
    """Representation of the specification for a StopLossOrder.

    It is typically used to specify 'stop loss details' for the
    'stopLossOnFill' parameter of an OrderRequest. This way one
    can create the Stop Loss Order as a dependency when an order
    gets filled.

    The other way to create a StopLossOrder is to create it afterwards
    on an existing trade. In that case you use StopLossOrderRequest on
    the trade.
    """

    def __init__(self,
                 price,
                 timeInForce=OD.TimeInForce.GTC,
                 gtdTime=None,
                 clientExtensions=None):
        """Instantiate StopLossDetails.

        Parameters
        ----------

        price : float or string (required)
            the price to trigger take profit order

        timeInForce : TimeInForce (required), default TimeInForce.GTC
            the time in force

        gtdTime : DateTime (optional)
            gtdTime is required in case timeInForce == TimeInForce.GTD

        clientExtensions : ClientExtensions (optional)


        Example
        -------

            >>> import json
            >>> from oandapyV20 import API
            >>> import oandapyV20.endpoints.orders as orders
            >>> from oandapyV20.contrib.requests import (
            >>>     MarketOrderRequest, StopLossDetails)
            >>>
            >>> accountID = "..."
            >>> client = API(access_token=...)
            >>> # at time of writing EUR_USD = 1.0740
            >>> # let us take profit at 1.10, GoodTillCancel (default)
            >>> stopLossOnFill = StopLossDetails(price=1.06)
            >>> print(stopLossOnFill)
            {
                "timeInForce": "GTC",
                "price": "1.10000"
            }
            >>> ordr = MarketOrderRequest(
            >>>     instrument="EUR_USD",
            >>>     units=10000,
            >>>     stopLossOnFill=stopLossOnFill.data
            >>> )
            >>> # or as shortcut ...
            >>> #   stopLossOnFill=StopLossDetails(price=1.06).data
            >>> print(json.dumps(ordr.data, indent=4))
            >>> r = orders.OrderCreate(accountID, data=ordr.data)
            >>> rv = client.request(r)
            >>> ...
        """
        super(StopLossDetails, self).__init__(
            timeInForce=timeInForce,
            gtdTime=gtdTime,
            clientExtensions=clientExtensions)
        self._data.update({"price": PriceValue(price).value})


class TrailingStopLossDetails(OnFill):
    """Representation of the specification for a TrailingStopLossOrder.

    It is typically used to specify 'trailing stop loss details' for the
    'trailingStopLossOnFill' parameter of an OrderRequest. This way one
    can create the Trailing Stop Loss Order as a dependency when an order
    gets filled.

    The other way to create a TrailingStopLossOrder is to create it afterwards
    on an existing trade. In that case you use TrailingStopLossOrderRequest on
    the trade.
    """

    def __init__(self,
                 distance,
                 timeInForce=OD.TimeInForce.GTC,
                 gtdTime=None,
                 clientExtensions=None):
        """Instantiate TrailingStopLossDetails.

        Parameters
        ----------

        distance : float or string (required)
            the price to trigger trailing stop loss order

        timeInForce : TimeInForce (required), default TimeInForce.GTC
            the time in force

        gtdTime : DateTime (optional)
            gtdTime is required in case timeInForce == TimeInForce.GTD

        clientExtensions : ClientExtensions (optional)


        Example
        -------

            >>> import json
            >>> from oandapyV20 import API
            >>> import oandapyV20.endpoints.orders as orders
            >>> from oandapyV20.contrib.requests import (
            >>>     MarketOrderRequest, TrailingStopLossDetails)
            >>>
            >>> accountID = "..."
            >>> client = API(access_token=...)
            >>> # at time of writing EUR_USD = 1.0740
            >>> # let us take profit at 1.10, GoodTillCancel (default)
            >>> trailingStopLossOnFill = TrailingStopLossDetails(price=1.06)
            >>> print(trailingStopLossOnFill)
            {
                "timeInForce": "GTC",
                "price": "1.10000"
            }
            >>> ordr = MarketOrderRequest(
            >>>     instrument="EUR_USD",
            >>>     units=10000,
            >>>     trailingStopLossOnFill=trailingStopLossOnFill.data
            >>> )
            >>> # or as shortcut ...
            >>> #   ...OnFill=trailingStopLossDetails(price=1.06).data
            >>> print(json.dumps(ordr.data, indent=4))
            >>> r = orders.OrderCreate(accountID, data=ordr.data)
            >>> rv = client.request(r)
            >>> ...
        """
        super(TrailingStopLossDetails, self).__init__(
            timeInForce=timeInForce,
            gtdTime=gtdTime,
            clientExtensions=clientExtensions)
        self._data.update({"distance": PriceValue(distance).value})
