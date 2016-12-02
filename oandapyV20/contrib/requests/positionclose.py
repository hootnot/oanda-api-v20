# -*- coding: utf-8 -*-
"""positionclose."""

from .baserequest import BaseRequest
from oandapyV20.types import Units


class PositionCloseRequest(BaseRequest):
    """create a PositionCloseRequest.

    PositionCloseRequest is used to build the body to close a position.
    The body can be used to pass to the PositionClose endpoint.
    """

    def __init__(self,
                 longUnits=None,
                 longClientExtensions=None,
                 shortUnits=None,
                 shortClientExtensions=None):
        """
        Instantiate a PositionCloseRequest.

        Parameters
        ----------

        longUnits : integer (optional)
            the number of long units to close

        longClientExtensions : dict (optional)
            dict representing longClientExtensions

        shortUnits : integer (optional)
            the number of short units to close

        shortClientExtensions : dict (optional)
            dict representing shortClientExtensions


        One of the parameters or both must be supplied.

        Example
        -------

        >>> import json
        >>> from oandapyV20 import API
        >>> import oandapyV20.endpoints.positions as positions
        >>> from oandapyV20.contrib.requests import PositionCloseRequest
        >>>
        >>> accountID = "..."
        >>> client = API(access_token=...)
        >>> ordr = PositionCloseRequest(longUnits=10000)
        >>> print(json.dumps(ordr.data, indent=4))
        {
           "longUnits": "10000"
        }
        >>> # now we have the order specification, create the order request
        >>> r = position.PositionClose(accountID,
        >>>                            instrument="EUR_USD", data=ordr.data)
        >>> # perform the request
        >>> rv = client.request(r)
        >>> print(rv)
        >>> ...
        """
        super(PositionCloseRequest, self).__init__()

        if not (longUnits or shortUnits):
            raise ValueError("longUnits and/or shortUnits parameter required")

        if longUnits:
            self._data.update({"longUnits": Units(longUnits).value})

            if longClientExtensions:
                self._data.update({"longClientExtensions":
                                   longClientExtensions})

        if shortUnits:
            self._data.update({"shortUnits": Units(shortUnits).value})

            if shortClientExtensions:
                self._data.update({"shortClientExtensions":
                                   shortClientExtensions})
