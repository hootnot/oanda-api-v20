"""OANDA API wrapper for OANDA's REST-V20 API."""

import json
import requests
from .exceptions import V20Error


TRADING_ENVIRONMENTS = {
    "practice": {
        "stream": 'https://stream-fxpractice.oanda.com',
        "api": 'https://api-fxpractice.oanda.com'
    },
    "live": {
        "stream": 'https://stream-fxtrade.oanda.com',
        "api": 'https://api-fxtrade.oanda.com'
    }
}


class API(object):
    r"""API - class to handle APIRequests objects to access API endpoints.

    Examples
    --------

    ::

        # get a list of trades
        from oandapyV20 import API
        import oandapyV20.endpoints.trades as trades

        api = API(access_token="xxx")
        accountID = "101-305-3091856-001"

        r = trades.Trades(accountID, op=trades.TRADE_LIST)
        # show the endpoint as it is constructed for this call
        print("REQUEST:{}".format(r))
        rv = api.request(r)
        print("RESPONSE:\n{}".format(json.dumps(rv, indent=2)))


    Output::

        REQUEST:v3/accounts/101-305-3091856-001/trades
        RESPONSE:
        "trades": [
            {
              "financing": "0.0000",
              "openTime": "2016-07-21T15:47:05.170212014Z",
              "price": "10133.9",
              "unrealizedPL": "8.0000",
              "realizedPL": "0.0000",
              "instrument": "DE30_EUR",
              "state": "OPEN",
              "initialUnits": "-10",
              "currentUnits": "-10",
              "id": "1032"
            },
            {
              "financing": "0.0000",
              "openTime": "2016-07-21T15:47:04.963590941Z",
              "price": "10134.4",
              "unrealizedPL": "13.0000",
              "realizedPL": "0.0000",
              "instrument": "DE30_EUR",
              "state": "OPEN",
              "initialUnits": "-10",
              "currentUnits": "-10",
              "id": "1030"
            }
          ],
          "lastTransactionID": "1040"
        }

    ::

        # reduce a trade by it's id
        from oandapyV20 import API
        import oandapyV20.endpoints.trades as trades

        headers = {"Content-Type": "application/json"}
        api = API(access_token="...", headers=headers)

        accountID = "101-305-3091856-001"
        tradeID = "1030"
        cfg = { "units": 5 }
        r = trades.Trades(accountID, tradeID=tradeID,
                          op=trades.TRADE_CLOSE, data=cfg)
        # show the endpoint as it is constructed for this call
        print("REQUEST:{}".format(r))
        rv = api.request(r)
        print("RESPONSE\n{}".format(json.dumps(rv, indent=2)))


    Output::

        REQUEST:v3/accounts/101-305-3091856-001/trades/1030/close
        RESPONSE: {
          "orderFillTransaction": {
            "orderID": "1041",
            "financing": "-0.1519",
            "instrument": "DE30_EUR",
            "userID": 1435156,
            "price": "10131.6",
            "tradeReduced": {
              "units": "5",
              "financing": "-0.1519",
              "realizedPL": "14.0000",
              "tradeID": "1030"
            },
            "batchID": "1041",
            "accountBalance": "44876.2548",
            "reason": "MARKET_ORDER_TRADE_CLOSE",
            "time": "2016-07-21T17:32:51.361464739Z",
            "units": "5",
            "type": "ORDER_FILL",
            "id": "1042",
            "pl": "14.0000",
            "accountID": "101-305-3091856-001"
          },
          "orderCreateTransaction": {
            "timeInForce": "FOK",
            "positionFill": "REDUCE_ONLY",
            "userID": 1435156,
            "batchID": "1041",
            "instrument": "DE30_EUR",
            "reason": "TRADE_CLOSE",
            "tradeClose": {
              "units": "5",
              "tradeID": "1030"
            },
            "time": "2016-07-21T17:32:51.361464739Z",
            "units": "5",
            "type": "MARKET_ORDER",
            "id": "1041",
            "accountID": "101-305-3091856-001"
          },
          "relatedTransactionIDs": [
            "1041",
            "1042"
          ],
          "lastTransactionID": "1042"
        }
    """

    def __init__(self, access_token, environment="practice", headers=None):
        """Instantiate an instance of OandaPy's API wrapper.

        Parameters
        ----------
        access_token : string
            Provide a valid access token.

        environment : string
            Provide the environment for OANDA's REST api. Valid values:
            'practice' or 'live'. Default: 'practice'.

        headers : dict (optional)
            Provide request headers to be set for a request. Several API
            endpoints need data in a JSON format. These calls require the
            header: 'Content-Type: application/json'.

        """
        try:
            TRADING_ENVIRONMENTS[environment]
        except:
            raise KeyError("Unknown environment: {}".format(environment))
        else:
            self.environment = environment

        self.access_token = access_token
        self.client = requests.Session()
        self._connected = False
        self.client.stream = False

        # personal token authentication
        if self.access_token:
            self.client.headers['Authorization'] = 'Bearer '+self.access_token

        if headers:
            self.client.headers.update(headers)

    def disconnect(self):
        """disconnect.

        disconnect a streaming connection. The _stream_request generator
        wil terminate.
        """
        self._connected = False

    def _request(self, method, url, request_args):
        func = getattr(self.client, method)

        response = None
        try:
            response = func(url, **request_args)
        except requests.RequestException as e:
            # log it ?
            raise e
        else:
            self._connected = True

        # Handle error responses
        if response.status_code >= 400:
            raise V20Error(response.status_code,
                           response.content.decode('utf-8'))
        return response

    def _api_request(self, method, url, request_args):
        """_api_request.

        make a 'regular' request. This method is called by
        the 'request' method after it has determined which
        call applies: regular or streaming.
        """
        content = None
        response = None
        try:
            response = self._request(method, url, request_args)
        except requests.RequestException as e:
            raise e
        else:
            content = response.content.decode('utf-8')
            content = json.loads(content)
            #endpoint.response(content)

        return content

    def _stream_request(self, method, url, request_args):
        """_stream_request.

        make a 'stream' request. This method is called by
        the 'request' method after it has determined which
        call applies: regular or streaming.
        """
        response = self._request(method, url, request_args)
        for line in response.iter_lines(90):
            if not self._connected:
                break

            if line:
                data = json.loads(line.decode("utf-8"))
                yield data

    def request(self, endpoint):
        """Perform a request for the APIRequest instance 'endpoint'.

        Parameters
        ----------
        endpoint : APIRequest
            The endpoint parameter contains an instance of an APIRequest
            containing the endpoint, method and optionally other parameters
            or body data.

        Raises
        ------
            V20Error in case of HTTP response code >= 400
        """
        at = "api"
        if hasattr(endpoint, "STREAM") and getattr(endpoint, "STREAM") is True:
            self.client.stream = True
            at = "stream"

        url = "{}/{}".format(TRADING_ENVIRONMENTS[self.environment][at],
                             endpoint)

        method = endpoint.method
        method = method.lower()
        params = None
        try:
            params = getattr(endpoint, "params")
        except AttributeError:
            # request does not have params
            params = {}

        request_args = {}
        if method == 'get':
            request_args['params'] = params
        elif hasattr(endpoint, "data") and endpoint.data:
            request_args['data'] = json.dumps(endpoint.data)

        if at == "api":
            content = self._api_request(method, url, request_args)
            endpoint.response(content)
            return content
        else:
            return self._stream_request(method, url, request_args)
