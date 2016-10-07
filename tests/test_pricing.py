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
                      access_token=access_token,
                      headers={"Content-Type": "application/json"})
        except Exception as e:
            print("%s" % e)
            exit(0)

    @requests_mock.Mocker()
    def test__pricing(self, mock_get):
        """get the pricing information for instruments."""
        uri = 'https://test.com/v3/accounts/{}/pricing'.format(accountID)
        resp = responses["_v3_accounts_accountID_pricing"]['response']
        text = json.dumps(resp)
        mock_get.register_uri('GET',
                              uri,
                              text=text)
        params = {"instruments": "EUR_USD,EUR_JPY"}
        r = pricing.PricingInfo(accountID, params=params)
        result = api.request(r)
        s_result = json.dumps(result)
        self.assertTrue("EUR_USD" in s_result and "EUR_JPY" in s_result)

    @requests_mock.Mocker()
    def test__pricing_stream(self, mock_get):
        """get the pricing information for instruments."""
        uri = 'https://test.com/v3/accounts/{}/pricing/stream'.format(accountID)
        resp = responses["_v3_accounts_accountID_pricing"]['response']
        resp = {"a": 10}
        text = json.dumps(resp)
        mock_get.register_uri('GET',
                              uri,
                              text=text)
        params = {"instruments": "EUR_USD,EUR_JPY"}
        r = pricing.PricingStream(accountID, params=params)
        result = []
        for r in api.request(r):
            result.append(r)
        self.assertTrue(result[0] == resp)


if __name__ == "__main__":

    unittest.main()
