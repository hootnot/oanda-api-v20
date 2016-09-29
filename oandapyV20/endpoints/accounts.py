"""Handle account endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint, abstractclass

# responses serve both testing purpose aswell as dynamic docstring replacement
responses = {
    "_v3_accounts": {
        "url": "/v3/accounts",
        "response": {
            "accounts": [
                {
                  "id": "101-004-1435156-002",
                  "tags": []
                },
                {
                  "id": "101-004-1435156-001",
                  "tags": []
                }
            ]
            },
        },
    "_v3_account_by_accountID": {
        "url": "/v3/accounts/{}",
        "response": {
            "account": {
                "trades": [
                    {
                        "instrument": "DE30_EUR",
                        "financing": "0.0000",
                        "openTime": "2016-07-12T09:32:18.062823776Z",
                        "initialUnits": "-10",
                        "currentUnits": "-10",
                        "price": "9984.7",
                        "unrealizedPL": "341.0000",
                        "realizedPL": "0.0000",
                        "state": "OPEN",
                        "id": "821"
                    },
                    {
                        "instrument": "DE30_EUR",
                        "financing": "0.0000",
                        "openTime": "2016-07-12T09:32:18.206929733Z",
                        "initialUnits": "-10",
                        "currentUnits": "-10",
                        "price": "9984.7",
                        "unrealizedPL": "341.0000",
                        "realizedPL": "0.0000",
                        "state": "OPEN",
                        "id": "823"
                    }
                ],
                "marginCloseoutNAV": "49393.6580",
                "marginUsed": "9948.9000",
                "currency": "EUR",
                "resettablePL": "-1301.0046",
                "NAV": "49377.6580",
                "marginCloseoutMarginUsed": "9949.8000",
                "id": "101-004-1435156-001",
                "marginCloseoutPositionValue": "198996.0000",
                "openTradeCount": 2,
                "orders": [
                    {
                        "partialFill": "DEFAULT_FILL",
                        "price": "0.87000",
                        "stopLossOnFill": {
                            "timeInForce": "GTC",
                            "price": "0.88000"
                        },
                        "timeInForce": "GTC",
                        "clientExtensions": {
                            "comment": "myComment",
                            "id": "myID"
                        },
                        "id": "204",
                        "triggerCondition": "TRIGGER_DEFAULT",
                        "replacesOrderID": "200",
                        "positionFill": "POSITION_DEFAULT",
                        "createTime": "2016-07-08T07:18:47.623211321Z",
                        "instrument": "EUR_GBP",
                        "state": "PENDING",
                        "units": "-50000",
                        "type": "LIMIT"
                    }
                ],
                "hedgingEnabled": False,
                "marginCloseoutPercent": "0.10072",
                "marginCallMarginUsed": "9949.8000",
                "openPositionCount": 1,
                "positionValue": "198978.0000",
                "pl": "-1301.0046",
                "lastTransactionID": "833",
                "marginAvailable": "39428.7580",
                "marginCloseoutUnrealizedPL": "698.0000",
                "marginRate": "0.05",
                "marginCallPercent": "0.20144",
                "pendingOrderCount": 1,
                "withdrawalLimit": "39428.7580",
                "unrealizedPL": "682.0000",
                "alias": "hootnotv20",
                "createdByUserID": 1435156,
                "positions": [
                    {
                        "short": {
                            "units": "0",
                            "resettablePL": "0.0000",
                            "unrealizedPL": "0.0000",
                            "pl": "0.0000"
                        },
                        "unrealizedPL": "0.0000",
                        "long": {
                            "units": "0",
                            "resettablePL": "-3.8046",
                            "unrealizedPL": "0.0000",
                            "pl": "-3.8046"
                        },
                        "instrument": "EUR_USD",
                        "resettablePL": "-3.8046",
                        "pl": "-3.8046"
                    },
                    {
                        "short": {
                            "unrealizedPL": "682.0000",
                            "tradeIDs": [
                                "821",
                                "823"
                            ],
                            "resettablePL": "-1744.8000",
                            "units": "-20",
                            "averagePrice": "9984.7",
                            "pl": "-1744.8000"
                        },
                        "unrealizedPL": "682.0000",
                        "long": {
                            "units": "0",
                            "resettablePL": "447.6000",
                            "unrealizedPL": "0.0000",
                            "pl": "447.6000"
                        },
                        "instrument": "DE30_EUR",
                        "resettablePL": "-1297.2000",
                        "pl": "-1297.2000"
                    }
                ],
                "createdTime": "2016-06-24T21:03:50.914647476Z",
                "balance": "48695.6580"
            },
            "lastTransactionID": "833"
        }
    },
    "_v3_account_by_accountID_configuration": {
        "url": "/v3/accounts/{}/configuration",
        "response": {
            "lastTransactionID": "830",
            "clientConfigureTransaction": {
                "userID": 1435156,
                "marginRate": "0.05",
                "batchID": "830",
                "time": "2016-07-12T19:48:11.657494168Z",
                "type": "CLIENT_CONFIGURE",
                "id": "830",
                "accountID": "101-004-1435156-001"
            }
        },
        "body": {
            "marginRate": "0.05"
        }
    }
}


@abstractclass
class Accounts(APIRequest):
    """Accounts - class to handle the accounts endpoints."""

    ENDPOINT = ""
    METHOD = "GET"

    @dyndoc_insert(responses)
    def __init__(self, accountID=None, data=None, op=None):
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
        super(Accounts, self).__init__(endpoint, method=self.METHOD, body=data)


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


@endpoint("v3/accounts/{accountID}/instruments")
class AccountInstruments(Accounts):
    """AccountInstruments.

    Get the list of tradable instruments for the given Account. The list of
    tradeable instruments is dependent on the regulatory division that the
    Account is located in, thus should be the same for all Accounts owned by a
    single user.
    """


@endpoint("v3/accounts/{accountID}/configuration", "PATCH")
class AccountConfiguration(Accounts):
    """AccountConfiguration.

    Set the client-configurable portions of an Account.
    """


@endpoint("v3/accounts/{accountID}/changes")
class AccountChanges(Accounts):
    """AccountChanges.

    Endpoint used to poll an Account for its current state and changes
    since a specified TransactionID.
    """
