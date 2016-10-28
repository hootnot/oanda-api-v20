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
from oandapyV20.exceptions import V20Error, StreamTerminated
import oandapyV20.endpoints.transactions as transactions
from oandapyV20.endpoints.transactions import responses

access_token = None
accountID = None
account_cur = None
api = None


class TestTransactions(unittest.TestCase):
    """Tests regarding the transactions endpoints."""

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
    def test__transactions(self, mock_get):
        """get the transactions information for an account."""
        tid = "_v3_accounts_accountID_transactions"
        resp, data, params = fetchTestData(responses, tid)
        r = transactions.TransactionList(accountID)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(resp == r.response)

    @requests_mock.Mocker()
    def test__transactions_details(self, mock_get):
        """get the transactions details for a transaction."""
        tid = "_v3_accounts_transaction_details"
        resp, data = fetchTestData(responses, tid)
        transactionID = 2304
        r = transactions.TransactionDetails(accountID, transactionID)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(resp == r.response)

    @requests_mock.Mocker()
    def test__transactions_idrange(self, mock_get):
        """get the transactions by an idrange."""
        tid = "_v3_accounts_transaction_idrange"
        resp, data, params = fetchTestData(responses, tid)
        r = transactions.TransactionIDRange(accountID, params=params)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(resp == r.response)

    @requests_mock.Mocker()
    def test__transactions_sinceid(self, mock_get):
        """get the transactions since an id."""
        tid = "_v3_accounts_transaction_sinceid"
        resp, data, params = fetchTestData(responses, tid)
        r = transactions.TransactionsSinceID(accountID, params=params)
        mock_get.register_uri('GET',
                              "{}/{}".format(api.api_url, r),
                              text=json.dumps(resp))
        result = api.request(r)
        self.assertTrue(resp == r.response)

    @requests_mock.Mocker()
    def test__transaction_stream(self, mock_get):
        """get the streaming transaction information."""
        uri = 'https://test.com/v3/accounts/{}/transactions/stream'.format(accountID)
        # simulated list of transactions
        lot = [{"a": 10}, {"b": 20}, {"c": 30}, {"d": 40}, {"e": 50}]
        text = "\n".join([json.dumps(r) for r in lot])
        mock_get.register_uri('GET',
                              uri,
                              text=text)
        r = transactions.TransactionsStream(accountID)
        result = []
        n = 0
        with self.assertRaises(StreamTerminated) as oErr:
            for rv in api.request(r):
                result.append(json.dumps(rv))
                n += 1
                # terminate when we have 3 response lines
                if n == 3:
                    r.terminate()

        # the result containing 3 items, should equal the first 3 items
        # of the ticks
        self.assertTrue("\n".join(result) ==
                        "\n".join(json.dumps(x) for x in lot[0:3]))

    def test__transaction_stream_termination_1(self):
        """terminate a stream that does not exist."""
        r = transactions.TransactionsStream(accountID)
        with self.assertRaises(ValueError) as oErr:
            r.terminate()

if __name__ == "__main__":

    unittest.main()
