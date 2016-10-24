"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement
"""
responses = {
    "_v3_accounts_accountID_orders": {
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
    "_v3_accounts_accountID_order_replace": {
        "url": "v3/accounts/{accountID}/orders",
        "response": {
            "orders": [
                {
                    "triggerCondition": "TRIGGER_DEFAULT",
                    "replacesOrderID": "2125",
                    "partialFill": "DEFAULT_FILL",
                    "price": "1.25000",
                    "createTime": "2016-10-05T10:52:43.742347417Z",
                    "timeInForce": "GTC",
                    "instrument": "EUR_USD",
                    "state": "PENDING",
                    "units": "-50000",
                    "id": "2133",
                    "type": "LIMIT",
                    "positionFill": "POSITION_DEFAULT"
                }
            ],
            "lastTransactionID": "2133"
        }
    }
}
