"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement
"""
responses = {
    "_v3_accounts_accountID_trades": {
        "url": "v3/accounts/{accountID}/trades",
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
    },
    "_v3_accounts_accountID_opentrades": {
        "url": "v3/accounts/{accountID}/openTrades",
        "response": {
            "trades": [
                {
                    "financing": "0.0000",
                    "openTime": "2016-10-28T14:28:05.231759081Z",
                    "price": "10678.3",
                    "unrealizedPL": "136.0000",
                    "realizedPL": "0.0000",
                    "instrument": "DE30_EUR",
                    "state": "OPEN",
                    "initialUnits": "10",
                    "currentUnits": "10",
                    "id": "2315"
                }
            ],
            "lastTransactionID": "2317"
        }
    },
    "_v3_account_accountID_trades_details": {
        # tradeID 2315
        "url": "v3/accounts/{accountID}/trades/{tradeID}",
        "response": {
            "lastTransactionID": "2317",
            "trade": {
                "financing": "0.0000",
                "openTime": "2016-10-28T14:28:05.231759081Z",
                "price": "10678.3",
                "unrealizedPL": "226.0000",
                "realizedPL": "0.0000",
                "instrument": "DE30_EUR",
                "state": "OPEN",
                "initialUnits": "10",
                "currentUnits": "10",
                "id": "2315"
            }
        }
    },
    "_v3_account_accountID_trades_close": {
        "url": "v3/accounts/{accountID}/trades/{tradeID}/close",
        "body": {
            "units": 100
        },
        "response": {
            "orderFillTransaction": {
                "orderID": "2316",
                "financing": "0.0000",
                "instrument": "EUR_USD",
                "price": "1.09289",
                "userID": 1435156,
                "batchID": "2316",
                "accountBalance": "33848.1208",
                "reason": "MARKET_ORDER_TRADE_CLOSE",
                "tradesClosed": [
                    {
                        "units": "-100",
                        "financing": "0.0000",
                        "realizedPL": "-0.1455",
                        "tradeID": "2313"
                    }
                ],
                "time": "2016-10-28T15:11:58.023004583Z",
                "units": "-100",
                "type": "ORDER_FILL",
                "id": "2317",
                "pl": "-0.1455",
                "accountID": "101-004-1435156-001"
            },
            "orderCreateTransaction": {
                "timeInForce": "FOK",
                "positionFill": "REDUCE_ONLY",
                "userID": 1435156,
                "batchID": "2316",
                "instrument": "EUR_USD",
                "reason": "TRADE_CLOSE",
                "tradeClose": {
                    "units": "100",
                    "tradeID": "2313"
                },
                "time": "2016-10-28T15:11:58.023004583Z",
                "units": "-100",
                "type": "MARKET_ORDER",
                "id": "2316",
                "accountID": "101-004-1435156-001"
            },
            "relatedTransactionIDs": [
                "2316",
                "2317"
            ],
            "lastTransactionID": "2317"
        }
    },
    "_v3_account_accountID_trades_cltext": {
        "url": "v3/accounts/{accountID}/trades/{tradeID}/close",
        "body": {
            "clientExtensions": {
                "comment": "myComment",
                "id": "myID2315",
            }
        },
        "response": {
            "tradeClientExtensionsModifyTransaction": {
                "tradeID": "2315",
                "userID": 1435156,
                "batchID": "2319",
                "time": "2016-10-28T20:32:39.356516787Z",
                "tradeClientExtensionsModify": {
                    "comment": "myComment",
                    "id": "myID2315"
                },
                "type": "TRADE_CLIENT_EXTENSIONS_MODIFY",
                "id": "2319",
                "accountID": "101-004-1435156-001"
            },
            "relatedTransactionIDs": [
                "2319"
            ],
            "lastTransactionID": "2319"
        }
    },
    "_v3_account_accountID_trades_crcdo": {
        "url": "v3/accounts/{accountID}/trades/{tradeID}/close",
        "body": {
            "takeProfit": {
                "timeInForce": "GTC",
                "price": "1.05"
            },
            "stopLoss": {
                "timeInForce": "GTC",
                "price": "1.10"
            }
        },
        "response": {
            "stopLossOrderTransaction": {
                "timeInForce": "GTC",
                "triggerCondition": "TRIGGER_DEFAULT",
                "replacesOrderID": "2324",
                "tradeID": "2323",
                "price": "1.10000",
                "userID": 1435156,
                "batchID": "2325",
                "reason": "REPLACEMENT",
                "time": "2016-10-28T21:00:19.978476830Z",
                "cancellingTransactionID": "2326",
                "type": "STOP_LOSS_ORDER",
                "id": "2327",
                "accountID": "101-004-1435156-001"
            },
            "takeProfitOrderTransaction": {
                "timeInForce": "GTC",
                "triggerCondition": "TRIGGER_DEFAULT",
                "tradeID": "2323",
                "price": "1.05000",
                "userID": 1435156,
                "batchID": "2325",
                "reason": "CLIENT_ORDER",
                "time": "2016-10-28T21:00:19.978476830Z",
                "type": "TAKE_PROFIT_ORDER",
                "id": "2325",
                "accountID": "101-004-1435156-001"
            },
            "relatedTransactionIDs": [
                "2325",
                "2326",
                "2327"
            ],
            "lastTransactionID": "2327",
            "stopLossOrderCancelTransaction": {
                "orderID": "2324",
                "replacedByOrderID": "2327",
                "userID": 1435156,
                "batchID": "2325",
                "reason": "CLIENT_REQUEST_REPLACED",
                "time": "2016-10-28T21:00:19.978476830Z",
                "type": "ORDER_CANCEL",
                "id": "2326",
                "accountID": "101-004-1435156-001"
            }
        }
    }
}
