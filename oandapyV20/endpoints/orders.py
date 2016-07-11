"""Handle orders and pendingOrders endpoints."""
from .apirequest import APIRequest


class PendingOrders(APIRequest):
    """PendingOrders - class to handle the pendingOrders endpoint."""

    ENDPOINT = "/v3/accounts/{}/pendingOrders"

    def __init__(self, account_id):
        """Instantiate a PendingOrders request.

        Parameters
        ----------
        account_id : string
            id of the account to perform the request on
        """
        endpoint = self.ENDPOINT
        endpoint = endpoint.format(account_id)
        super(PendingOrders, self).__init__(endpoint)


class Orders(APIRequest):
    """Accounts - class to handle the /v3/accounts endpoint."""

    ENDPOINT = "/v3/accounts/{}/orders"

    def __init__(self, account_id,
                 subject=None, orderID=None, configuration=None):
        """Instantiate an Orders request.

        Parameters
        ----------
        account_id : string
            id of the account to perform the request on

        subject : string
            static final part of the endpoint defining the details of the
            request.

        orderID : string
            id of the order to perform the request for

        account_id : string
            id of the account to perform the request on

        configuration : dict (optional)
            configuration details for the order in case of a request
            to create or modify an order.
        """
        endpoint = self.ENDPOINT.format(account_id)
        if orderID:
            endpoint = '{}/{}'.format(endpoint, orderID)

        if subject:
            endpoint = '{}/{}'.format(endpoint, subject)

        super(Orders, self).__init__(endpoint)

        self.body = configuration
        if orderID and (subject or configuration):
            self.method = "PUT"
        elif configuration:
            self.method = "POST"
