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
            api = API(environment=environment,
                      access_token=access_token,
                      headers={"Content-Type": "application/json"})
            api.api_url = 'https://test.com'
        except Exception as e:
            print("%s" % e)
            exit(0)

    def test__oandapyv20_environment(self):
        """test the exception on a faulty environment."""
        tapi = None
        with self.assertRaises(KeyError) as envErr:
            tapi = API(environment="faulty",
                       access_token=access_token,
                       headers={"Content-Type": "application/json"})

        self.assertTrue("Unknown environment" in "{}".format(envErr.exception))


if __name__ == "__main__":

    unittest.main()
