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
import oandapyV20.endpoints.accounts as accounts
from oandapyV20.endpoints.accounts import responses
from oandapyV20.endpoints.definitions import primitives

access_token = None
accountID = None
account_cur = None
api = None


class TestAccounts(unittest.TestCase):
    """Tests regarding the accounts endpoints."""

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
    def test__get_accounts(self, mock_get):
        """get the list of accounts."""
        text = json.dumps(responses["_v3_accounts"]['response'])
        mock_get.register_uri('GET',
                              'https://test.com/v3/accounts',
                              text=text)
        r = accounts.AccountList()
        result = api.request(r)
        count = len(result['accounts'])
        self.assertGreaterEqual(count, 1)

    @requests_mock.Mocker()
    def test__get_account(self, mock_get):
        """get the details of specified account."""
        uri = 'https://test.com/v3/accounts/{}'.format(accountID)
        text = json.dumps(responses["_v3_account_by_accountID"]['response'])
        mock_get.register_uri('GET', uri, text=text)
        r = accounts.AccountDetails(accountID=accountID)
        result = api.request(r)
        s_result = json.dumps(result)
        self.assertTrue(accountID in s_result)

    @parameterized.expand([
                       (None, 200),
                       ("X", 404, "Account does not exist"),
                         ])
    @requests_mock.Mocker(kw='mock')
    def test__get_account_summary(self, accID, status_code,
                                  fail=None, **kwargs):
        """get the summary of specified account."""
        tid = "_v3_account_by_accountID_summary"
        resp, data = fetchTestData(responses, tid)
        if not accID:
            # hack to use the global accountID
            accID = accountID
        r = accounts.AccountSummary(accountID=accID)
        text = fail
        if not fail:
            text = json.dumps(resp)

        kwargs['mock'].register_uri('GET',
                                    "{}/{}".format(api.api_url, r),
                                    text=text,
                                    status_code=status_code)

        if fail:
            # The test should raise an exception with code == fail
            oErr = None
            with self.assertRaises(V20Error) as oErr:
                result = api.request(r)

            self.assertTrue(fail in "{}".format(oErr.exception))
        else:
            result = api.request(r)
            self.assertTrue(result["account"]["id"] == accountID and
                            result["account"]["currency"] == account_cur)

    @requests_mock.Mocker()
    def test__get_instruments(self, mock_get):
        """get the instruments of specified account."""
        uri = 'https://test.com/v3/accounts/{}/instruments'.format(accountID)
        respKey = "_v3_account_by_accountID_instruments"
        text = json.dumps(responses[respKey]['response'])
        mock_get.register_uri('GET', uri, text=text)
        r = accounts.AccountInstruments(accountID=accountID)
        result = api.request(r)
        dax = None
        for instr in result["instruments"]:
            if instr["name"] == "DE30_EUR":
                dax = instr
                break

        s_result = json.dumps(result)
        primDev = primitives.definitions["InstrumentType"][dax["type"]]
        self.assertTrue(
            dax is not None and
            dax["type"] == "CFD" and
            primDev == "Contract For Difference" and
            "EUR_AUD" not in s_result)

    @requests_mock.Mocker()
    def test__account_configuration(self, mock_req):
        """set configurable parts of account."""
        tid = "_v3_accounts_accountID_account_config"
        resp, data = fetchTestData(responses, tid)
        r = accounts.AccountConfiguration(accountID=accountID, data=data)
        mock_req.register_uri('PATCH',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__account_changes(self, mock_get):
        """get account state since ID of transaction."""
        tid = "_v3_accounts_accountID_account_changes"
        resp, data, params = fetchTestData(responses, tid)
        r = accounts.AccountChanges(accountID=accountID, params=params)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(result == resp)

    def test__get_instruments_data_exception(self):
        """check for data parameter exception."""
        with self.assertRaises(TypeError) as oErr:
            r = accounts.AccountInstruments(accountID=accountID, data={})

        self.assertEqual("__init__() got an unexpected keyword "
                         "argument 'data'", "{}".format(oErr.exception))

    def test__get_instruments_params_exception(self):
        """check for params parameter exception."""
        with self.assertRaises(TypeError) as oErr:
            r = accounts.AccountConfiguration(accountID=accountID, params={})

        self.assertEqual("__init__() got an unexpected keyword "
                         "argument 'params'", "{}".format(oErr.exception))

if __name__ == "__main__":

    unittest.main()
