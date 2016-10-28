"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement
"""
responses = {
    "_v3_accounts_accountID_trades": {
        "url": "v3/accounts/101-004-1435156-001/trades",
        "params": {
            "instrument": "DE30_EUR,EUR_USD"
        },
        "response": {
            "trades": [
                {
                    "financing": "0.0000",
                    "openTime": "2016-10-28T14:28:05.231759081Z",
                    "price": "10678.3",
                    "unrealizedPL": "25.0000",
                    "realizedPL": "0.0000",
                    "instrument": "DE30_EUR",
                    "state": "OPEN",
                    "initialUnits": "10",
                    "currentUnits": "10",
                    "id": "2315"
                },
                {
                    "financing": "0.0000",
                    "openTime": "2016-10-28T14:27:19.011002322Z",
                    "price": "1.09448",
                    "unrealizedPL": "-0.0933",
                    "realizedPL": "0.0000",
                    "instrument": "EUR_USD",
                    "state": "OPEN",
                    "initialUnits": "100",
                    "currentUnits": "100",
                    "id": "2313"
                }
            ],
            "lastTransactionID": "2315"
        }
    }
}
