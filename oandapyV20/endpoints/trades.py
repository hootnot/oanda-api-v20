# -*- encoding: utf-8 -*-
"""Handle trades endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint, abstractclass, extendargs
from .definitions.trades import definitions    # flake8: noqa
from .responses.trades import responses


@abstractclass
class Trades(APIRequest):
    """Trades - abstract baseclass to handle the trades endpoints."""

    ENDPOINT = ""
    METHOD = "GET"

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
    """OpenTrades.

    Get the list of open Trades for an Account.
    """


@endpoint("v3/accounts/{accountID}/trades/{tradeID}")
class TradeDetails(Trades):
    """TradeDetails.

    Get the details of a specific Trade in an Account.
    """


@extendargs("data")
@endpoint("v3/accounts/{accountID}/trades/{tradeID}/close", "PUT")
class TradeClose(Trades):
    """TradeClose.

    Close (partially or fully) a specific open Trade in an Account.
    """

    HEADERS = {"Content-Type": "application/json"}


@extendargs("data")
@endpoint("v3/accounts/{accountID}/trades/{tradeID}/clientExtensions", "PUT")
class TradeClientExtensions(Trades):
    """TradeClientExtensions.

    Update the Client Extensions for a Trade. Do not add, update or delete
    the Client Extensions if your account is associated with MT4.
    """

    HEADERS = {"Content-Type": "application/json"}


@extendargs("data")
@endpoint("v3/accounts/{accountID}/trades/{tradeID}/orders", "PUT")
class TradeCRCDO(Trades):
    """TradeCRCDO.

    Trade Create Replace Cancel Dependent Orders.
    """

    HEADERS = {"Content-Type": "application/json"}
