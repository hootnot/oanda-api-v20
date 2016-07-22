"""Handle transactions endpoints."""
from .apirequest import APIRequest, dyndoc_insert, get_endpoint_config

responses = {}

# op flags
TRANSACTION_LIST = 1
TRANSACTION_DETAILS = 2
TRANSACTION_IDRANGE = 4
TRANSACTION_SINCEID = 8

endp_conf = {
    TRANSACTION_LIST: {"path_comp": None, "method": "GET"},
    TRANSACTION_DETAILS: {"path_comp": None, "method": "GET"},
    TRANSACTION_IDRANGE: {"path_comp": "idrange", "method": "GET"},
    TRANSACTION_SINCEID: {"path_comp": "sinceid", "method": "GET"},
}


class Transactions(APIRequest):
    """Transactions - class to handle the transaction endpoints."""

    ENDPOINT = "/v3/accounts/{accountID}/transactions"

    @dyndoc_insert(responses)
    def __init__(self, accountID, transactionID=None, op=None):
        """Instantiate a Transactions APIRequest instance.

        Parameters
        ----------
        accountID : string (required)
            the id of the account.

        transactionID : string
            the id of the transaction

        op : operation flag (required)
            this flag acts as task identifier. It is used to construct the API
            endpoint and determine the HTTP method for the request.

            Possible flags::

                TRANSACTION_LIST
                TRANSACTION_DETAILS
                TRANSACTION_IDRANGE
                TRANSACTION_SINCEID
        """
        endpoint = self.ENDPOINT
        method, path_comp = get_endpoint_config(endp_conf, op)

        if op in [TRANSACTION_DETAILS]:
            endpoint = "{}/{{transactionID}}".format(endpoint)

        if path_comp:
            endpoint = "{}/{}".format(endpoint, path_comp)

        endpoint = endpoint.format(accountID=accountID,
                                   transactionID=transactionID)
        super(Transactions, self).__init__(endpoint, method=method, body=None)
