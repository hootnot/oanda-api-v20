"""Handle pricing endpoints."""
from .apirequest import APIRequest


class Pricing(APIRequest):
    """Pricing - class to handle pricing endpoint."""

    ENDPOINT = "/v3/accounts/{}/pricing"

    def __init__(self, account_id):
        """Instantiate a Pricing APIRequest instance.

        Parameters
        ----------
        account_id : string (optional)
            the account_id of the account. Optional when requesting
            all accounts. For all other requests to endpoint it is
            required.
        """
        endpoint = self.ENDPOINT.format(account_id)

        super(Pricing, self).__init__(endpoint)
