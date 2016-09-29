"""Handle pricing endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint, abstractclass, params

responses = {}


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
        """
        endpoint = self.ENDPOINT.format(accountID=accountID)
        super(Pricing, self).__init__(endpoint, method=self.METHOD)


@params
@endpoint("v3/accounts/{accountID}/pricing")
class PricingInfo(Pricing):
    """Pricing.

    Get pricing information for a specified list of Instruments within
    an account.
    """
