# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
import unittest
from . import unittestsetup
from .unittestsetup import environment as environment

try:
    from nose_parameterized import parameterized
except:
    print("*** Please install 'nose_parameterized' to run these tests ***")
    exit(0)

import oandapyV20 as oandapy
import oandapyV20.endpoints.pricing as pricing

access_token = None
account_id = None
account_cur = None
api = None


class TestAccounts(unittest.TestCase):

    def setUp(self):
        global access_token
        global account_id
        global account_cur
        global api
        # self.maxDiff = None
        try:
            account_id, account_cur, access_token = unittestsetup.auth()
        except Exception as e:
            print("{}".format(e))
            exit(0)

        api = oandapy.API(environment=environment, access_token=access_token,
                          headers={"Content-Type": "application/json"})

    @parameterized.expand([
                           ("DE30_EUR,EUR_GBP,EUR_USD,EUR_JPY"),
                           ("DE30EUR,EUR_GBP", True)
                          ])
    def test__pricing(self, instruments, fail=False):

        r = pricing.Pricing(account_id)
        result = api.request(r, params={"instruments": instruments})
        count = len(result['prices'])
        f = result['prices'][0]
        # status strings allowed in the response
        status = ["tradeable", "non-tradeable"]
        if fail:
            status.append("invalid")

        self.assertTrue(count == len(instruments.split(",")) and
                        f['status'] in status)


if __name__ == "__main__":

    unittest.main()
