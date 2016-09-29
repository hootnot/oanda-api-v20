"""Handle orders and pendingOrders endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint, abstractclass

# responses serve both testing purpose aswell as dynamic docstring replacement
responses = {}


@abstractclass
class Orders(APIRequest):
    """Orders - class to handle the orders endpoints."""

    ENDPOINT = ""
    METHOD = "GET"

    @dyndoc_insert(responses)
    def __init__(self, accountID, orderID=None, data=None):
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
        endpoint = self.ENDPOINT.format(accountID=accountID, orderID=orderID)
        super(Orders, self).__init__(endpoint, method=self.METHOD, body=data)


@endpoint("v3/accounts/{accountID}/orders", "POST")
class OrderCreate(Orders):
    """OrderCreate.

    Create an Order for an Account.
    """


@endpoint("v3/accounts/{accountID}/orders")
class OrderList(Orders):
    """OrderList.

    Create an Order for an Account.
    """


@endpoint("v3/accounts/{accountID}/pendingOrders")
class OrdersPending(Orders):
    """OrdersPending.

    Create an Order for an Account.
    """


@endpoint("v3/accounts/{accountID}/orders/{orderID}")
class OrderDetails(Orders):
    """OrderDetails.

    Get details for a single Order in an Account.
    """


@endpoint("v3/accounts/{accountID}/orders/{orderID}", "PUT")
class OrderReplace(Orders):
    """OrderReplace.

    Replace an Order in an Account by simultaneously cancelling it and
    createing a replacement Order.
    """


@endpoint("v3/accounts/{accountID}/orders/{orderID}/cancel", "PUT")
class OrderCancel(Orders):
    """OrderCancel.

    Cancel a pending Order in an Account.
    """


@endpoint("v3/accounts/{accountID}/orders/{orderID}/clientExtensions", "PUT")
class OrderClientExtensions(Orders):
    """OrderClientExtensions.

    Update the Client Extensions for an Order in an Account. Do not set,
    modify or delete clientExtensions if your account is associated with MT4.
    """
