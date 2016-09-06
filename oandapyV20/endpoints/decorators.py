"""decorators."""


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


def endpoint(url, method="GET"):
    """endpoint - decorator to manipulate the REST-service endpoint.

    The endpoint decorator sets the endpoint and the method for the class
    to access the REST-service.
    """
    def dec(obj):
        obj.ENDPOINT = url
        obj.METHOD = method
        return obj

    return dec
