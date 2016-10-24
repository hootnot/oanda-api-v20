# -*- encoding: utf-8 -*-
"""Handle orders and pendingOrders endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint, abstractclass, extendargs
from .definitions.orders import definitions    # flake8: noqa
from .responses.orders import responses


@abstractclass
class Orders(APIRequest):
    """Orders - class to handle the orders endpoints."""

    ENDPOINT = ""
    METHOD = "GET"
    EXPECTED_STATUS = 0

    @dyndoc_insert(responses)
    def __init__(self, accountID, orderID=None):
        """Instantiate an Orders request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        orderID : string
            id of the order to perform the request for.

        data : dict (optional)
            configuration details for the order in case of a request
            to create or modify an order.

        params : dict (depends on the endpoint to access)
            parameters for the request. This applies only the GET based
            endpoints.
        """
        endpoint = self.ENDPOINT.format(accountID=accountID, orderID=orderID)
        super(Orders, self).__init__(endpoint, method=self.METHOD,
                                     expected_status=self.EXPECTED_STATUS)


@extendargs("data")
@endpoint("v3/accounts/{accountID}/orders", "POST", 201)
class OrderCreate(Orders):
    """OrderCreate.

    Create an Order for an Account.
    """

    HEADERS = {"Content-Type": "application/json"}


@extendargs("params")
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


@extendargs("data")
@endpoint("v3/accounts/{accountID}/orders/{orderID}", "PUT", 201)
class OrderReplace(Orders):
    """OrderReplace.

    Replace an Order in an Account by simultaneously cancelling it and
    createing a replacement Order.
    """

    HEADERS = {"Content-Type": "application/json"}


@endpoint("v3/accounts/{accountID}/orders/{orderID}/cancel", "PUT")
class OrderCancel(Orders):
    """OrderCancel.

    Cancel a pending Order in an Account.
    """


@extendargs("data")
@endpoint("v3/accounts/{accountID}/orders/{orderID}/clientExtensions", "PUT")
class OrderClientExtensions(Orders):
    """OrderClientExtensions.

    Update the Client Extensions for an Order in an Account. Do not set,
    modify or delete clientExtensions if your account is associated with MT4.
    """

    HEADERS = {"Content-Type": "application/json"}
