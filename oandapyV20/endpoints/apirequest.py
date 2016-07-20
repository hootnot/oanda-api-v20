"""Handling of API requests."""


def dyndoc_insert(src):
    """docstring_insert - a decorator to insert API-docparts dynamically."""
    # manipulating docstrings this way is tricky due to indentation
    # the JSON needs leading whitespace to be interpreted correctly
    import json

    def mkblock(d):
        # response, pretty formatted
        v = json.dumps(d, indent=2)
        # add leading whitespace for each line and start with a newline
        return "\n{}".format("".join(["{0:>16}{1}\n".format("", L)
                             for L in v.split('\n')]))

    def dec(obj):
        sub = {}
        for k in src.keys():
            # url
            sub["{}_url".format(k)] = src[k]["url"]
            sub["{}_resp".format(k)] = mkblock(src[k]["response"])
            if "body" in src[k]:
                sub["{}_body".format(k)] = mkblock(src[k]["body"])

        obj.__doc__ = obj.__doc__.format(**sub)
        return obj

    return dec


class APIRequest(object):
    """Base Class for API-request classes."""

    def __init__(self, endpoint, method="GET", body=None):
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
        self._response = None

        self._endpoint = endpoint
        self.method = method
        self.body = body

    def response(self, s):
        """response - set the response of the request."""
        self._response = s

    def __str__(self):
        """return the endpoint."""
        return self._endpoint
