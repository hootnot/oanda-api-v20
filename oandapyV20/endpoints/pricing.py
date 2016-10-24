# -*- encoding: utf-8 -*-
"""Handle pricing endpoints."""
from .apirequest import APIRequest
from ..exceptions import StreamTerminated
from .decorators import dyndoc_insert, endpoint, abstractclass, extendargs
from .definitions.pricing import definitions    # flake8: noqa
from .responses.pricing import responses
from types import GeneratorType


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

    def terminate(self, message=""):
        if not isinstance(self.response, GeneratorType):
            raise ValueError("request does not contain a stream response")

        self.response.throw(StreamTerminated(message))
