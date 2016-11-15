# -*- coding: utf-8 -*-
"""Handle instruments endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint
from .responses.instruments import responses
from abc import abstractmethod


class Instruments(APIRequest):
    """Instruments - abstract class to handle instruments endpoint."""

    ENDPOINT = ""
    METHOD = "GET"

    @abstractmethod
    @dyndoc_insert(responses)
    def __init__(self, instrument):
        """Instantiate a Instrument APIRequest instance.

        Parameters
        ----------
        instrument : string (required)
            the instrument to operate on

        params : dict with query parameters
        """
        endpoint = self.ENDPOINT.format(instrument=instrument)
        super(Instruments, self).__init__(endpoint, method=self.METHOD)


@endpoint("v3/instruments/{instrument}/candles")
class InstrumentsCandles(Instruments):
    """Get candle data for a specified Instrument."""

    @dyndoc_insert(responses)
    def __init__(self, instrument, params=None):
        """Instantiate an InstrumentsCandles request.

        Parameters
        ----------
        instrument : string (required)
            the instrument to fetch candle data for

        params : dict
            optional request query parameters, check developer.oanda.com
            for details


        Params example::

            {_v3_instruments_instrument_candles_params}


        Candle data example::

        >>> import oandapyV20
        >>> import oandapyV20.endpoints.instruments as instruments
        >>> client = oandapyV20.API(access_token=...)
        >>> params = ...
        >>> r = instruments.InstrumentsCandles(instrument="DE30_EUR",
        >>>                                    params=params)
        >>> client.request(r)
        >>> print r.response


        Output::

            {_v3_instruments_instrument_candles_resp}

        """
        super(InstrumentsCandles, self).__init__(instrument)
        self.params = params
