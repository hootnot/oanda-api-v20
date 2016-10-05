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
import oandapyV20.endpoints.orders as orders
from oandapyV20.endpoints.orders import responses

access_token = None
accountID = None
account_cur = None
api = None


class TestOrders(unittest.TestCase):
    """Tests regarding the orders endpoints."""

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

    def test__orders_base_exception(self):
        """test for the exception when using the baseclass."""
        with self.assertRaises(TypeError) as bcErr:
            r = orders.Orders(accountID)

        bcErr = bcErr.exception
        self.assertTrue("Use of abstract base class" in "{}".format(bcErr))

    @requests_mock.Mocker()
    def test__orders_list(self, mock_get):
        """get the orders information for an account."""
        uri = 'https://test.com/v3/accounts/{}/orders'.format(accountID)
        resp = responses["_v3_accounts_accountID_orders"]['response']
        text = json.dumps(resp)
        mock_get.register_uri('GET',
                              uri,
                              text=text)
        r = orders.OrderList(accountID)
        result = api.request(r)
        self.assertTrue(len(result['orders']) == 1 and
                        result['orders'][0]['instrument'] == "EUR_USD")

    @requests_mock.Mocker()
    def test__order_replace(self, mock_get):
        """test replacing an order."""
        orderID = "2125"
        # to replace with
        tmp = {"order": {
                   "units": "-50000",
                   "type": "LIMIT",
                   "instrument": "EUR_USD",
                   "price": "1.25",
                }
               }

        uri = 'https://test.com/v3/accounts/{}/orders/{}'.format(accountID,
                                                                 orderID)
        resp = responses["_v3_accounts_accountID_order_replace"]['response']
        text = json.dumps(resp)
        mock_get.register_uri('PUT',
                              uri,
                              text=text)
        r = orders.OrderReplace(accountID, orderID, data=tmp)
        result = api.request(r)
        self.assertTrue(len(result['orders']) == 1 and
                        result['orders'][0]['units'] == tmp["order"]["units"])


if __name__ == "__main__":

    unittest.main()
