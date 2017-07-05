import sys
import unittest
from . import unittestsetup
from .unittestsetup import environment as environment
from oandapyV20 import API

access_token = None
accountID = None
account_cur = None
api = None


class TestOandapyV20(unittest.TestCase):
    """Tests regarding the client."""

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

    def test__oandapyv20_environment(self):
        """test the exception on a faulty environment."""
        with self.assertRaises(KeyError) as envErr:
            API(environment="faulty",
                access_token=access_token,
                headers={"Content-Type": "application/json"})

        self.assertTrue("Unknown environment" in "{}".format(envErr.exception))

    def test__requests_params(self):
        """request parameters."""
        request_params = {"timeout": 10}
        api = API(environment=environment,
                  access_token=access_token,
                  headers={"Content-Type": "application/json"},
                  request_params=request_params)
        self.assertTrue(api.request_params == request_params)

    def test__requests_exception(self):
        """force a requests exception."""
        from requests.exceptions import RequestException
        import oandapyV20.endpoints.accounts as accounts
        setattr(sys.modules["oandapyV20.oandapyV20"],
                "TRADING_ENVIRONMENTS",
                {"practice": {
                 "stream": "ttps://test.com",
                 "api": "ttps://test.com",
                 }})
        api = API(environment=environment,
                  access_token=access_token,
                  headers={"Content-Type": "application/json"})
        text = "No connection " \
               "adapters were found for 'ttps://test.com/v3/accounts'"
        r = accounts.AccountList()
        with self.assertRaises(RequestException) as oErr:
            api.request(r)

        self.assertEqual("{}".format(oErr.exception), text)


if __name__ == "__main__":

    unittest.main()
