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
            api = API(environment=environment,
                      access_token=access_token,
                      headers={"Content-Type": "application/json"})
            api.api_url = 'https://test.com'
        except Exception as e:
            print("%s" % e)
            exit(0)

    @requests_mock.Mocker()
    def test__pricing(self, mock_get):
        """get the pricing information for instruments."""
        uri = 'https://test.com/v3/accounts/{}/pricing'.format(accountID)
        resp = responses["_v3_account_accountID_pricing"]['response']
        text = json.dumps(resp)
        mock_get.register_uri('GET',
                              uri,
                              text=text)
        params = {"instruments": "EUR_USD,EUR_JPY"}
        r = pricing.PricingInfo(accountID, params=params)
        result = api.request(r)
        self.assertTrue("EUR_USD" in result and "EUR_JPY" in result)


if __name__ == "__main__":

    unittest.main()
