import sys
import unittest
import json
from . import unittestsetup
from .unittestsetup import environment as environment
from .unittestsetup import fetchTestData
import requests_mock


try:
    from nose_parameterized import parameterized
except:
    print("*** Please install 'nose_parameterized' to run these tests ***")
    exit(0)

import oandapyV20
from oandapyV20 import API
from oandapyV20.exceptions import V20Error
import oandapyV20.endpoints.trades as trades
from oandapyV20.endpoints.trades import responses

access_token = None
accountID = None
account_cur = None
api = None


class TestTrades(unittest.TestCase):
    """Tests regarding the trades endpoints."""

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
            api = API(environment=environment, access_token=access_token)
            api.api_url = 'https://test.com'
        except Exception as e:
            print("%s" % e)
            exit(0)

    def test__trades_base_exception(self):
        """test for the exception when using the baseclass."""
        with self.assertRaises(TypeError) as bcErr:
            r = trades.Trades(accountID)

        bcErr = bcErr.exception
        self.assertTrue("Use of abstract base class" in "{}".format(bcErr))

    @requests_mock.Mocker()
    def test__trades_list(self, mock_get):
        """get the trades information for an account."""
        tid = "_v3_accounts_accountID_trades"
        resp, data, params = fetchTestData(responses, tid)
        r = trades.TradesList(accountID, params=params)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__open_trades(self, mock_get):
        """get the open trades information for an account."""
        tid = "_v3_accounts_accountID_opentrades"
        resp, data = fetchTestData(responses, tid)
        r = trades.OpenTrades(accountID)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__trade_details(self, mock_get):
        """get the trade details for a trade."""
        tid = "_v3_account_accountID_trades_details"
        resp, data = fetchTestData(responses, tid)
        r = trades.TradeDetails(accountID, tradeID=2315)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__trade_close(self, mock_put):
        """close trade by id ."""
        tid = "_v3_account_accountID_trades_close"
        resp, data = fetchTestData(responses, tid)
        r = trades.TradeClose(accountID, tradeID=2315)
        mock_put.register_uri('PUT',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__trade_cltext(self, mock_put):
        """trade client extensions."""
        tid = "_v3_account_accountID_trades_cltext"
        resp, data = fetchTestData(responses, tid)
        r = trades.TradeClientExtensions(accountID, tradeID=2315, data=data)
        mock_put.register_uri('PUT',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__trades_list_byids(self, mock_get):
        """get the trades information for an account."""
        uri = 'https://test.com/v3/accounts/{}/trades'.format(accountID)
        resp = responses["_v3_accounts_accountID_trades"]['response']
        text = json.dumps(resp)
        mock_get.register_uri('GET',
                              uri,
                              text=text)
        params = {"ids": "2121, 2123"}
        r = trades.TradesList(accountID, params=params)
        result = api.request(r)
        self.assertTrue(len(result['trades']) == 2 and
                        result['trades'][0]['instrument'] == "DE30_EUR")


if __name__ == "__main__":

    unittest.main()
