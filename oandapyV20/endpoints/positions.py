"""Handle position endpoints."""
from .apirequest import APIRequest


class OpenPositions(APIRequest):
    """OpenPositions - class to handle the 'openPositions' endpoint."""

    ENDPOINT = "/v3/accounts/{}/openPositions"

    def __init__(self, account_id):
        """Instantiate an OpenPositions APIRequest instance.

        Parameters
        ----------
        account_id : string
            the account_id of the account.
        """
        endpoint = self.ENDPOINT.format(account_id)
        super(OpenPositions, self).__init__(endpoint)


class Positions(APIRequest):
    """Positions - class to handle the 'positions' endpoint."""

    ENDPOINT = "/v3/accounts/{}/positions"

    def __init__(self, account_id,
                 subject=None, instrument=None, configuration=None):
        """Instantiate a Positions APIRequest instance.

        Parameters
        ----------
        account_id : string
            the account_id of the account.

        subject : string
            static final part of the endpoint defining the details of the
            request.

        instrument : string

        configuration : dict (optional)
            configuration details in case of a PUT request.
        """
        endpoint = self.ENDPOINT.format(account_id)
        if instrument:
            endpoint = '{}/{}'.format(endpoint, instrument)

        if subject:
            endpoint = '{}/{}'.format(endpoint, subject)

        super(Positions, self).__init__(endpoint)

        self.body = configuration
        if configuration or subject is "close":
            self.method = "PUT"
