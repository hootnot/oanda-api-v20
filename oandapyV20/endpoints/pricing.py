"""Handle pricing endpoints."""
from .apirequest import APIRequest


class Pricing(APIRequest):
    """Pricing - class to handle pricing endpoint."""

    ENDPOINT = "v3/accounts/{accountID}/pricing"

    def __init__(self, accountID):
        """Instantiate a Pricing APIRequest instance.

        Parameters
        ----------
        accountID : string (required)
            the accountID of the account. 
        """
        endpoint = self.ENDPOINT.format(accountID=accountID)

        super(Pricing, self).__init__(endpoint)
