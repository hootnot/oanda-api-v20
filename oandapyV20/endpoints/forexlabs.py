"""Handle forexlabs endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint
from .responses.forexlabs import responses
from abc import abstractmethod


class ForexLabs(APIRequest):
    """ForexLabs - abstractbase class to handle the 'forexlabs' endpoints."""

    ENDPOINT = ""
    METHOD = "GET"

    @abstractmethod
    @dyndoc_insert(responses)
    def __init__(self):
        """Instantiate a ForexLabs APIRequest instance."""
        endpoint = self.ENDPOINT.format()
        super(ForexLabs, self).__init__(endpoint,
                                        method=self.METHOD)


@endpoint("labs/v1/calendar")
class Calendar(ForexLabs):
    """Calendar.

    Get calendar information.
    """

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate a Calendar request.

        Parameters
        ----------
        params : dict (required)
            query params to send, check developer.oanda.com for details.


        Query Params example::


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.forexlabs as labs
        >>> accountID = ...
        >>> client = oandapyV20.API(access_token=...)
        >>> params = {_v3_forexlabs_calendar_params}
        >>> r = labs.Calendar(params=params)
        >>> client.request(r)
        >>> print(r.response)

        Output::

            {_v3_forexlabs_calendar_resp}

        """
        super(Calendar, self).__init__()
        self.params = params


@endpoint("labs/v1/historical_position_ratios")
class HistoricalPositionRatios(ForexLabs):
    """HistoricalPositionRatios.

    Get the historical positionratios for an instrument.
    """

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate a HistoricalPositionRatio request.

        Parameters
        ----------
        params : dict (required)
            query params to send, check developer.oanda.com for details.

        >>> import oandapyV20
        >>> import oandapyV20.endpoints.forexlabs as labs
        >>> accountID = ...
        >>> client = oandapyV20.API(access_token=...)
        >>> params = {_v3_forexlabs_histposratios_params}
        >>> r = labs.HistoricalPositionRatios(params=params)
        >>> client.request(r)
        >>> print(r.response)

        Output::

            {_v3_forexlabs_histposratios_resp}

        """
        super(HistoricalPositionRatios, self).__init__()
        self.params = params


@endpoint("labs/v1/spreads")
class Spreads(ForexLabs):
    """Spreads.

    Get the spread information for an instrument.
    """

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate a Spread request.

        Parameters
        ----------
        params : dict (required)
            query params to send, check developer.oanda.com for details.

        >>> import oandapyV20
        >>> import oandapyV20.endpoints.forexlabs as labs
        >>> accountID = ...
        >>> client = oandapyV20.API(access_token=...)
        >>> params = {_v3_forexlabs_spreads_params}
        >>> r = labs.Spreads(params=params)
        >>> client.request(r)
        >>> print(r.response)

        Output::

            {_v3_forexlabs_spreads_resp}

        """
        super(Spreads, self).__init__()
        self.params = params


@endpoint("labs/v1/commitments_of_traders")
class CommitmentsOfTraders(ForexLabs):
    """CommitmentsOfTraders.

    Get the 'commitments of traders' information for an instrument.
    """

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate a CommitmentOfTraders request.

        Parameters
        ----------
        params : dict (required)
            query params to send, check developer.oanda.com for details.


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.forexlabs as labs
        >>> accountID = ...
        >>> client = oandapyV20.API(access_token=...)
        >>> params = {_v3_forexlabs_commoftrad_params}
        >>> r = labs.CommitmentOfTraders(params=params)
        >>> client.request(r)
        >>> print(r.response)

        Output::

            {_v3_forexlabs_commoftrad_resp}

        """
        super(CommitmentsOfTraders, self).__init__()
        self.params = params


@endpoint("labs/v1/orderbook_data")
class OrderbookData(ForexLabs):
    """OrderbookData.

    Get the 'orderbook data' for an instrument.
    """

    @dyndoc_insert(responses)
    def __init__(self, params):
        """Instantiate an OrderbookData request.

        Parameters
        ----------
        params : dict (required)
            query params to send, check developer.oanda.com for details.


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.forexlabs as labs
        >>> accountID = ...
        >>> client = oandapyV20.API(access_token=...)
        >>> params = {_v3_forexlabs_orderbookdata_params}
        >>> r = labs.CommitmentOfTraders(params=params)
        >>> client.request(r)
        >>> print(r.response)

        Output::

            {_v3_forexlabs_orderbookdata_resp}

        """
        super(OrderbookData, self).__init__()
        self.params = params


@endpoint("labs/v1/signal/autochartist")
class Autochartist(ForexLabs):
    """Autochartist.

    Get the 'autochartist data'.
    """

    @dyndoc_insert(responses)
    def __init__(self, params=None):
        """Instantiate an Autochartist request.

        Parameters
        ----------
        params : dict (optional)
            query params to send, check developer.oanda.com for details.


        >>> import oandapyV20
        >>> import oandapyV20.endpoints.forexlabs as labs
        >>> accountID = ...
        >>> client = oandapyV20.API(access_token=...)
        >>> params = {_v3_forexlabs_autochartist_params}
        >>> r = labs.Autochartist(params=params)
        >>> client.request(r)
        >>> print(r.response)

        Output::

            {_v3_forexlabs_autochartist_resp}

        """
        super(Autochartist, self).__init__()
        self.params = params
