"""OANDA API wrapper for OANDA's REST-V20 API."""

import json
import requests
from .exceptions import V20Error


TRADING_ENVIRONMENTS = {
    "practice": 'https://api-fxpractice.oanda.com',
    "live": 'https://api-fxtrade.oanda.com'
}


class API(object):
    """API - class to handle requests to access API endpoints."""

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
            self.api_url = TRADING_ENVIRONMENTS[environment]
        except: 
            raise KeyError("Unknown environment: {}".format(environment))

        self.access_token = access_token
        self.client = requests.Session()

        # personal token authentication
        if self.access_token:
            self.client.headers['Authorization'] = 'Bearer '+self.access_token

        if headers:
            self.client.headers.update(headers)

    def request(self, endpoint, params=None):
        """Perform a request for the APIRequest instance 'endpoint'.

        Parameters
        ----------
        endpoint : APIRequest
            The endpoint parameter contains an instance of an APIRequest
            containing the endpoint, method and optionally other parameters.

        params : dict
            The params paremeter optionally provides a dictionary with
            parameters for the request. Data for POST, PUT and PATCH is
            passed this way.
        """
        url = "{}/{}".format(self.api_url, endpoint)

        method = endpoint.method
        method = method.lower()
        params = params or {}

        func = getattr(self.client, method)

        request_args = {}
        if method == 'get':
            request_args['params'] = params
        elif endpoint.body:
            request_args['data'] = json.dumps(endpoint.body)

        response = None
        try:
            response = func(url, **request_args)
        except requests.RequestException as e:
            # log it ?
            raise e

        content = response.content.decode('utf-8')

        # Handle error responses
        if response.status_code >= 400:
            raise V20Error(response.status_code, content)

        content = json.loads(content)

        endpoint.response(content)
        return content
