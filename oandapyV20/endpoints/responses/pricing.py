"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement
"""
responses = {
    "_v3_accounts_accountID_pricing": {
        "url": "v3/accounts/{accountID}/pricing",
        "params": {
            "instruments": "EUR_USD,EUR_JPY"
        },
        "response": {
            "prices": [
                {
                    "status": "tradeable",
                    "quoteHomeConversionFactors": {
                        "negativeUnits": "0.89160730",
                        "positiveUnits": "0.89150397"
                    },
                    "asks": [
                        {
                            "price": "1.12170",
                            "liquidity": 10000000
                        },
                        {
                            "price": "1.12172",
                            "liquidity": 10000000
                        }
                    ],
                    "unitsAvailable": {
                        "default": {
                            "short": "506246",
                            "long": "506128"
                        },
                        "reduceOnly": {
                            "short": "0",
                            "long": "0"
                        },
                        "openOnly": {
                            "short": "506246",
                            "long": "506128"
                        },
                        "reduceFirst": {
                            "short": "506246",
                            "long": "506128"
                        }
                    },
                    "closeoutBid": "1.12153",
                    "bids": [
                        {
                            "price": "1.12157",
                            "liquidity": 10000000
                        },
                        {
                            "price": "1.12155",
                            "liquidity": 10000000
                        }
                    ],
                    "instrument": "EUR_USD",
                    "time": "2016-10-05T05:28:16.729643492Z",
                    "closeoutAsk": "1.12174"
                },
                {
                    "status": "tradeable",
                    "quoteHomeConversionFactors": {
                        "negativeUnits": "0.00867085",
                        "positiveUnits": "0.00866957"
                    },
                    "asks": [
                        {
                            "price": "115.346",
                            "liquidity": 1000000
                        },
                        {
                            "price": "115.347",
                            "liquidity": 2000000
                        },
                        {
                            "price": "115.348",
                            "liquidity": 5000000
                        },
                        {
                            "price": "115.350",
                            "liquidity": 10000000
                        }
                    ],
                    "unitsAvailable": {
                        "default": {
                            "short": "506262",
                            "long": "506112"
                        },
                        "reduceOnly": {
                            "short": "0",
                            "long": "0"
                        },
                        "openOnly": {
                            "short": "506262",
                            "long": "506112"
                        },
                        "reduceFirst": {
                            "short": "506262",
                            "long": "506112"
                        }
                    },
                    "closeoutBid": "115.325",
                    "bids": [
                        {
                            "price": "115.329",
                            "liquidity": 1000000
                        },
                        {
                            "price": "115.328",
                            "liquidity": 2000000
                        },
                        {
                            "price": "115.327",
                            "liquidity": 5000000
                        },
                        {
                            "price": "115.325",
                            "liquidity": 10000000
                        }
                    ],
                    "instrument": "EUR_JPY",
                    "time": "2016-10-05T05:28:15.621238671Z",
                    "closeoutAsk": "115.350"
                }
            ]
        }
    }
}
