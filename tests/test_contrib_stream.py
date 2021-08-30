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
import oandapyV20.endpoints.pricing as pricing
from oandapyV20.contrib.stream import (
    CandleFactory,
    StreamRecord,
    PRICE,
    HEARTBEAT
)

access_token = None
accountID = None
account_cur = None
api = None

TEST_TICKS = "data/test_ticks.txt"
TEST_CANDLES = "data/test_candles.txt"


class TestContribStream(unittest.TestCase):
    """Tests regarding the stream classes."""

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
                      access_token=access_token)
            api.api_url = "https://test.com"
        except Exception as e:
            print("%s" % e)
            exit(0)

    @requests_mock.Mocker()
    def test__streamrecords(self, mock_get):
        """test the streamrecord."""
        params = {"instruments": "EUR_USD"}
        with open(TEST_TICKS) as I:
            resp = I.readlines()
        text = "\n".join([json.dumps(t) for t in resp])
        r = pricing.PricingStream(accountID, params=params)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=text)
        ticksRead = 0
        ticksParsedAndVerified = 0
        # first cycle: test passing string records to StreamRecord
        # second cycle: test passing a dict to StreamRecord
        for cycle in [0, 1]:
            for rec in api.request(r):
                if cycle:
                    rec = json.loads(rec)
                sr = StreamRecord(rec)
                if sr.recordtype == PRICE:
                    ticksRead += 1

                if not isinstance(rec, dict):  # cycle 0
                    rec = json.loads(rec)
                if sr.recordtype == PRICE and \
                   sr.data['bid'] == float(rec.get("closeoutBid")) and \
                   sr.data['ask'] == float(rec.get("closeoutAsk")):
                    ticksParsedAndVerified += 1

        self.assertTrue(ticksRead == ticksParsedAndVerified)

    @requests_mock.Mocker()
    def test__candlefactory(self, mock_get):
        """test the candlefactory."""
        params = {"instruments": "EUR_USD"}
        with open(TEST_TICKS) as I:
            resp = I.readlines()
        text = "\n".join([json.dumps(t) for t in resp])
        r = pricing.PricingStream(accountID, params=params)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=text)
        ticksRead = 0
        ticksParsedAndVerified = 0
        candles = []
        verify = []
        with open(TEST_CANDLES) as I:
            for candle in I:
                verify.append(json.loads(candle))

        cf = CandleFactory([{"EUR_USD": ["M1", "M5"]}])
        for rec in api.request(r):
            sr = StreamRecord(rec)
            for candle in cf.processTick(sr):
                if candle:
                    candles.append(candle)

        self.assertTrue(verify == candles)


if __name__ == "__main__":

    unittest.main()
