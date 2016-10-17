# -*- encoding: utf-8 -*-
"""Handle instruments endpoints."""
from .apirequest import APIRequest
from .decorators import dyndoc_insert, endpoint, abstractclass, extendargs
from .definitions.instruments import definitions    # flake8: noqa

responses = {
    "_v3_instruments_instrument_candles": {
        "url": "/v3/instruments/{instrument}/candles",
        "response": {
            "candles": [
                {
                  "volume": 132,
                  "time": "2016-10-17T19:35:00.000000000Z",
                  "complete": True,
                  "mid": {
                    "h": "10508.0",
                    "c": "10506.0",
                    "l": "10503.8",
                    "o": "10503.8"
                  }
                },
                {
                  "volume": 162,
                  "time": "2016-10-17T19:40:00.000000000Z",
                  "complete": True,
                  "mid": {
                    "h": "10507.0",
                    "c": "10504.9",
                    "l": "10502.0",
                    "o": "10506.0"
                  }
                },
                {
                  "volume": 196,
                  "time": "2016-10-17T19:45:00.000000000Z",
                  "complete": True,
                  "mid": {
                    "h": "10509.8",
                    "c": "10505.0",
                    "l": "10502.6",
                    "o": "10504.9"
                  }
                },
                {
                  "volume": 153,
                  "time": "2016-10-17T19:50:00.000000000Z",
                  "complete": True,
                  "mid": {
                    "h": "10510.1",
                    "c": "10509.0",
                    "l": "10504.2",
                    "o": "10505.0"
                  }
                },
                {
                  "volume": 172,
                  "time": "2016-10-17T19:55:00.000000000Z",
                  "complete": True,
                  "mid": {
                    "h": "10509.8",
                    "c": "10507.8",
                    "l": "10503.2",
                    "o": "10509.0"
                  }
                }
            ],
            "instrument": "DE30/EUR",
            "granularity": "M5"
        }
    }
}


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
