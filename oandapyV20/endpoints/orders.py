"""Handle orders and pendingOrders endpoints."""
from .apirequest import APIRequest, dyndoc_insert, get_endpoint_config

# responses serve both testing purpose aswell as dynamic docstring replacement
responses = {}

# op flags
ORDER_CREATE = 1
ORDER_LIST = 2
ORDER_DETAILS = 4
ORDER_REPLACE = 8
ORDER_CANCEL = 16
ORDER_CLIENT_EXTENSIONS = 32

endp_conf = {
    ORDER_CREATE: {"path_comp": None, "method": "POST"},
    ORDER_LIST: {"path_comp": None, "method": "GET"},
    ORDER_DETAILS: {"path_comp": None, "method": "GET"},
    ORDER_REPLACE: {"path_comp": None, "method": "PUT"},
    ORDER_CANCEL: {"path_comp": "cancel", "method": "PUT"},
    ORDER_CLIENT_EXTENSIONS: {"path_comp": "clientExtensions", "method": "PUT"}
}


class PendingOrders(APIRequest):
    """PendingOrders - class to handle the pendingOrders endpoint."""

    ENDPOINT = "v3/accounts/{}/pendingOrders"

    def __init__(self, accountID):
        """Instantiate a PendingOrders request.

        Parameters
        ----------
        accountID : string
            id of the account to perform the request on
        """
        endpoint = self.ENDPOINT.format(accountID)
        super(PendingOrders, self).__init__(endpoint)


class Orders(APIRequest):
    """Orders - class to handle the orders endpoints."""

    ENDPOINT = "v3/accounts/{accountID}/orders"

    @dyndoc_insert(responses)
    def __init__(self, accountID, orderID=None, data=None, op=None):
        """Instantiate an Orders request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        op : operation flag (required)
            this flag acts as task identifier. It is used to construct the API
            endpoint and determine the HTTP method for the request.

            Possible flags::

                ORDER_CREATE (data)
                ORDER_LIST
                ORDER_DETAILS
                ORDER_REPLACE (data)
                ORDER_CANCEL
                ORDER_CLIENT_EXTENSIONS (data)

                requests involving the 'data'-parameter require headers to
                be set: Content-Type: application/json)

        orderID : string
            id of the order to perform the request for.

        data : dict (optional)
            configuration details for the order in case of a request
            to create or modify an order.
        """
        endpoint = self.ENDPOINT
        method, path_comp = get_endpoint_config(endp_conf, op)

        if op in [ORDER_DETAILS, ORDER_REPLACE, ORDER_CANCEL,
                  ORDER_CLIENT_EXTENSIONS]:
            endpoint = '{}/{{orderID}}'.format(endpoint)

        if path_comp:
            endpoint = '{}/{}'.format(endpoint, path_comp)

        endpoint = endpoint.format(accountID=accountID, orderID=orderID)
        super(Orders, self).__init__(endpoint, method=method, body=data)
