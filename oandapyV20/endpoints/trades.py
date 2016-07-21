"""Handle trades endpoints."""
from .apirequest import APIRequest, dyndoc_insert, get_endpoint_config

# op flags
TRADE_LIST = 1
TRADE_DETAILS = 2
TRADE_CLOSE = 4
TRADE_UPDATE = 8
TRADE_CRC_DO = 16

responses = {}

endp_conf = {
    TRADE_LIST: {"path_comp": None, "method": "GET"},
    TRADE_DETAILS: {"path_comp": None, "method": "GET"},
    TRADE_CLOSE: {"path_comp": "close", "method": "PUT"},
    TRADE_UPDATE: {"path_comp": "clientExtensions", "method": "PUT"},
    TRADE_CRC_DO: {"path_comp": "orders", "method": "PUT"},
}


class OpenTrades(APIRequest):
    """Handle openTrades endpoint."""

    ENDPOINT = "/v3/accounts/{accountID}/openTrades"

    def __init__(self, accountID):
        """Instantiate an OpenTrades APIRequest instance.

        Parameters
        ----------
        accountID : string
            the accountID of the account.
        """
        endpoint = self.ENDPOINT.format(accountID=accountID)
        super(OpenTrades, self).__init__(endpoint)


class Trades(APIRequest):
    """Handle trades endpoints."""

    ENDPOINT = "v3/accounts/{accountID}/trades"

    @dyndoc_insert(responses)
    def __init__(self, accountID, tradeID=None, data=None, op=None):
        """Instantiate a Trades APIRequest instance.

        Parameters
        ----------
        accountID : string
            the account_id of the account.

        tradeID : string
            ID of the trade

        op : operation flag
            this flag acts as task identifier. It is used to construct the API
            endpoint and determine the HTTP method for the request.

        data : dict (optional)
            configuration details for request depending on the operation
            to be performed.
        """
        endpoint = self.ENDPOINT
        method, path_comp = get_endpoint_config(endp_conf, op)

        if op in [TRADE_DETAILS, TRADE_CLOSE, TRADE_UPDATE, TRADE_CRC_DO]:
            endpoint = "{}/{{tradeID}}".format(endpoint)

        if path_comp:
            endpoint = "{}/{}".format(endpoint, path_comp)

        endpoint = endpoint.format(accountID=accountID, tradeID=tradeID)
        super(Trades, self).__init__(endpoint, method=method, body=data)
