"""Handle position endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint, abstractclass, extendargs
from .responses.positions import responses


@abstractclass
class Positions(APIRequest):
    """Positions - class to handle the 'positions' endpoints."""

    ENDPOINT = ""
    METHOD = "GET"

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


@endpoint("v3/accounts/{accountID}/openPositions")
class OpenPositions(Positions):
    """OpenPositions.

    List all open Positions for an Account. An open Position is a Position
    in an Account that currently has a Trade opened for it.
    """


@endpoint("v3/accounts/{accountID}/positions/{instrument}")
class PositionDetails(Positions):
    """PositionDetails.

    Get the details of a single instrument's position in an Account. The
    position may be open or not.
    """


@extendargs("data")
@endpoint("v3/accounts/{accountID}/positions/{instrument}/close", "PUT")
class PositionClose(Positions):
    """PositionClose.

    Closeout the open Position for a specific instrument in an Account.
    """

    HEADERS = {"Content-Type": "application/json"}
