"""Handle position endpoints."""
from .apirequest import APIRequest, get_endpoint_config

# op flags
POSITION_LIST = 1
POSITION_DETAILS = 2
POSITION_CLOSE = 4

endp_conf = {
    POSITION_LIST: {"path_comp": None, "method": "GET"},
    POSITION_DETAILS: {"path_comp": None, "method": "GET"},
    POSITION_CLOSE: {"path_comp": "close", "method": "PUT"},
}


class OpenPositions(APIRequest):
    """OpenPositions - class to handle the 'openPositions' endpoint."""

    ENDPOINT = "v3/accounts/{accountID}/openPositions"

    def __init__(self, accountID):
        """Instantiate an OpenPositions APIRequest instance.

        Parameters
        ----------
        accountID : string (required)
            the id of the account to perform the request on.
        """
        endpoint = self.ENDPOINT.format(accountID=accountID)
        super(OpenPositions, self).__init__(endpoint)


class Positions(APIRequest):
    """Positions - class to handle the 'positions' endpoints."""

    ENDPOINT = "v3/accounts/{accountID}/positions"

    def __init__(self, accountID,
                 subject=None, instrument=None, data=None, op=None):
        """Instantiate a Positions APIRequest instance.

        Parameters
        ----------
        accountID : string (required)
            the id of the account to perform the request on.

        op : operation flag
            this flag acts as task identifier. It is used to construct the API
            endpoint and determine the HTTP method for the request.

            Possible flags::

                POSITION_LIST
                POSITION_DETAILS
                POSITION_CLOSE (data)

                requests involving the 'data'-parameter require headers to
                be set: Content-Type: application/json)


        instrument : string
            the instrument for the Positions request

        data : dict
            configuration details for the request, depending on the operation
            choosen this parameter may be required.
        """
        endpoint = self.ENDPOINT
        method, path_comp = get_endpoint_config(endp_conf, op)

        if op in [POSITION_DETAILS]:
            endpoint = '{}/{{instrument}}'.format(endpoint)

        if path_comp:
            endpoint = "{}/{}".format(endpoint, path_comp)

        endpoint = endpoint.format(accountID=accountID, instrument=instrument)
        super(Positions, self).__init__(endpoint, method=method, body=data)
