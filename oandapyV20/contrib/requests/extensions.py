# -*- coding: utf-8 -*-

from .baserequest import BaseRequest
from oandapyV20.types import ClientID, ClientTag, ClientComment


class ClientExtensions(BaseRequest):
    """Representation of the ClientExtensions."""

    def __init__(self,
                 clientID=None,
                 clientTag=None,
                 clientComment=None):
        """Instantiate ClientExtensions.

        Parameters
        ----------

        clientID : clientID (required)
            the clientID

        clientTag : clientTag (required)
            the clientTag

        clientComment : clientComment (required)
            the clientComment


        Example
        -------

            >>> import json
            >>> from oandapyV20 import API
            >>> import oandapyV20.endpoints.orders as orders
            >>> from oandapyV20.contrib.requests import (
            ...     MarketOrderRequest, TakeProfitDetails, ClientExtensions)
            >>>
            >>> accountID = "..."
            >>> client = API(access_token=...)
            >>> # at time of writing EUR_USD = 1.0740
            >>> # let us take profit at 1.10, GoodTillCancel (default)
            >>> # add clientExtensions to it also
            >>> takeProfitOnFillOrder = TakeProfitDetails(
            ...     price=1.10,
            ...     clientExtensions=ClientExtensions(clientTag="mytag").data)
            >>> print(takeProfitOnFillOrder.data)
            {
                'timeInForce': 'GTC',
                'price": '1.10000',
                'clientExtensions': {'tag': 'mytag'}
            }
            >>> ordr = MarketOrderRequest(
            ...     instrument="EUR_USD",
            ...     units=10000,
            ...     takeProfitOnFill=takeProfitOnFillOrder.data
            ... )
            >>> # or as shortcut ...
            >>> #   takeProfitOnFill=TakeProfitDetails(price=1.10).data
            >>> print(json.dumps(ordr.data, indent=4))
            >>> r = orders.OrderCreate(accountID, data=ordr.data)
            >>> rv = client.request(r)
            >>> ...
        """
        super(ClientExtensions, self).__init__()
        if not (clientID or clientTag or clientComment):
            raise ValueError("clientID, clientTag, clientComment required")

        if clientID:
            self._data.update({"id": ClientID(clientID).value})

        if clientTag:
            self._data.update({"tag": ClientTag(clientTag).value})

        if clientComment:
            self._data.update({"comment": ClientComment(clientComment).value})
