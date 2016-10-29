"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement
"""
responses = {
    "_v3_accounts_accountID_positions": {
        "url": "v3/accounts/{accountID}/positions",
        "response": {
            "positions": [
                {
                    "short": {
                        "units": "0",
                        "resettablePL": "-272.6805",
                        "unrealizedPL": "0.0000",
                        "pl": "-272.6805"
                    },
                    "unrealizedPL": "0.0000",
                    "long": {
                        "units": "0",
                        "resettablePL": "0.0000",
                        "unrealizedPL": "0.0000",
                        "pl": "0.0000"
                    },
                    "instrument": "EUR_GBP",
                    "resettablePL": "-272.6805",
                    "pl": "-272.6805"
                },
                {
                    "short": {
                        "unrealizedPL": "870.0000",
                        "units": "-20",
                        "resettablePL": "-13959.3000",
                        "tradeIDs": [
                            "2121",
                            "2123"
                        ],
                        "averagePrice": "10581.5",
                        "pl": "-13959.3000"
                    },
                    "unrealizedPL": "870.0000",
                    "long": {
                        "units": "0",
                        "resettablePL": "404.5000",
                        "unrealizedPL": "0.0000",
                        "pl": "404.5000"
                    },
                    "instrument": "DE30_EUR",
                    "resettablePL": "-13554.8000",
                    "pl": "-13554.8000"
                },
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
                        "resettablePL": "-12.8720",
                        "unrealizedPL": "0.0000",
                        "pl": "-12.8720"
                    },
                    "instrument": "EUR_USD",
                    "resettablePL": "-12.8720",
                    "pl": "-12.8720"
                }
            ],
            "lastTransactionID": "2124"
        }
    },
    "_v3_accounts_accountID_openpositions": {
        "url": "v3/accounts/{accountID}/positions",
        "response": {
            "positions": [
                {
                    "short": {
                        "units": "0",
                        "resettablePL": "-14164.3000",
                        "unrealizedPL": "0.0000",
                        "pl": "-14164.3000"
                    },
                    "unrealizedPL": "-284.0000",
                    "long": {
                        "unrealizedPL": "-284.0000",
                        "units": "10",
                        "resettablePL": "404.5000",
                        "tradeIDs": [
                            "2315"
                        ],
                        "averagePrice": "10678.3",
                        "pl": "404.5000"
                    },
                    "instrument": "DE30_EUR",
                    "resettablePL": "-13759.8000",
                    "pl": "-13759.8000"
                },
                {
                    "short": {
                        "unrealizedPL": "-0.0738",
                        "units": "-100",
                        "resettablePL": "0.0000",
                        "tradeIDs": [
                            "2323"
                        ],
                        "averagePrice": "1.09843",
                        "pl": "0.0000"
                    },
                    "unrealizedPL": "-0.0738",
                    "long": {
                        "units": "0",
                        "resettablePL": "-44.6272",
                        "unrealizedPL": "0.0000",
                        "pl": "-44.6272"
                    },
                    "instrument": "EUR_USD",
                    "resettablePL": "-44.6272",
                    "pl": "-44.6272"
                }
            ],
            "lastTransactionID": "2327"
        }
    },
    "_v3_accounts_accountID_positiondetails": {
        "url": "v3/accounts/{accountID}/positions",
        "response": {
            "position": {
                "short": {
                    "unrealizedPL": "-0.0738",
                    "units": "-100",
                    "resettablePL": "0.0000",
                    "tradeIDs": [
                        "2323"
                    ],
                    "averagePrice": "1.09843",
                    "pl": "0.0000"
                },
                "unrealizedPL": "-0.0738",
                "long": {
                    "units": "0",
                    "resettablePL": "-44.6272",
                    "unrealizedPL": "0.0000",
                    "pl": "-44.6272"
                },
                "instrument": "EUR_USD",
                "resettablePL": "-44.6272",
                "pl": "-44.6272"
            },
            "lastTransactionID": "2327"
        }
    }
}
