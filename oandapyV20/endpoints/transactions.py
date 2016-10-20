# -*- encoding: utf-8 -*-
"""Handle transactions endpoints."""
from .apirequest import APIRequest
from ..exceptions import StreamTerminated
from .decorators import dyndoc_insert, endpoint, abstractclass, extendargs
from .definitions.transactions import definitions    # flake8: noqa
from types import GeneratorType

responses = {
    "_v3_accounts_accountID_transactions": {
        "url": "v3/accounts/{accountID}/transactions",
        "response": {
            "count": 2124,
            "from": "2016-06-24T21:03:50.914647476Z",
            "lastTransactionID": "2124",
            "pageSize": 100,
            "to": "2016-10-05T06:54:14.025946546Z",
            "pages": [
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1&to=100",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=101&to=200",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=201&to=300",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=301&to=400",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=401&to=500",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=501&to=600",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=601&to=700",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=701&to=800",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=801&to=900",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=901&to=1000",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1001&to=1100",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1101&to=1200",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1201&to=1300",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1301&to=1400",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1401&to=1500",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1501&to=1600",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1601&to=1700",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1701&to=1800",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1801&to=1900",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1901&to=2000",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=2001&to=2100",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=2101&to=2124"
            ]
        }
    }
}


@abstractclass
class Transactions(APIRequest):
    """Transactions - class to handle the transaction endpoints."""

    ENDPOINT = ""
    METHOD = "GET"

    @dyndoc_insert(responses)
    def __init__(self, accountID, transactionID=None):
        """Instantiate a Transactions APIRequest instance.

        Parameters
        ----------
        accountID : string (required)
            the id of the account.

        transactionID : string
            the id of the transaction

        params : dict (depends on the endpoint to access)
            parameters for the request. This applies only the GET based
            endpoints
        """
        endpoint = self.ENDPOINT.format(accountID=accountID,
                                        transactionID=transactionID)
        super(Transactions, self).__init__(endpoint,
                                           method=self.METHOD)


@extendargs("params")
@endpoint("v3/accounts/{accountID}/transactions")
class TransactionList(Transactions):
    """TransactionList.

    Get a list of Transactions pages that satisfy a time-based Transaction
    query.
    """


@endpoint("v3/accounts/{accountID}/transactions/{transactionID}")
class TransactionDetails(Transactions):
    """TransactionDetails.

    Get the details of a single Account Transaction.
    """


@extendargs("params")
@endpoint("v3/accounts/{accountID}/transactions/idrange")
class TransactionIDRange(Transactions):
    """TransactionIDRange.

    Get a range of Transactions for an Account based on Transaction IDs.
    """


@extendargs("params")
@endpoint("v3/accounts/{accountID}/transactions/sinceid")
class TransactionSinceID(Transactions):
    """TransactionSinceID.

    Get a range of Transactions for an Account starting at (but not including)
    a provided Transaction ID.
    """


@extendargs("params")
@endpoint("v3/accounts/{accountID}/transactions/stream")
class TransactionsStream(Transactions):
    """TransactionsStream.

    Get a stream of Transactions for an Account starting from when the
    request is made.
    """

    STREAM = True

    def terminate(self, message=""):
        if not isinstance(self.response, GeneratorType):
            raise ValueError("request does not contain a stream response")

        self.response.throw(StreamTerminated(message))
