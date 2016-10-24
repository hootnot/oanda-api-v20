"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement
"""
responses = {
    "_v3_accounts_accountID_trades": {
        "url": "v3/accounts/101-004-1435156-001/trades",
        "response": {
            "trades": [
                {
                    "financing": "-1.8516",
                    "openTime": "2016-10-04T08:51:40.444453952Z",
                    "price": "10581.5",
                    "unrealizedPL": "250.0000",
                    "realizedPL": "0.0000",
                    "instrument": "DE30_EUR",
                    "state": "OPEN",
                    "initialUnits": "-10",
                    "currentUnits": "-10",
                    "id": "2123"
                },
                {
                    "financing": "-1.8516",
                    "openTime": "2016-10-04T08:51:40.214522674Z",
                    "price": "10581.5",
                    "unrealizedPL": "250.0000",
                    "realizedPL": "0.0000",
                    "instrument": "DE30_EUR",
                    "state": "OPEN",
                    "initialUnits": "-10",
                    "currentUnits": "-10",
                    "id": "2121"
                }
            ],
            "lastTransactionID": "2124"
        }
    }
}
