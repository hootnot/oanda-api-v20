"""Handle pricing endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint, abstractclass, extendargs

responses = {
    "_v3_accounts_accountID_pricing": {
        "url": "v3/accounts/{accountID}/pricing",
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


@abstractclass
class Pricing(APIRequest):
    """Pricing - class to handle pricing endpoint."""

    ENDPOINT = ""
    METHOD = "GET"

    @dyndoc_insert(responses)
    def __init__(self, accountID):
        """Instantiate a Pricing APIRequest instance.

        Parameters
        ----------
        accountID : string (required)
            the accountID of the account.

        params : dict (depends on the endpoint to access)
            parameters for the request. This applies only the GET based
            endpoints.
        """
        endpoint = self.ENDPOINT.format(accountID=accountID)
        super(Pricing, self).__init__(endpoint, method=self.METHOD)


@extendargs("params")
@endpoint("v3/accounts/{accountID}/pricing")
class PricingInfo(Pricing):
    """Pricing.

    Get pricing information for a specified list of Instruments within
    an account.
    """


@extendargs("params")
@endpoint("v3/accounts/{accountID}/pricing/stream")
class PricingStream(Pricing):
    """PricingStream.

    Get realtime pricing information for a specified list of Instruments.
    """

    STREAM = True
