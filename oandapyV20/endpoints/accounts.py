# -*- coding: utf-8 -*-
"""Handle account endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint
from .responses.accounts import responses
from abc import abstractmethod


class Accounts(APIRequest):
    """Accounts - class to handle the accounts endpoints."""

    ENDPOINT = ""
    METHOD = "GET"

    @abstractmethod
    @dyndoc_insert(responses)
    def __init__(self, accountID=None):
        """Instantiate an Accounts APIRequest instance.

        Parameters
        ----------
        accountID : string (optional)
            the accountID of the account. Optional when requesting
            all accounts. For all other requests to the endpoint it is
            required.

        """
        endpoint = self.ENDPOINT.format(accountID=accountID)
        super(Accounts, self).__init__(endpoint, method=self.METHOD)


@endpoint("v3/accounts")
class AccountList(Accounts):
    """Get a list of all Accounts authorized for the provided token."""

    @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate an AccountList request.

        >>> import oandapyV20
        >>> import oandapyV20.endpoints.accounts as accounts
        >>> client = oandapyV20.API(access_token=...)
        >>> r = accounts.AccountList()
        >>> client.request(r)
        >>> print r.response

        ::

            {_v3_accounts_resp}

        """
        super(AccountList, self).__init__()


@endpoint("v3/accounts/{accountID}")
class AccountDetails(Accounts):
    """AccountDetails.

    Get the full details for a single Account that a client has access
    to. Full pending Order, open Trade and open Position representations are
    provided.
    """

    @dyndoc_insert(responses)
    def __init__(self, accountID):
        """Instantiate an AccountDetails request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.accounts as accounts
        >>> client = oandapyV20.API(access_token=...)
        >>> r = accounts.AccountDetails(accountID)
        >>> client.request(r)
        >>> print r.response

        ::

            {_v3_account_by_accountID_resp}

        """
        super(AccountDetails, self).__init__(accountID)


@endpoint("v3/accounts/{accountID}/summary")
class AccountSummary(Accounts):
    """Get a summary for a single Account that a client has access to."""

    @dyndoc_insert(responses)
    def __init__(self, accountID):
        """Instantiate an AccountSummary request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.accounts as accounts
        >>> client = oandapyV20.API(access_token=...)
        >>> r = accounts.AccountSummary(accountID)
        >>> client.request(r)
        >>> print r.response

        ::

            {_v3_account_by_accountID_summary_resp}

        """
        super(AccountSummary, self).__init__(accountID)


@endpoint("v3/accounts/{accountID}/instruments")
class AccountInstruments(Accounts):
    """AccountInstruments.

    Get the list of tradable instruments for the given Account. The list of
    tradeable instruments is dependent on the regulatory division that the
    Account is located in, thus should be the same for all Accounts owned by a
    single user.
    """

    @dyndoc_insert(responses)
    def __init__(self, accountID, params=None):
        """Instantiate an AccountInstruments request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        params : dict (optional)
            query params to send, check developer.oanda.com for details.


        Query Params example::

            {_v3_account_by_accountID_instruments_params}


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.accounts as accounts
        >>> client = oandapyV20.API(access_token=...)
        >>> params = ...
        >>> r = accounts.AccountInstruments(accountID=..., params=params)
        >>> client.request(r)
        >>> print r.response

        Output::

            {_v3_account_by_accountID_instruments_resp}

        """
        super(AccountInstruments, self).__init__(accountID)
        self.params = params


@endpoint("v3/accounts/{accountID}/configuration", "PATCH")
class AccountConfiguration(Accounts):
    """Set the client-configurable portions of an Account."""

    HEADERS = {"Content-Type": "application/json"}

    @dyndoc_insert(responses)
    def __init__(self, accountID, data):
        """Instantiate an AccountConfiguration request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        data : dict (required)
            json body to send


        body example::

            {_v3_accounts_accountID_account_config_body}

        >>> import oandapyV20
        >>> import oandapyV20.endpoints.accounts as accounts
        >>> client = oandapyV20.API(access_token=...)
        >>> r = accounts.AccountConfiguration(accountID, data=data)
        >>> client.request(r)
        >>> print r.response

        ::

            {_v3_accounts_accountID_account_config_resp}

        """
        super(AccountConfiguration, self).__init__(accountID)
        self.data = data


@endpoint("v3/accounts/{accountID}/changes")
class AccountChanges(Accounts):
    """AccountChanges.

    Endpoint used to poll an Account for its current state and changes
    since a specified TransactionID.
    """

    @dyndoc_insert(responses)
    def __init__(self, accountID, params=None):
        """Instantiate an AccountChanges request.

        Parameters
        ----------
        accountID : string (required)
            id of the account to perform the request on.

        params : dict (optional)
            query params to send, check developer.oanda.com for details.


        Query Params example::

            {_v3_accounts_accountID_account_changes_params}

        >>> import oandapyV20
        >>> import oandapyV20.endpoints.accounts as accounts
        >>> client = oandapyV20.API(access_token=...)
        >>> params = ...
        >>> r = accounts.AccountChanges(accountID=..., params=params)
        >>> client.request(r)
        >>> print r.response

        Output::

            {_v3_accounts_accountID_account_changes_resp}

        """
        super(AccountChanges, self).__init__(accountID)
        self.params = params
