"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement
"""
responses = {
    "_v3_accounts_accountID_transactions": {
        "url": "v3/accounts/{accountID}/transactions",
        "params": {
            "pageSize": 200
        },
        "response": {
            "count": 2124,
            "from": "2016-06-24T21:03:50.914647476Z",
            "lastTransactionID": "2124",
            "pageSize": 100,
            "to": "2016-10-05T06:54:14.025946546Z",
            "pages": [
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1&to=100",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=101&to=200",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=201&to=300",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=301&to=400",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=401&to=500",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=501&to=600",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=601&to=700",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=701&to=800",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=801&to=900",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=901&to=1000",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1001&to=1100",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1101&to=1200",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1201&to=1300",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1301&to=1400",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1401&to=1500",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1501&to=1600",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1601&to=1700",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1701&to=1800",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1801&to=1900",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=1901&to=2000",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=2001&to=2100",
                "https://api-fxpractice.oanda.com/v3/accounts/"
                "101-004-1435156-001/transactions/idrange?from=2101&to=2124"
            ]
        }
    },
    "_v3_accounts_transaction_details": {
        "url": "v3/accounts/{accountID}/transactions/{transactionID}",
        "response": {
            "transaction": {
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
            "lastTransactionID": "2311"
        }
    }
}
