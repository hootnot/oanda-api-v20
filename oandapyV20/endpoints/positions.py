"""Handle position endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint, abstractclass

responses = {
    "_v3_accounts_accountID_positions": {
        "url": "v3/accounts/{accountID}/positions",
        "response": {
            "positions": [
                {
                    "short": {
                        "units": "0",
                        "resettablePL": "-272.6805",
                        "unrealizedPL": "0.0000",
                        "pl": "-272.6805"
                    },
                    "unrealizedPL": "0.0000",
                    "long": {
                        "units": "0",
                        "resettablePL": "0.0000",
                        "unrealizedPL": "0.0000",
                        "pl": "0.0000"
                    },
                    "instrument": "EUR_GBP",
                    "resettablePL": "-272.6805",
                    "pl": "-272.6805"
                },
                {
                    "short": {
                        "unrealizedPL": "870.0000",
                        "units": "-20",
                        "resettablePL": "-13959.3000",
                        "tradeIDs": [
                            "2121",
                            "2123"
                        ],
                        "averagePrice": "10581.5",
                        "pl": "-13959.3000"
                    },
                    "unrealizedPL": "870.0000",
                    "long": {
                        "units": "0",
                        "resettablePL": "404.5000",
                        "unrealizedPL": "0.0000",
                        "pl": "404.5000"
                    },
                    "instrument": "DE30_EUR",
                    "resettablePL": "-13554.8000",
                    "pl": "-13554.8000"
                },
                {
                    "short": {
                        "units": "0",
                        "resettablePL": "0.0000",
                        "unrealizedPL": "0.0000",
                        "pl": "0.0000"
                    },
                    "unrealizedPL": "0.0000",
                    "long": {
                        "units": "0",
                        "resettablePL": "-12.8720",
                        "unrealizedPL": "0.0000",
                        "pl": "-12.8720"
                    },
                    "instrument": "EUR_USD",
                    "resettablePL": "-12.8720",
                    "pl": "-12.8720"
                }
            ],
            "lastTransactionID": "2124"
        }
    }
}


@abstractclass
class Positions(APIRequest):
    """Positions - class to handle the 'positions' endpoints."""

    ENDPOINT = ""
    METHOD = "GET"

    @dyndoc_insert(responses)
    def __init__(self, accountID, instrument=None, data=None):
        """Instantiate a Positions APIRequest instance.

        Parameters
        ----------
        accountID : string (required)
            the id of the account to perform the request on.

        instrument : string
            the instrument for the Positions request

        data : dict
            configuration details for the request, depending on the operation
            choosen this parameter may be required.
        """
        endpoint = self.ENDPOINT.format(accountID=accountID,
                                        instrument=instrument)
        super(Positions, self).__init__(endpoint,
                                        method=self.METHOD, body=data)


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


@endpoint("v3/accounts/{accountID}/positions/{instrument}/close", "PUT")
class PositionClose(Positions):
    """PositionClose.

    Closeout the open Position for a specific instrument in an Account.
    """
