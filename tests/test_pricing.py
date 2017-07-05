import sys
import unittest
import json
from . import unittestsetup
from .unittestsetup import environment as environment
from .unittestsetup import fetchTestData
import requests_mock


from oandapyV20 import API
from oandapyV20.exceptions import StreamTerminated
import oandapyV20.endpoints.pricing as pricing
from oandapyV20.endpoints.pricing import responses

access_token = None
accountID = None
account_cur = None
api = None


class TestPricing(unittest.TestCase):
    """Tests regarding the pricing endpoints."""

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
            api.api_url = 'https://test.com'
        except Exception as e:
            print("%s" % e)
            exit(0)

    @requests_mock.Mocker()
    def test__pricing(self, mock_get):
        """get the pricing information for instruments."""
        tid = "_v3_accounts_accountID_pricing"
        resp, data, params = fetchTestData(responses, tid)
        r = pricing.PricingInfo(accountID, params=params)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        instr = params["instruments"].split(",")
        self.assertTrue(result["prices"][0]["instrument"] == instr[0] and
                        result["prices"][1]["instrument"] == instr[1])

    @requests_mock.Mocker()
    def test__pricing_stream(self, mock_get):
        """get the streaming pricing information for instruments."""
        tid = "_v3_accounts_accountID_pricing_stream"
        resp, data, params = fetchTestData(responses, tid)
        text = "\n".join([json.dumps(t) for t in resp])
        r = pricing.PricingStream(accountID, params=params)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=text)
        result = []
        n = 0
        m = 3
        with self.assertRaises(StreamTerminated):
            for rec in api.request(r):
                result.append(rec)
                n += 1
                # terminate when we have m response lines
                if n == m:
                    r.terminate()

        # the result containing m items, should equal the first m items
        self.assertTrue(result == resp[0:m])

    def test__pricing_stream_termination_1(self):
        """terminate a stream that does not exist."""
        params = {"instruments": "EUR_USD,EUR_JPY"}
        r = pricing.PricingStream(accountID, params=params)
        with self.assertRaises(ValueError):
            r.terminate()

if __name__ == "__main__":

    unittest.main()
