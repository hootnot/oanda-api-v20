# -*- coding: utf-8 -*-
"""OANDA API wrapper for OANDA's REST-V20 API."""

import json
import requests
import logging
from .exceptions import V20Error

ITER_LINES_CHUNKSIZE = 60

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

DEFAULT_HEADERS = {
    "Accept-Encoding": "gzip, deflate"
}

logger = logging.getLogger(__name__)


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

        r = trades.TradesList(accountID)
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

        api = API(access_token="...")

        accountID = "101-305-3091856-001"
        tradeID = "1030"
        cfg = {"units": 5}
        r = trades.TradeClose(accountID, tradeID=tradeID, data=cfg)
        # show the endpoint as it is constructed for this call
        print("REQUEST:{}".format(r))
        rv = api.request(r)
        print("RESPONSE\n{}".format(json.dumps(rv, indent=2)))

    or by using it in a *with context*:

    ::

        with API(access_token="...") as api:

            accountID = "101-305-3091856-001"
            tradeID = "1030"
            cfg = {"units": 5}
            r = trades.TradeClose(accountID, tradeID=tradeID, data=cfg)
            # show the endpoint as it is constructed for this call
            print("REQUEST:{}".format(r))
            rv = api.request(r)
            print("RESPONSE\n{}".format(json.dumps(rv, indent=2)))

    in this case the API-client instance *api* will close connections
    explicitely.

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

    def __init__(self, access_token, environment="practice",
                 headers=None, request_params=None):
        """Instantiate an instance of OandaPy's API wrapper.

        Parameters
        ----------
        access_token : string
            Provide a valid access token.

        environment : string
            Provide the environment for OANDA's REST api. Valid values:
            'practice' or 'live'. Default: 'practice'.

        headers : dict (optional)
            Provide request headers to be set for a request.


        .. note::

            There is no need to set the 'Content-Type: application/json'
            for the endpoints that require this header. The API-request
            classes covering those endpoints will take care of the header.

        request_params : (optional)
            parameters to be passed to the request. This can be used to apply
            for instance a timeout value:

               request_params={"timeout": 0.1}

            See specs of the requests module for full details of possible
            parameters.

        .. warning::
            parameters belonging to a request need to be set on the
            requestinstance and are NOT passed via the client.

        """
        logger.info("setting up API-client for environment %s", environment)
        try:
            TRADING_ENVIRONMENTS[environment]

        except KeyError as err:  # noqa F841
            logger.error("unkown environment %s", environment)
            raise KeyError("Unknown environment: {}".format(environment))

        else:
            self.environment = environment

        self.access_token = access_token
        self.client = requests.Session()
        self.client.stream = False
        self._request_params = request_params if request_params else {}

        # personal token authentication
        if self.access_token:
            self.client.headers['Authorization'] = 'Bearer '+self.access_token

        self.client.headers.update(DEFAULT_HEADERS)
        if headers:
            self.client.headers.update(headers)
            logger.info("applying headers %s", ",".join(headers.keys()))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        """close.

        explicit close of the session.
        """
        self.client.close()

    @property
    def request_params(self):
        """request_params property."""
        return self._request_params

    def __request(self, method, url, request_args, headers=None, stream=False):
        """__request.

        make the actual request. This method is called by the
        request method in case of 'regular' API-calls. Or indirectly by
        the__stream_request method if it concerns a 'streaming' call.
        """
        func = getattr(self.client, method)
        headers = headers if headers else {}
        response = None
        try:
            logger.info("performing request %s", url)
            response = func(url, stream=stream, headers=headers,
                            **request_args)
        except requests.RequestException as err:
            logger.error("request %s failed [%s]", url, err)
            raise err

        # Handle error responses
        if response.status_code >= 400:
            logger.error("request %s failed [%d,%s]",
                         url,
                         response.status_code,
                         response.content.decode('utf-8'))
            raise V20Error(response.status_code,
                           response.content.decode('utf-8'))
        return response

    def __stream_request(self, method, url, request_args, headers=None):
        """__stream_request.

        make a 'stream' request. This method is called by
        the 'request' method after it has determined which
        call applies: regular or streaming.
        """
        headers = headers if headers else {}
        response = self.__request(method, url, request_args,
                                  headers=headers, stream=True)
        lines = response.iter_lines(ITER_LINES_CHUNKSIZE)
        for line in lines:
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
        method = endpoint.method
        method = method.lower()
        params = None
        try:
            params = getattr(endpoint, "params")
        except AttributeError:
            # request does not have params
            params = {}

        headers = {}
        if hasattr(endpoint, "HEADERS"):
            headers = getattr(endpoint, "HEADERS")

        request_args = {}
        if method == 'get':
            request_args['params'] = params
        elif hasattr(endpoint, "data") and endpoint.data:
            request_args['json'] = endpoint.data

        # if any parameter for request then merge them
        request_args.update(self._request_params)

        # which API to access ?
        if not (hasattr(endpoint, "STREAM") and
                getattr(endpoint, "STREAM") is True):
            url = "{}/{}".format(
                TRADING_ENVIRONMENTS[self.environment]["api"],
                endpoint)

            response = self.__request(method, url,
                                      request_args, headers=headers)
            content = response.content.decode('utf-8')
            content = json.loads(content)

            # update endpoint
            endpoint.response = content
            endpoint.status_code = response.status_code

            return content

        else:
            url = "{}/{}".format(
                TRADING_ENVIRONMENTS[self.environment]["stream"],
                endpoint)
            endpoint.response = self.__stream_request(method,
                                                      url,
                                                      request_args,
                                                      headers=headers)
            return endpoint.response
