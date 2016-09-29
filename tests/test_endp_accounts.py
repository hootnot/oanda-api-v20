import unittest
import json
from . import unittestsetup
from .unittestsetup import environment as environment

try:
    from nose_parameterized import parameterized
except:
    print("*** Please install 'nose_parameterized' to run these tests ***")
    exit(0)

import oandapyV20 as oandapy
from oandapyV20.exceptions import V20Error
import oandapyV20.endpoints.accounts as accounts

access_token = None
accountID = None
account_cur = None
api = None


class TestAccounts(unittest.TestCase):

    def setUp(self):
        global access_token
        global accountID
        global account_cur
        global api
        # self.maxDiff = None
        try:
            accountID, account_cur, access_token = unittestsetup.auth()
        except Exception as e:
            print("%s" % e)
            exit(0)

        api = oandapy.API(environment=environment, access_token=access_token,
                          headers={"Content-Type": "application/json"})

    def test__get_accounts(self):
        """ get all accounts
            normally a user has at least one account
        """
        r = accounts.AccountList()
        result = api.request(r)
        count = len(result['accounts'])
        self.assertGreaterEqual(count, 1)

    def test__get_account(self):
        """ get account
            the details of specified account
        """
        r = accounts.AccountDetails(accountID=accountID)
        result = api.request(r)
        s_result = json.dumps(result)
        self.assertTrue(accountID in s_result)

    @parameterized.expand([
                       (None, ),
                       ("X", "Account does not exist"),
                         ])
    def test__get_account_summary(self, accID, fail=None):
        """ get account
            the summary of specified account
        """
        if not accID:
            # hack to use the global accountID
            accID = accountID
        r = accounts.AccountSummary(accountID=accID)
        if fail:
            # The test should raise an exception with code == fail
            oErr = None
            with self.assertRaises(V20Error) as oErr:
                result = api.request(r)
                s = "{}".format(oErr)
                self.assertTrue(fail in s)
        else:
            result = api.request(r)
            self.assertTrue(result["account"]["id"] == accountID and
                            result["account"]["currency"] == account_cur)

    @parameterized.expand([
                       (None, "gt", 0),
                       ("DE30_EUR,EUR_USD", "eq", 2),
                       ("EURJPY,EUR_USD", "eq", 2, "Invalid value specified")
                         ])
    def test__get_account_instruments_1(self, instr, f, cnt, fail=None):
        """ get account
            the instruments of specified account
        """
        params = None
        if instr:
            params = {"instruments": instr}
        r = accounts.AccountInstruments(accountID=accountID, params=params)

        result = None
        if fail:
            # The test should raise an exception with code == fail
            oErr = None
            with self.assertRaises(V20Error) as oErr:
                result = api.request(r)
                s = "{}".format(oErr)
                self.assertTrue(fail in s)

        else:
            result = api.request(r)

            if f == "gt":
                self.assertTrue(len(result["instruments"]) > cnt)
            elif f == "eq":
                self.assertTrue(len(result["instruments"]) == cnt)

    @parameterized.expand([
                       (None, "0.1"),
                       (None, "0.05"),
                       ("X", "0.05", "Account does not exist"),
                         ])
    def test__account_configuration(self, accID, marginRate, fail=None):
        """account configuration tests."""
        if not accID:
            accID = accountID

        config = {"marginRate": marginRate}
        r = accounts.AccountConfiguration(accountID=accID, data=config)

        result = None
        if fail:
            # The test should raise an exception with code == fail
            oErr = None
            with self.assertRaises(V20Error) as oErr:
                result = api.request(r)
                s = "{}".format(oErr)
                self.assertTrue(fail in s)

        else:
            result = api.request(r)
            newRate = result["clientConfigureTransaction"]["marginRate"]
            self.assertTrue(newRate == marginRate)

if __name__ == "__main__":

    unittest.main()
