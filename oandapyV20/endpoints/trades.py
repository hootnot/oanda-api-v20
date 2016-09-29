"""Handle trades endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint, abstractclass

responses = {}


@abstractclass
class Trades(APIRequest):
    """Trades - class to handle the trades endpoints."""

    ENDPOINT = ""
    METHOD = "GET"

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

            Possible flags::

                TRADE_LIST
                TRADE_DETAILS
                TRADE_CLOSE (data)
                TRADE_UPDATE (data for clientExtensions)
                TRADE_CRC_DO (create, replace, cancel dependent order) (data)

                requests involving the 'data'-parameter require headers to
                be set: Content-Type: application/json)

        data : dict (optional)
            configuration details for request depending on the operation
            to be performed.
        """
        endpoint = self.ENDPOINT.format(accountID=accountID, tradeID=tradeID)
        super(Trades, self).__init__(endpoint, method=self.METHOD, body=data)


@endpoint("v3/accounts/{accountID}/trades")
class TradesList(Trades):
    """TradesList.

    Get a list of trades for an Account.
    """


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


@endpoint("v3/accounts/{accountID}/trades/{tradeID}/close", "PUT")
class TradeClose(Trades):
    """TradeClose.

    Close (partially or fully) a specific open Trade in an Account.
    """


@endpoint("v3/accounts/{accountID}/trades/{tradeID}/clientExtensions", "PUT")
class TradeClientExtensions(Trades):
    """TradeClientExtensions.

    Update the Client Extensions for a Trade. Do not add, update or delete
    the Client Extensions if your account is associated with MT4.
    """


@endpoint("v3/accounts/{accountID}/trades/{tradeID}/orders", "PUT")
class TradeCRCDO(Trades):
    """TradeCRCDO.

    Trade Create Replace Cancel Dependent Orders.
    """
