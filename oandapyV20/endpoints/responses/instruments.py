"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement
"""
responses = {
    "_v3_instruments_instrument_candles": {
        "url": "/v3/instruments/{instrument}/candles",
        "instrument": "DE30_EUR",
        "params": {
            "count": 5,
            "granularity": "M5"
        },
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
