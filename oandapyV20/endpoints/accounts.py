"""Handle account endpoints."""
from .apirequest import APIRequest


class Accounts(APIRequest):
    """Accounts - class to handle the /v3/accounts endpoint."""

    ENDPOINT = "/v3/accounts"

    def __init__(self, account_id=None, subject=None, configuration=None):
        """Instantiate an Accounts APIRequest instance.

        Parameters
        ----------
        account_id : string (optional)
            the account_id of the account. Optional when requesting
            all accounts. For all other requests to endpoint it is
            required.

        subject : string 
            static final part of the endpoint defining the details of the
            request.

        configuration : dict (optional)
            configuration details for the account in case of a PATCH request.
        """

        endpoint = self.ENDPOINT
        method = "GET"
        if account_id:
            endpoint = "{}/{}".format(endpoint, account_id)

            if subject:
                endpoint = "{}/{}".format(endpoint, subject)
                if subject == "configuration":
                    method = "PATCH"

        super(Accounts, self).__init__(endpoint,
                                       method=method,
                                       body=configuration)
