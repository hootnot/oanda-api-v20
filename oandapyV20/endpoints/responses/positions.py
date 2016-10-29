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
        "url": "v3/accounts/{accountID}/positions/{instrument}",
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
    },
    "_v3_accounts_accountID_position_close": {
        "url": "v3/accounts/{accountID}/positions/{instrument}/close",
        "body": {
            "longUnits": "ALL"
        },
        "response": {
            "lastTransactionID": "6391",
            "longOrderCreateTransaction": {
                "accountID": "<ACCOUNT>",
                "batchID": "6390",
                "id": "6390",
                "instrument": "EUR_USD",
                "longPositionCloseout": {
                    "instrument": "EUR_USD",
                    "units": "ALL"
                },
                "positionFill": "REDUCE_ONLY",
                "reason": "POSITION_CLOSEOUT",
                "time": "2016-06-22T18:41:35.034041665Z",
                "timeInForce": "FOK",
                "type": "MARKET_ORDER",
                "units": "-251",
                "userID": "<USERID>"
            },
            "longOrderFillTransaction": {
                "accountBalance": "43650.69807",
                "accountID": "<ACCOUNT>",
                "batchID": "6390",
                "financing": "0.00000",
                "id": "6391",
                "instrument": "EUR_USD",
                "orderID": "6390",
                "pl": "-0.03370",
                "price": "1.13018",
                "reason": "MARKET_ORDER_POSITION_CLOSEOUT",
                "time": "2016-06-22T18:41:35.034041665Z",
                "tradesClosed": [
                    {
                        "financing": "0.00000",
                        "realizedPL": "-0.00013",
                        "tradeID": "6383",
                        "units": "-1"
                    },
                    {
                        "financing": "0.00000",
                        "realizedPL": "-0.03357",
                        "tradeID": "6385",
                        "units": "-250"
                    }
                ],
                "type": "ORDER_FILL",
                "units": "-251",
                "userID": "<USERID>"
            },
            "relatedTransactionIDs": [
                "6390",
                "6391"
            ]
        }
    }
}
