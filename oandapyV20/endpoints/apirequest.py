"""Handling of API requests."""
from abc import ABCMeta, abstractmethod


class APIRequest(object):
    """Base Class for API-request classes."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, endpoint, method="GET", expected_status=200):
        """Instantiate an API request.

        Parameters
        ----------
        endpoint : string
            the URL format string

        method : string
            the method for the request. Default: GET.

        body : dict
            dictionary with data for the request. This data
            will be sent as JSON-data.
        """
        self._expected_status = expected_status
        self._status_code = None
        self._response = None

        self._endpoint = endpoint
        self.method = method

    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        if value != self._expected_status:
            raise ValueError("{} {} {:d}".format(self, self.method, value))
        self._status_code = value

    def response(self, s):
        """response - set the response of the request."""
        self._response = s

    def __str__(self):
        """return the endpoint."""
        return self._endpoint
