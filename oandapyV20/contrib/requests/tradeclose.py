# -*- coding: utf-8 -*-
"""tradeclose."""

from .baserequest import BaseRequest


class TradeCloseRequest(BaseRequest):
    """create a TradeCloseRequest.

    TradeCloseRequest is used to build the body to close a trade.
    The body can be used to pass to the TradeClose endpoint.
    """

    def __init__(self, units="ALL"):
        """
        Instantiate a TradeCloseRequest.

        Parameters
        ----------

        units : integer (optional)
            the number of units to close. Default it is set to "ALL".

        Example
        -------

        >>> import json
        >>> from oandapyV20 import API
        >>> import oandapyV20.endpoints.trades as trades
        >>> from oandapyV20.contrib.requests import TradeCloseRequest
        >>>
        >>> accountID = "..."
        >>> client = API(access_token=...)
        >>> ordr = TradeCloseRequest(units=10000)
        >>> print(json.dumps(ordr.data, indent=4))
        {
           "units": "10000"
        }
        >>> # now we have the order specification, create the order request
        >>> r = trades.TradeClose(accountID, tradeID=1234,
        >>>                       data=ordr.data)
        >>> # perform the request
        >>> rv = client.request(r)
        >>> print(rv)
        >>> ...
        """
        super(TradeCloseRequest, self).__init__()

        # by default for a TradeClose no parameters are required
        if units:
            self._data.update(
                {"units":
                 "{:d}".format(int(units)) if units != "ALL" else "ALL"})
