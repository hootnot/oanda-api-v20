# -*- encoding: utf-8 -*-
"""Handle account endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint, abstractclass, extendargs
from .definitions.accounts import definitions    # flake8: noqa
from .responses.accounts import responses


@abstractclass
class Accounts(APIRequest):
    """Accounts - class to handle the accounts endpoints."""

    ENDPOINT = ""
    METHOD = "GET"

    @dyndoc_insert(responses)
    def __init__(self, accountID=None):
        """Instantiate an Accounts APIRequest instance.

        Parameters
        ----------
        accountID : string (optional)
            the accountID of the account. Optional when requesting
            all accounts. For all other requests to the endpoint it is
            required.


        data : dict (depends on the endpoint to access)
            configuration details for the account in case of

            requests involving the 'data'-parameter require headers to
            be set: Content-Type: application/json)

        params : dict (depends on the endpoint to access)
            parameters for the request. This applies only the GET based
            endpoints

        Examples
        --------

        ::

            # get all accounts
            # corresponding API endpoint: GET {_v3_accounts_url}

            import oandapyv20 as oandapy
            import oandapyv20.endpoints.accounts as accounts

            access_token = "..."
            client = oandapy.API(access_token=access_token)
            r = accounts.AccountList()
            response = client.request(r)

        response::

            {_v3_accounts_resp}

        ::

            # get an account by accountID
            # corresponding API endpoint: GET {_v3_account_by_accountID_url}

            import oandapyv20 as oandapy
            import oandapyv20.endpoints.accounts as accounts

            access_token = "..."
            accountID = "101-004-1435156-002"
            client = oandapy.API(access_token=access_token)
            r = accounts.AccountDetails(accountID)
            response = client.request(r)

        response::

            {_v3_account_by_accountID_resp}

        ::

            # Set account configuration for account with id accountID
            # corresponding API endpoint:
            # PATCH {_v3_account_by_accountID_configuration_url}

            import oandapyv20 as oandapy
            import oandapyv20.endpoints.accounts as accounts

            access_token = "..."
            accountID = "101-004-1435156-002"
            configuration = {_v3_account_by_accountID_configuration_body}
            client = oandapy.API(access_token=access_token)

            r = accounts.AccountConfiguration(accountID, data=configuration)
            response = client.request(r)

        response::

            {_v3_account_by_accountID_configuration_resp}

        """
        endpoint = self.ENDPOINT.format(accountID=accountID)
        super(Accounts, self).__init__(endpoint, method=self.METHOD)


@endpoint("v3/accounts")
class AccountList(Accounts):
    """Get a list of all Accounts authorized for the provided token."""


@endpoint("v3/accounts/{accountID}")
class AccountDetails(Accounts):
    """AccountDetails.

    Get the full details for a single Account that a client has access
    to. Full pending Order, open Trade and open Position representations are
    provided.
    """


@endpoint("v3/accounts/{accountID}/summary")
class AccountSummary(Accounts):
    """AccountSummary.

    Get a summary for a single Account that a client has access to.
    """


@extendargs("params")
@endpoint("v3/accounts/{accountID}/instruments")
class AccountInstruments(Accounts):
    """AccountInstruments.

    Get the list of tradable instruments for the given Account. The list of
    tradeable instruments is dependent on the regulatory division that the
    Account is located in, thus should be the same for all Accounts owned by a
    single user.
    """


@extendargs("data")
@endpoint("v3/accounts/{accountID}/configuration", "PATCH")
class AccountConfiguration(Accounts):
    """AccountConfiguration.

    Set the client-configurable portions of an Account.
    """

    HEADERS = {"Content-Type": "application/json"}


@extendargs("params")
@endpoint("v3/accounts/{accountID}/changes")
class AccountChanges(Accounts):
    """AccountChanges.

    Endpoint used to poll an Account for its current state and changes
    since a specified TransactionID.
    """
