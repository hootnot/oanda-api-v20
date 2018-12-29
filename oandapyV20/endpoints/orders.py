# -*- coding: utf-8 -*-
"""Handle orders and pendingOrders endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint
from .responses.orders import responses
from abc import abstractmethod


class Orders(APIRequest):
    """Orders - abstract base class to handle the orders endpoints."""

    ENDPOINT = ""
    METHOD = "GET"
    EXPECTED_STATUS = 0

    @abstractmethod
    @dyndoc_insert(responses)
    def __init__(self, accountID, orderID=None):
        """Instantiate an Orders request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        orderID : string
            id of the order to perform the request for.
        """
        endpoint = self.ENDPOINT.format(accountID=accountID, orderID=orderID)
        super(Orders, self).__init__(endpoint, method=self.METHOD,
                                     expected_status=self.EXPECTED_STATUS)


@endpoint("v3/accounts/{accountID}/orders", "POST", 201)
class OrderCreate(Orders):
    """Create an Order for an Account."""

    HEADERS = {"Content-Type": "application/json"}

    @dyndoc_insert(responses)
    def __init__(self, accountID, data):
        """Instantiate an OrderCreate request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        data : JSON (required)
            json orderbody to send


        Orderbody example::

            {_v3_accounts_accountID_orders_create_body}

        >>> import oandapyV20
        >>> import oandapyV20.endpoints.orders as orders
        >>> client = oandapyV20.API(access_token=...)
        >>> r = orders.OrderCreate(accountID, data=data)
        >>> client.request(r)
        >>> print r.response

        ::

            {_v3_accounts_accountID_orders_create_resp}

        """
        super(OrderCreate, self).__init__(accountID)
        self.data = data


@endpoint("v3/accounts/{accountID}/orders")
class OrderList(Orders):
    """Create an Order for an Account."""

    @dyndoc_insert(responses)
    def __init__(self, accountID, params=None):
        """Instantiate an OrderList request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        params : dict
            optional request query parameters, check developer.oanda.com
            for details


        Example::

        >>> import oandapyV20
        >>> import oandapyV20.endpoints.orders as orders
        >>> client = oandapyV20.API(access_token=...)
        >>> r = orders.OrderList(accountID)
        >>> client.request(r)
        >>> print r.response


        Output::

            {_v3_accounts_accountID_orders_list_resp}

        """
        super(OrderList, self).__init__(accountID)
        self.params = params


@endpoint("v3/accounts/{accountID}/pendingOrders")
class OrdersPending(Orders):
    """List all pending Orders in an Account."""

    @dyndoc_insert(responses)
    def __init__(self, accountID):
        """Instantiate an OrdersPending request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.


        Example::

        >>> import oandapyV20
        >>> import oandapyV20.endpoints.orders as orders
        >>> client = oandapyV20.API(access_token=...)
        >>> r = orders.OrdersPending(accountID)
        >>> client.request(r)
        >>> print r.response


        Output::

            {_v3_accounts_accountID_orders_pending_resp}

        """
        super(OrdersPending, self).__init__(accountID)


@endpoint("v3/accounts/{accountID}/orders/{orderID}")
class OrderDetails(Orders):
    """Get details for a single Order in an Account."""

    @dyndoc_insert(responses)
    def __init__(self, accountID, orderID):
        """Instantiate an OrderDetails request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        orderID : string (required)
            id of the order to perform the request on.


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.orders as orders
        >>> client = oandapyV20.API(access_token=...)
        >>> r = orders.OrderDetails(accountID=..., orderID=...)
        >>> client.request(r)
        >>> print r.response

        Output::

            {_v3_accounts_accountID_order_details_resp}

        """
        super(OrderDetails, self).__init__(accountID, orderID)


@endpoint("v3/accounts/{accountID}/orders/{orderID}", "PUT", 201)
class OrderReplace(Orders):
    """OrderReplace.

    Replace an Order in an Account by simultaneously cancelling it and
    creating a replacement Order.
    """

    HEADERS = {"Content-Type": "application/json"}

    @dyndoc_insert(responses)
    def __init__(self, accountID, orderID, data):
        """Instantiate an OrderReplace request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        orderID : string (required)
            id of the order to perform the request on.

        data : JSON (required)
            json orderbody to send


        Orderbody example::

            {_v3_accounts_accountID_order_replace_body}

        >>> import oandapyV20
        >>> import oandapyV20.endpoints.orders as orders
        >>> client = oandapyV20.API(access_token=...)
        >>> data = {_v3_accounts_accountID_order_replace_body}
        >>> r = orders.OrderReplace(accountID=..., orderID=..., data=data)
        >>> client.request(r)
        >>> print r.response

        Output::

            {_v3_accounts_accountID_order_replace_resp}

        """
        super(OrderReplace, self).__init__(accountID, orderID)
        self.data = data


@endpoint("v3/accounts/{accountID}/orders/{orderID}/cancel", "PUT")
class OrderCancel(Orders):
    """Cancel a pending Order in an Account."""

    @dyndoc_insert(responses)
    def __init__(self, accountID, orderID):
        """Instantiate an OrdersCancel request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        orderID : string (required)
            id of the account to perform the request on.


        Example::

        >>> import oandapyV20
        >>> import oandapyV20.endpoints.orders as orders
        >>> client = oandapyV20.API(access_token=...)
        >>> r = orders.OrderCancel(accountID= ..., orderID=...)
        >>> client.request(r)
        >>> print r.response


        Output::

            {_v3_accounts_accountID_order_cancel_resp}

        """
        super(OrderCancel, self).__init__(accountID, orderID)


@endpoint("v3/accounts/{accountID}/orders/{orderID}/clientExtensions", "PUT")
class OrderClientExtensions(Orders):
    """Update the Client Extensions for an Order in an Account.

    .. warning::
        Do not set, modify or delete clientExtensions if your account
        is associated with MT4.
    """

    HEADERS = {"Content-Type": "application/json"}

    @dyndoc_insert(responses)
    def __init__(self, accountID, orderID, data):
        """Instantiate an OrderCreate request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        orderID : string (required)
            id of the order to perform the request on.

        data : JSON (required)
            json orderbody to send


        Orderbody example::

            {_v3_accounts_accountID_order_clientextensions_body}

        >>> import oandapyV20
        >>> import oandapyV20.endpoints.orders as orders
        >>> client = oandapyV20.API(access_token=...)
        >>> r = orders.OrderClientExtensions(accountID, orderID, data=data)
        >>> client.request(r)
        >>> print r.response

        ::

            {_v3_accounts_accountID_order_clientextensions_resp}

        """
        super(OrderClientExtensions, self).__init__(accountID, orderID)
        self.data = data
