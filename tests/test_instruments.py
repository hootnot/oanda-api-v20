import sys
import unittest
import json
from . import unittestsetup
from .unittestsetup import environment as environment
import requests_mock


try:
    from nose_parameterized import parameterized
except:
    print("*** Please install 'nose_parameterized' to run these tests ***")
    exit(0)

import oandapyV20
from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.instruments import responses
import oandapyV20.endpoints.instruments as instruments

access_token = None
accountID = None
account_cur = None
api = None


class TestInstruments(unittest.TestCase):
    """Tests regarding the instruments endpoints."""

    def setUp(self):
        """setup for all tests."""
        global access_token
        global accountID
        global account_cur
        global api
        # self.maxDiff = None
        try:
            accountID, account_cur, access_token = unittestsetup.auth()
            setattr(sys.modules["oandapyV20.oandapyV20"],
                    "TRADING_ENVIRONMENTS",
                    {"practice": {
                     "stream": "https://test.com",
                     "api": "https://test.com",
                     }})
            api = API(environment=environment,
                      access_token=access_token,
                      headers={"Content-Type": "application/json"})
        except Exception as e:
            print("%s" % e)
            exit(0)

    @requests_mock.Mocker()
    def test__instruments_candles(self, mock_get):
        """get the candle information for instruments."""
        instrument = "DE30_EUR"
        uri = 'https://test.com/v3/instruments/{}/candles'.format(instrument)
        resp = responses["_v3_instruments_instrument_candles"]['response']
        text = json.dumps(resp)
        mock_get.register_uri('GET',
                              uri,
                              text=text)
        params = {"granularity": "M5",
                  "count": 5}
        r = instruments.InstrumentsCandles(instrument=instrument,
                                           params=params)
        result = api.request(r)
        self.assertTrue(result == resp)


if __name__ == "__main__":

    unittest.main()
