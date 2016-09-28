"""Handle transactions endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint, abstractclass

responses = {}


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

        """
        endpoint = self.ENDPOINT.format(accountID=accountID,
                                        transactionID=transactionID)
        super(Transactions, self).__init__(endpoint,
                                           method=self.METHOD, body=None)


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


@endpoint("v3/accounts/{accountID}/transactions/idrange")
class TransactionIDRange(Transactions):
    """TransactionIDRange.

    Get a range of Transactions for an Account based on Transaction IDs.
    """


@endpoint("v3/accounts/{accountID}/transactions/sinceid")
class TransactionSinceID(Transactions):
    """TransactionSinceID.

    Get a range of Transactions for an Account starting at (but not including)
    a provided Transaction ID.
    """
