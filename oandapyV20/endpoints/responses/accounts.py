"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement
"""
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
    "_v3_account_by_accountID_summary": {
        "url": "v3/accounts/{accountID}/summary",
        "response": {
            "account": {
                "marginCloseoutNAV": "35454.4740",
                "marginUsed": "10581.5000",
                "currency": "EUR",
                "resettablePL": "-13840.3525",
                "NAV": "35454.4740",
                "marginCloseoutMarginUsed": "10581.5000",
                "marginCloseoutPositionValue": "211630.0000",
                "openTradeCount": 2,
                "id": "101-004-1435156-001",
                "openPositionCount": 1,
                "marginCloseoutPercent": "0.14923",
                "marginCallMarginUsed": "10581.5000",
                "hedgingEnabled": False,
                "positionValue": "211630.0000",
                "pl": "-13840.3525",
                "lastTransactionID": "2123",
                "marginAvailable": "24872.9740",
                "marginRate": "0.05",
                "marginCallPercent": "0.29845",
                "pendingOrderCount": 0,
                "withdrawalLimit": "24872.9740",
                "unrealizedPL": "0.0000",
                "alias": "hootnotv20",
                "createdByUserID": 1435156,
                "marginCloseoutUnrealizedPL": "0.0000",
                "createdTime": "2016-06-24T21:03:50.914647476Z",
                "balance": "35454.4740"
            },
            "lastTransactionID": "2123"
        }
    },
    "_v3_account_by_accountID_instruments": {
        "url": "/v3/accounts/{accountID}/instuments",
        "response": {
            "instruments": [
                {
                    "minimumTradeSize": "1",
                    "displayName": "Europe 50",
                    "name": "EU50_EUR",
                    "displayPrecision": 1,
                    "type": "CFD",
                    "minimumTrailingStopDistance": "5.0",
                    "marginRate": "0.05",
                    "maximumOrderUnits": "3000",
                    "tradeUnitsPrecision": 0,
                    "pipLocation": 0,
                    "maximumPositionSize": "0",
                    "maximumTrailingStopDistance": "10000.0"
                },
                {
                    "minimumTradeSize": "1",
                    "displayName": "EUR/USD",
                    "name": "EUR_USD",
                    "displayPrecision": 5,
                    "type": "CURRENCY",
                    "minimumTrailingStopDistance": "0.00050",
                    "marginRate": "0.05",
                    "maximumOrderUnits": "100000000",
                    "tradeUnitsPrecision": 0,
                    "pipLocation": -4,
                    "maximumPositionSize": "0",
                    "maximumTrailingStopDistance": "1.00000"
                },
                {
                    "minimumTradeSize": "1",
                    "displayName": "US Wall St 30",
                    "name": "US30_USD",
                    "displayPrecision": 1,
                    "type": "CFD",
                    "minimumTrailingStopDistance": "5.0",
                    "marginRate": "0.05",
                    "maximumOrderUnits": "1000",
                    "tradeUnitsPrecision": 0,
                    "pipLocation": 0,
                    "maximumPositionSize": "0",
                    "maximumTrailingStopDistance": "10000.0"
                },
                {
                    "minimumTradeSize": "1",
                    "displayName": "France 40",
                    "name": "FR40_EUR",
                    "displayPrecision": 1,
                    "type": "CFD",
                    "minimumTrailingStopDistance": "5.0",
                    "marginRate": "0.05",
                    "maximumOrderUnits": "2000",
                    "tradeUnitsPrecision": 0,
                    "pipLocation": 0,
                    "maximumPositionSize": "0",
                    "maximumTrailingStopDistance": "10000.0"
                },
                {
                    "minimumTradeSize": "1",
                    "displayName": "EUR/CHF",
                    "name": "EUR_CHF",
                    "displayPrecision": 5,
                    "type": "CURRENCY",
                    "minimumTrailingStopDistance": "0.00050",
                    "marginRate": "0.05",
                    "maximumOrderUnits": "100000000",
                    "tradeUnitsPrecision": 0,
                    "pipLocation": -4,
                    "maximumPositionSize": "0",
                    "maximumTrailingStopDistance": "1.00000"
                },
                {
                    "minimumTradeSize": "1",
                    "displayName": "Germany 30",
                    "name": "DE30_EUR",
                    "displayPrecision": 1,
                    "type": "CFD",
                    "minimumTrailingStopDistance": "5.0",
                    "marginRate": "0.05",
                    "maximumOrderUnits": "2500",
                    "tradeUnitsPrecision": 0,
                    "pipLocation": 0,
                    "maximumPositionSize": "0",
                    "maximumTrailingStopDistance": "10000.0"
                },
            ],
            "lastTransactionID": "2124"
        },
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
