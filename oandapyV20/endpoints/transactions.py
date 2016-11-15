# -*- coding: utf-8 -*-
"""Handle transactions endpoints."""
from .apirequest import APIRequest
from ..exceptions import StreamTerminated
from .decorators import dyndoc_insert, endpoint
from .responses.transactions import responses
from types import GeneratorType
from abc import abstractmethod


class Transactions(APIRequest):
    """Transactions - abstract baseclass to handle transaction endpoints."""

    ENDPOINT = ""
    METHOD = "GET"

    @abstractmethod
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
        >>> import oandapyV20.endpoints.transactions as trans
        >>> client = oandapyV20.API(access_token=...)
        >>> r = trans.TransactionList(accountID)  # params optional
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
        >>> r = trans.TransactionIDRange(accountID=..., params=params)
        >>> client.request(r)
        >>> print r.response

        Output::

            {_v3_accounts_transaction_idrange_resp}

        """
        super(TransactionIDRange, self).__init__(accountID)
        self.params = params


@endpoint("v3/accounts/{accountID}/transactions/sinceid")
class TransactionsSinceID(Transactions):
    """TransactionsSinceID.

    Get a range of Transactions for an Account starting at (but not including)
    a provided Transaction ID.
    """

    @dyndoc_insert(responses)
    def __init__(self, accountID, params=None):
        """Instantiate an TransactionsSince request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        params : dict (required)
            query params to send, check developer.oanda.com for details.


        Query Params example::

            {_v3_accounts_transaction_sinceid_params}


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.transactions as trans
        >>> client = oandapyV20.API(access_token=...)
        >>> params = {_v3_accounts_transaction_sinceid_params}
        >>> r = trans.TransactionsSinceID(accountID=..., params=params)
        >>> client.request(r)
        >>> print r.response

        Output::

            {_v3_accounts_transaction_sinceid_resp}

        """
        super(TransactionsSinceID, self).__init__(accountID)
        self.params = params


@endpoint("v3/accounts/{accountID}/transactions/stream")
class TransactionsStream(Transactions):
    """TransactionsStream.

    Get a stream of Transactions for an Account starting from when the
    request is made.
    """

    STREAM = True

    @dyndoc_insert(responses)
    def __init__(self, accountID, params=None):
        """Instantiate an TransactionsStream request.

        Performing this request will result in a generator yielding
        transactions.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.transactions as trans
        >>> client = oandapyV20.API(access_token=...)
        >>> r = trans.TransactionsStream(accountID=...)
        >>> rv = client.request(r)
        >>> maxrecs = 5
        >>> try:
        >>>     for T in r.response:  # or rv ...
        >>>         print json.dumps(R, indent=4), ","
        >>>         maxrecs -= 1
        >>>         if maxrecs == 0:
        >>>             r.terminate("Got them all")
        >>> except StreamTerminated as e:
        >>>    print("Finished: {{msg}}".format(msg=e))

        Output::

            {_v3_accounts_transactions_stream_ciresp}

            Finished: Got them all

        """
        super(TransactionsStream, self).__init__(accountID)
        self.params = params

    def terminate(self, message=""):
        """terminate the stream.

        Calling this method will stop the generator yielding transaction
        records. A message can be passed optionally.
        """
        if not isinstance(self.response, GeneratorType):
            raise ValueError("request does not contain a stream response")

        self.response.throw(StreamTerminated(message))
