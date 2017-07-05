import sys
import unittest
import json
from . import unittestsetup
from .unittestsetup import environment as environment
from .unittestsetup import fetchTestData
import requests_mock


from oandapyV20 import API
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

    def test__orders_base_exception(self):
        """test for the exception when using the baseclass."""
        with self.assertRaises(TypeError) as bcErr:
            orders.Orders(accountID)

        bcErr = bcErr.exception
        self.assertTrue("Can't instantiate abstract class Orders "
                        "with abstract methods" in "{}".format(bcErr))

    @requests_mock.Mocker()
    def test__order_create(self, mock_post):
        """order create."""
        tid = "_v3_accounts_accountID_orders_create"
        resp, data = fetchTestData(responses, tid)
        r = orders.OrderCreate(accountID, data=data)
        mock_post.register_uri('POST',
                               "{}/{}".format(api.api_url, r),
                               text=json.dumps(resp),
                               status_code=r.expected_status)
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__order_clientextensions(self, mock_put):
        """set order client extensions."""
        tid = "_v3_accounts_accountID_order_clientextensions"
        resp, data = fetchTestData(responses, tid)
        r = orders.OrderClientExtensions(accountID, orderID="2304", data=data)
        mock_put.register_uri('PUT',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__orders_pending(self, mock_get):
        """get the orders pending for an account."""
        tid = "_v3_accounts_accountID_orders_pending"
        resp, data = fetchTestData(responses, tid)
        r = orders.OrdersPending(accountID)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        result = api.request(r)
        self.assertTrue(result == resp)

    @requests_mock.Mocker()
    def test__orders_list(self, mock_get):
        """get the orders for an account."""
        tid = "_v3_accounts_accountID_orders_list"
        resp, data = fetchTestData(responses, tid)
        r = orders.OrderList(accountID)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(
            len(result['orders']) == len(resp['orders']) and
            result['orders'][0]['instrument'] ==
            resp['orders'][0]['instrument'])

    @requests_mock.Mocker()
    def test__order_details(self, mock_get):
        """details of an order."""
        orderID = "2309"
        tid = "_v3_accounts_accountID_order_details"
        resp, data = fetchTestData(responses, tid)
        r = orders.OrderDetails(accountID, orderID=orderID)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        result = result["order"]
        self.assertTrue(result['id'] == orderID and
                        result['units'] == resp["order"]["units"])

    @requests_mock.Mocker()
    def test__order_cancel(self, mock_get):
        """cancel an order."""
        orderID = "2307"
        tid = "_v3_accounts_accountID_order_cancel"
        resp, data = fetchTestData(responses, tid)
        r = orders.OrderCancel(accountID, orderID=orderID)
        mock_get.register_uri('PUT',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        result = result["orderCancelTransaction"]
        self.assertTrue(result['orderID'] == orderID and
                        result['reason'] == "CLIENT_REQUEST" and
                        result['type'] == "ORDER_CANCEL")

    @requests_mock.Mocker()
    def test__order_replace(self, mock_put):
        """replace an order."""
        orderID = "2304"
        # to replace with data
        tid = "_v3_accounts_accountID_order_replace"
        resp, data = fetchTestData(responses, tid)
        r = orders.OrderReplace(accountID, orderID, data=data)
        mock_put.register_uri('PUT',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp),
                              status_code=r.expected_status)
        result = api.request(r)
        self.assertTrue(
          "orderCreateTransaction" in result and
          "orderCancelTransaction" in result and
          result["orderCancelTransaction"]["orderID"] == orderID and
          result["orderCreateTransaction"]["replacesOrderID"] == orderID and
          result["orderCreateTransaction"]["units"] ==
          data["order"]['units'] and
          result["orderCreateTransaction"]["price"] ==
          data["order"]['price'])

    @requests_mock.Mocker()
    def test__order_replace_wrong_status_exception(self, mock_get):
        """replacing an order with success but wrong status_code."""
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
        r = orders.OrderReplace(accountID, orderID, data=tmp)
        # force the wrong status code
        mock_get.register_uri('PUT',
                              uri,
                              text=text,
                              status_code=200)
        with self.assertRaises(ValueError) as err:
            api.request(r)

        self.assertTrue("200" in "{}".format(err.exception) and
                        r.status_code is None)

if __name__ == "__main__":

    unittest.main()
