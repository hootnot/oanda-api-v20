# -*- coding: utf-8 -*-
"""Handle trades endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint
from .responses.trades import responses
from abc import abstractmethod


class Trades(APIRequest):
    """Trades - abstract baseclass to handle the trades endpoints."""

    ENDPOINT = ""
    METHOD = "GET"

    @abstractmethod
    @dyndoc_insert(responses)
    def __init__(self, accountID, tradeID=None):
        """Instantiate a Trades APIRequest instance.

        Parameters
        ----------
        accountID : string
            the account_id of the account.

        tradeID : string
            ID of the trade

        """
        endpoint = self.ENDPOINT.format(accountID=accountID, tradeID=tradeID)
        super(Trades, self).__init__(endpoint, method=self.METHOD)


@endpoint("v3/accounts/{accountID}/trades")
class TradesList(Trades):
    """Get a list of trades for an Account."""

    @dyndoc_insert(responses)
    def __init__(self, accountID, params=None):
        """Instantiate a TradesList request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        params : dict (optional)
            query params to send, check developer.oanda.com for details.


        Query Params example::

            {_v3_accounts_accountID_trades_params}


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.trades as trades
        >>> client = oandapyV20.API(access_token=...)
        >>> params = {_v3_accounts_accountID_trades_params}
        >>> r = trades.TradesList(accountID=..., params=params)
        >>> client.request(r)
        >>> print r.response

        Output::

            {_v3_accounts_accountID_trades_resp}

        """
        super(TradesList, self).__init__(accountID)
        self.params = params


@endpoint("v3/accounts/{accountID}/openTrades")
class OpenTrades(Trades):
    """Get the list of open Trades for an Account."""

    @dyndoc_insert(responses)
    def __init__(self, accountID):
        """Instantiate an OpenTrades request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.trades as trades
        >>> client = oandapyV20.API(access_token=...)
        >>> r = trades.OpenTrades(accountID=...)
        >>> client.request(r)
        >>> print r.response


        Output::

            {_v3_accounts_accountID_opentrades_resp}

        """
        super(OpenTrades, self).__init__(accountID)


@endpoint("v3/accounts/{accountID}/trades/{tradeID}")
class TradeDetails(Trades):
    """Get the details of a specific Trade in an Account."""

    @dyndoc_insert(responses)
    def __init__(self, accountID, tradeID):
        """Instantiate a TradeDetails request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        tradeID : string (required)
            id of the trade.


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.trades as trades
        >>> client = oandapyV20.API(access_token=...)
        >>> r = trades.TradeDetails(accountID=..., tradeID=...)
        >>> client.request(r)
        >>> print r.response


        Output::

            {_v3_account_accountID_trades_details_resp}

        """
        super(TradeDetails, self).__init__(accountID, tradeID)


@endpoint("v3/accounts/{accountID}/trades/{tradeID}/close", "PUT")
class TradeClose(Trades):
    """TradeClose.

    Close (partially or fully) a specific open Trade in an Account.
    """

    HEADERS = {"Content-Type": "application/json"}

    @dyndoc_insert(responses)
    def __init__(self, accountID, tradeID, data=None):
        """Instantiate a TradeClose request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        tradeID : string (required)
            id of the trade to close.

        data : dict (optional)
            data to send, use this to close a trade partially. Check
            developer.oanda.com for details.


        Data body example::

            {_v3_account_accountID_trades_close_body}


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.trades as trades
        >>> client = oandapyV20.API(access_token=...)
        >>> data = {_v3_account_accountID_trades_close_body}
        >>> r = trades.TradeClose(accountID=..., data=data)
        >>> client.request(r)
        >>> print r.response

        Output::

            {_v3_account_accountID_trades_close_resp}

        """
        super(TradeClose, self).__init__(accountID, tradeID)
        self.data = data


@endpoint("v3/accounts/{accountID}/trades/{tradeID}/clientExtensions", "PUT")
class TradeClientExtensions(Trades):
    """TradeClientExtensions.

    Update the Client Extensions for a Trade. Do not add, update or delete
    the Client Extensions if your account is associated with MT4.
    """

    HEADERS = {"Content-Type": "application/json"}

    @dyndoc_insert(responses)
    def __init__(self, accountID, tradeID, data=None):
        """Instantiate a TradeClientExtensions request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        tradeID : string (required)
            id of the trade to update client extensions for.

        data : dict (required)
            clientextension data to send, check developer.oanda.com
            for details.


        Data body example::

            {_v3_account_accountID_trades_cltext_body}


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.trades as trades
        >>> accountID = ...
        >>> tradeID = ...
        >>> client = oandapyV20.API(access_token=...)
        >>> data = {_v3_account_accountID_trades_cltext_body}
        >>> r = trades.TradeClientExtensions(accountID=accountID,
        >>>                                  tradeID=tradeID,
        >>>                                  data=data)
        >>> client.request(r)
        >>> print r.response

        Output::

            {_v3_account_accountID_trades_cltext_resp}

        """
        super(TradeClientExtensions, self).__init__(accountID, tradeID)
        self.data = data


@endpoint("v3/accounts/{accountID}/trades/{tradeID}/orders", "PUT")
class TradeCRCDO(Trades):
    """Trade Create Replace Cancel Dependent Orders."""

    HEADERS = {"Content-Type": "application/json"}

    @dyndoc_insert(responses)
    def __init__(self, accountID, tradeID, data):
        """Instantiate a TradeClientExtensions request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        tradeID : string (required)
            id of the trade to update client extensions for.

        data : dict (required)
            clientextension data to send, check developer.oanda.com
            for details.


        Data body example::

            {_v3_account_accountID_trades_crcdo_body}


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.trades as trades
        >>> accountID = ...
        >>> tradeID = ...
        >>> client = oandapyV20.API(access_token=...)
        >>> data = {_v3_account_accountID_trades_crcdo_body}
        >>> r = trades.TradeCRCDO(accountID=accountID,
        >>>                       tradeID=tradeID,
        >>>                       data=data)
        >>> client.request(r)
        >>> print r.response

        Output::

            {_v3_account_accountID_trades_crcdo_resp}

        """
        super(TradeCRCDO, self).__init__(accountID, tradeID)
        self.data = data
