# -*- encoding: utf-8 -*-
"""Handle transactions endpoints."""
from .apirequest import APIRequest
from ..exceptions import StreamTerminated
from .decorators import dyndoc_insert, endpoint, abstractclass, extendargs
from .definitions.transactions import definitions    # flake8: noqa
from .responses.transactions import responses
from types import GeneratorType


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


@endpoint("v3/accounts/{accountID}/transactions")
class TransactionList(Transactions):
    """TransactionList.

    Get a list of Transactions pages that satisfy a time-based Transaction
    query.
    """

    @dyndoc_insert(responses)
    def __init__(self, accountID, params=None):
        """Instantiate a TransactionList request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        params : dict (optional)
            query params to send, check developer.oanda.com for details.


        Query Params example::

           {_v3_accounts_accountID_transactions_params}

        >>> import oandapyV20
        >>> import oandapyV20.endpoints.accounts as accounts
        >>> client = oandapyV20.API(access_token=...)
        >>> r = accounts.TransactionList(accountID)  # params optional
        >>> client.request(r)
        >>> print r.response

        Output::

           {_v3_accounts_accountID_transactions_resp}

        """
        super(TransactionList, self).__init__(accountID)
        self.params = params


@endpoint("v3/accounts/{accountID}/transactions/{transactionID}")
class TransactionDetails(Transactions):
    """Get the details of a single Account Transaction."""

    @dyndoc_insert(responses)
    def __init__(self, accountID, transactionID):
        """Instantiate a TransactionDetails request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        transactionID : string (required)
            id of the transaction


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.transactions as trans
        >>> client = oandapyV20.API(access_token=...)
        >>> r = trans.TransactionDetails(accountID=..., transactionID=...)
        >>> client.request(r)
        >>> print r.response

        Output::

           {_v3_accounts_transaction_details_resp}

        """
        super(TransactionDetails, self).__init__(accountID, transactionID)


@endpoint("v3/accounts/{accountID}/transactions/idrange")
class TransactionIDRange(Transactions):
    """TransactionIDRange.

    Get a range of Transactions for an Account based on Transaction IDs.
    """

    @dyndoc_insert(responses)
    def __init__(self, accountID, params=None):
        """Instantiate an TransactionIDRange request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        params : dict (required)
            query params to send, check developer.oanda.com for details.


        Query Params example::

            {_v3_accounts_transaction_idrange_params}


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.transactions as trans
        >>> client = oandapyV20.API(access_token=...)
        >>> params = {_v3_accounts_transaction_idrange_params}
        >>> r = accounts.AccountInstruments(accountID=..., params=params)
        >>> client.request(r)
        >>> print r.response

        Output::

            {_v3_accounts_transaction_idrange_resp}

        """
        super(TransactionIDRange, self).__init__(accountID)
        self.params = params


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
