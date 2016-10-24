# -*- encoding: utf-8 -*-
"""Handle instruments endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint, abstractclass, extendargs
from .definitions.instruments import definitions    # flake8: noqa
from .responses.instruments import responses


@abstractclass
class Instruments(APIRequest):
    """Instruments - class to handle instruments endpoint."""

    ENDPOINT = ""
    METHOD = "GET"

    @dyndoc_insert(responses)
    def __init__(self, instrument):
        """Instantiate a Instrument APIRequest instance.

        Parameters
        ----------
        instrument : string (required)
            the instrument to fetch candle data for

        params : dict (depends on the endpoint to access)
            parameters for the request. This applies only the GET based
            endpoints.
        """
        endpoint = self.ENDPOINT.format(instrument=instrument)
        super(Instruments, self).__init__(endpoint, method=self.METHOD)


@extendargs("params")
@endpoint("v3/instruments/{instrument}/candles")
class InstrumentsCandles(Instruments):
    """InstrumentsCandles.

    Get candle information for a specified Instrument
    """
