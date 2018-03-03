import sys
import unittest
import json
from . import unittestsetup
from .unittestsetup import environment as environment
from .unittestsetup import fetchTestData
import requests_mock


from oandapyV20 import API
import oandapyV20.endpoints.forexlabs as labs
from oandapyV20.endpoints.forexlabs import responses

access_token = None
accountID = None
account_cur = None
api = None


class TestForexLabs(unittest.TestCase):
    """Tests regarding the forexlabs endpoints."""

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
            api.api_url = 'https://test.com'
        except Exception as e:
            print("%s" % e)
            exit(0)

    @requests_mock.Mocker()
    def test__calendar(self, mock_get):
        """get the calendar information for an instrument."""
        tid = "_v3_forexlabs_calendar"
        resp, data, params = fetchTestData(responses, tid)
        r = labs.Calendar(params=params)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        api.request(r)
        self.assertTrue(resp == r.response)

    @requests_mock.Mocker()
    def test__histposratios(self, mock_get):
        """get the hist. pos. ratios information for an instrument."""
        tid = "_v3_forexlabs_histposratios"
        resp, data, params = fetchTestData(responses, tid)
        r = labs.HistoricalPositionRatios(params=params)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        api.request(r)
        self.assertTrue(resp == r.response)

    @requests_mock.Mocker()
    def test__spreads(self, mock_get):
        """get the spreads information for an instrument."""
        tid = "_v3_forexlabs_spreads"
        resp, data, params = fetchTestData(responses, tid)
        r = labs.Spreads(params=params)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        api.request(r)
        self.assertTrue(resp == r.response)

    @requests_mock.Mocker()
    def test__commoftrad(self, mock_get):
        """get the commitments of traders information for an instrument."""
        tid = "_v3_forexlabs_commoftrad"
        resp, data, params = fetchTestData(responses, tid)
        r = labs.CommitmentsOfTraders(params=params)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        api.request(r)
        self.assertTrue(resp == r.response)

    @requests_mock.Mocker()
    def test__orderbookdata(self, mock_get):
        """get the orderbookdata information for an instrument."""
        tid = "_v3_forexlabs_orderbookdata"
        resp, data, params = fetchTestData(responses, tid)
        r = labs.OrderbookData(params=params)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        api.request(r)
        self.assertTrue(resp == r.response)

    @requests_mock.Mocker()
    def test__autochartist(self, mock_get):
        """get autochartist information for an instrument."""
        tid = "_v3_forexlabs_autochartist"
        resp, data, params = fetchTestData(responses, tid)
        r = labs.Autochartist(params=params)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        api.request(r)
        self.assertTrue(resp == r.response)
