# -*- coding: utf-8 -*-
"""Handle pricing endpoints."""
from .apirequest import APIRequest
from ..exceptions import StreamTerminated
from .decorators import dyndoc_insert, endpoint
from .responses.pricing import responses
from types import GeneratorType
from abc import abstractmethod


class Pricing(APIRequest):
    """Pricing - class to handle pricing endpoint."""

    ENDPOINT = ""
    METHOD = "GET"

    @abstractmethod
    def __init__(self, accountID):
        """Instantiate a Pricing APIRequest instance.

        Parameters
        ----------
        accountID : string (required)
            the accountID of the account.

        """
        endpoint = self.ENDPOINT.format(accountID=accountID)
        super(Pricing, self).__init__(endpoint, method=self.METHOD)


@endpoint("v3/accounts/{accountID}/pricing")
class PricingInfo(Pricing):
    """Pricing.

    Get pricing information for a specified list of Instruments within
    an account.
    """

    @dyndoc_insert(responses)
    def __init__(self, accountID, params=None):
        """Instantiate a PricingStream APIRequest instance.

        Parameters
        ----------
        accountID : string (required)
            the accountID of the account.

        params : dict (required)
            parameters for the request, check developer.oanda.com for details.

        Example
        -------

        >>> import oandapyV20
        >>> from oandapyV20 import API
        >>> import oandapyV20.endpoints.pricing as pricing
        >>> accountID = "..."
        >>> api = API(access_token="...")
        >>> params = {_v3_accounts_accountID_pricing_params}
        >>> r = pricing.PricingInfo(accountID=accountID, params=params)
        >>> rv = api.request(r)
        >>> print r.response

        Output::


           {_v3_accounts_accountID_pricing_resp}


        """
        super(PricingInfo, self).__init__(accountID)
        self.params = params


@endpoint("v3/accounts/{accountID}/pricing/stream")
class PricingStream(Pricing):
    """PricingStream.

    Get realtime pricing information for a specified list of Instruments.

    """

    STREAM = True

    @dyndoc_insert(responses)
    def __init__(self, accountID, params=None):
        """Instantiate a PricingStream APIRequest instance.

        Parameters
        ----------
        accountID : string (required)
            the accountID of the account.

        params : dict (required)
            parameters for the request, check developer.oanda.com for details.

        Example
        -------

        >>> import oandapyV20
        >>> from oandapyV20 import API
        >>> import oandapyV20.endpoints.pricing as pricing
        >>> accountID = "..."
        >>> api = API(access_token="...")
        >>> params = {_v3_accounts_accountID_pricing_stream_params}
        >>> r = pricing.PricingStream(accountID=accountID, params=params)
        >>> rv = api.request(r)
        >>> maxrecs = 100
        >>> for ticks in r:
        >>>     print json.dumps(R, indent=4),","
        >>>     if maxrecs == 0:
        >>>         r.terminate("maxrecs records received")

        Output::

           {_v3_accounts_accountID_pricing_stream_ciresp}

        """
        super(PricingStream, self).__init__(accountID)
        self.params = params

    def terminate(self, message=""):
        """terminate the stream.

        Calling this method will stop the generator yielding tickrecords.
        A message can be passed optionally.
        """
        if not isinstance(self.response, GeneratorType):
            raise ValueError("request does not contain a stream response")

        self.response.throw(StreamTerminated(message))
