# -*- coding: utf-8 -*-
"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement
"""
responses = {
    "_v3_accounts_accountID_orders_create": {
        "url": "v3/accounts/{accountID}/orders",
        "body": {
                "order": {
                    "stopLossOnFill": {
                        "timeInForce": "GTC",
                        "price": "1.22"
                    },
                    "units": "-100",
                    "price": "1.2",
                    "instrument": "EUR_USD",
                    "timeInForce": "GTC",
                    "type": "LIMIT",
                    "positionFill": "DEFAULT"
                }
        },
        "response": {
            "orderCreateTransaction": {
                "timeInForce": "GTC",
                "triggerCondition": "TRIGGER_DEFAULT",
                "positionFill": "DEFAULT",
                "stopLossOnFill": {
                    "timeInForce": "GTC",
                    "price": "1.22000"
                },
                "userID": 1435156,
                "id": "2304",
                "batchID": "2304",
                "instrument": "EUR_USD",
                "reason": "CLIENT_ORDER",
                "time": "2016-10-24T21:48:18.593753865Z",
                "units": "-100",
                "type": "LIMIT_ORDER",
                "price": "1.20000",
                "accountID": "101-004-1435156-001"
            },
            "relatedTransactionIDs": [
                "2304"
            ],
            "lastTransactionID": "2304"
        }
    },
    "_v3_accounts_accountID_orders_pending": {
        "url": "v3/accounts/{accountID}/orders",
        "response": {
            "orders": [
                {
                    "timeInForce": "GTC",
                    "triggerCondition": "TRIGGER_DEFAULT",
                    "partialFill": "DEFAULT_FILL",
                    "positionFill": "POSITION_DEFAULT",
                    "stopLossOnFill": {
                        "timeInForce": "GTC",
                        "price": "1.22000"
                    },
                    "id": "2304",
                    "price": "1.20000",
                    "instrument": "EUR_USD",
                    "state": "PENDING",
                    "units": "-100",
                    "clientExtensions": {
                        "comment": "myComment",
                        "id": "myID"
                    },
                    "type": "LIMIT",
                    "createTime": "2016-10-24T21:48:18.593753865Z"
                }
            ],
            "lastTransactionID": "2305"
        }
    },
    "_v3_accounts_accountID_order_cancel": {
        "url": "v3/accounts/{accountID}/orders/{orderID}/cancel",
        "orderID": "2307",
        "response": {
            "orderCancelTransaction": {
                "orderID": "2307",
                "clientOrderID": "myID",
                "userID": 1435156,
                "batchID": "2308",
                "reason": "CLIENT_REQUEST",
                "time": "2016-10-25T20:53:03.789670387Z",
                "type": "ORDER_CANCEL",
                "id": "2308",
                "accountID": "101-004-1435156-001"
            },
            "relatedTransactionIDs": [
                "2308"
            ],
            "lastTransactionID": "2308"
        }
    },
    "_v3_accounts_accountID_orders_list": {
        "url": "v3/accounts/{accountID}/orders",
        "response": {
            "orders": [
                {
                    "triggerCondition": "TRIGGER_DEFAULT",
                    "partialFill": "DEFAULT_FILL",
                    "price": "1.20000",
                    "stopLossOnFill": {
                        "timeInForce": "GTC",
                        "price": "1.22000"
                    },
                    "createTime": "2016-10-05T10:25:47.627003645Z",
                    "timeInForce": "GTC",
                    "instrument": "EUR_USD",
                    "state": "PENDING",
                    "units": "-100",
                    "id": "2125",
                    "type": "LIMIT",
                    "positionFill": "POSITION_DEFAULT"
                }
            ],
            "lastTransactionID": "2129"
        }
    },
    "_v3_accounts_accountID_order_details": {
        "url": "v3/accounts/{accountID}/orders/{orderID}/details",
        "orderID": "2309",
        "response": {
            "order": {
                "triggerCondition": "TRIGGER_DEFAULT",
                "partialFill": "DEFAULT_FILL",
                "price": "1.20000",
                "stopLossOnFill": {
                    "timeInForce": "GTC",
                    "price": "1.22000"
                },
                "createTime": "2016-10-25T21:07:21.065554321Z",
                "timeInForce": "GTC",
                "instrument": "EUR_USD",
                "state": "PENDING",
                "units": "-100",
                "id": "2309",
                "type": "LIMIT",
                "positionFill": "POSITION_DEFAULT"
            },
            "lastTransactionID": "2309"
        }
    },
    "_v3_accounts_accountID_order_replace": {
        "url": "v3/accounts/{accountID}/orders",
        "body": {
            "order": {
                "units": "-500000",
                "type": "LIMIT",
                "instrument": "EUR_USD",
                "price": "1.25000",
            }
        },
        "response": {
                "orderCreateTransaction": {
                    "timeInForce": "GTC",
                    "triggerCondition": "TRIGGER_DEFAULT",
                    "replacesOrderID": "2304",
                    "positionFill": "DEFAULT",
                    "userID": 1435156,
                    "units": "-500000",
                    "batchID": "2306",
                    "instrument": "EUR_USD",
                    "reason": "REPLACEMENT",
                    "time": "2016-10-25T19:45:38.558056359Z",
                    "price": "1.25000",
                    "clientExtensions": {
                        "comment": "myComment",
                        "id": "myID"
                    },
                    "type": "LIMIT_ORDER",
                    "id": "2307",
                    "accountID": "101-004-1435156-001"
                },
                "orderCancelTransaction": {
                    "orderID": "2304",
                    "clientOrderID": "myID",
                    "replacedByOrderID": "2307",
                    "userID": 1435156,
                    "batchID": "2306",
                    "reason": "CLIENT_REQUEST_REPLACED",
                    "time": "2016-10-25T19:45:38.558056359Z",
                    "type": "ORDER_CANCEL",
                    "id": "2306",
                    "accountID": "101-004-1435156-001"
                },
                "relatedTransactionIDs": [
                    "2306",
                    "2307"
                ],
                "lastTransactionID": "2307"
        }
    },
    "_v3_accounts_accountID_order_clientextensions": {
        "url": "v3/accounts/{accountID}/orders/{orderID}/clientExtensions",
        "orderID": 2304,
        "body": {
            "clientExtensions": {
                "id": "myID",
                "comment": "myComment",
            }
        },
        "response": {
            "relatedTransactionIDs": [
                "2305"
            ],
            "orderClientExtensionsModifyTransaction": {
                "orderID": "2304",
                "userID": 1435156,
                "batchID": "2305",
                "clientExtensionsModify": {
                    "comment": "myComment",
                    "id": "myID"
                },
                "time": "2016-10-25T15:56:43.075594239Z",
                "type": "ORDER_CLIENT_EXTENSIONS_MODIFY",
                "id": "2305",
                "accountID": "101-004-1435156-001"
            },
            "lastTransactionID": "2305"
        }
    }
}
