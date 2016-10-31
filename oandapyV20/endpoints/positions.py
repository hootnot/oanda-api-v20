"""Handle position endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint
from .responses.positions import responses
from abc import abstractmethod


class Positions(APIRequest):
    """Positions - abstractbase class to handle the 'positions' endpoints."""

    ENDPOINT = ""
    METHOD = "GET"

    @abstractmethod
    @dyndoc_insert(responses)
    def __init__(self, accountID, instrument=None):
        """Instantiate a Positions APIRequest instance.

        Parameters
        ----------
        accountID : string (required)
            the id of the account to perform the request on.

        instrument : string (optional)
            the instrument for the Positions request

        """
        endpoint = self.ENDPOINT.format(accountID=accountID,
                                        instrument=instrument)
        super(Positions, self).__init__(endpoint,
                                        method=self.METHOD)


@endpoint("v3/accounts/{accountID}/positions")
class PositionList(Positions):
    """PositionList.

    List all Positions for an Account. The Positions returned are for every
    instrument that has had a position during the lifetime of the Account.
    """

    @dyndoc_insert(responses)
    def __init__(self, accountID):
        """Instantiate a PositionList request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.positions as positions
        >>> accountID = ...
        >>> client = oandapyV20.API(access_token=...)
        >>> r = positions.PositionList(accountID=accountID)
        >>> client.request(r)
        >>> print r.response

        Output::

            {_v3_accounts_accountID_positions_resp}

        """
        super(PositionList, self).__init__(accountID)


@endpoint("v3/accounts/{accountID}/openPositions")
class OpenPositions(Positions):
    """OpenPositions.

    List all open Positions for an Account. An open Position is a Position
    in an Account that currently has a Trade opened for it.
    """

    @dyndoc_insert(responses)
    def __init__(self, accountID):
        """Instantiate an OpenPositions request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.positions as positions
        >>> accountID = ...
        >>> client = oandapyV20.API(access_token=...)
        >>> r = positions.OpenPositions(accountID=accountID)
        >>> client.request(r)
        >>> print r.response

        Output::

            {_v3_accounts_accountID_openpositions_resp}

        """
        super(OpenPositions, self).__init__(accountID)


@endpoint("v3/accounts/{accountID}/positions/{instrument}")
class PositionDetails(Positions):
    """PositionDetails.

    Get the details of a single instrument's position in an Account. The
    position may be open or not.
    """

    @dyndoc_insert(responses)
    def __init__(self, accountID, instrument):
        """Instantiate a PositionDetails request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        instrument : string (required)
            id of the instrument to get the position details for.


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.positions as positions
        >>> accountID = ...
        >>> instrument = ...
        >>> client = oandapyV20.API(access_token=...)
        >>> r = positions.PositionDetails(accountID=accountID, instrument)
        >>> client.request(r)
        >>> print r.response

        Output::

            {_v3_accounts_accountID_positiondetails_resp}

        """
        super(PositionDetails, self).__init__(accountID, instrument)


@endpoint("v3/accounts/{accountID}/positions/{instrument}/close", "PUT")
class PositionClose(Positions):
    """Closeout the open Position regarding instrument in an Account."""

    HEADERS = {"Content-Type": "application/json"}

    @dyndoc_insert(responses)
    def __init__(self, accountID, instrument, data):
        """Instantiate a PositionClose request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        instrument : string (required)
            instrument to close partially or fully.

        data : dict (required)
            closeout specification data to send, check developer.oanda.com
            for details.


        Data body example::

            {_v3_accounts_accountID_position_close_body}


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.positions as positions
        >>> accountID = ...
        >>> instrument = ...
        >>> client = oandapyV20.API(access_token=...)
        >>> data = {_v3_accounts_accountID_position_close_body}
        >>> r = positions.PositionClose(accountID=accountID,
        >>>                             instrument=instrument,
        >>>                             data=data)
        >>> client.request(r)
        >>> print r.response

        Output::

            {_v3_accounts_accountID_position_close_resp}

        """
        super(PositionClose, self).__init__(accountID, instrument)
        self.data = data
