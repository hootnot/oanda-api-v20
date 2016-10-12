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


def endpoint(url, method="GET", expected_status=200):
    """endpoint - decorator to manipulate the REST-service endpoint.

    The endpoint decorator sets the endpoint and the method for the class
    to access the REST-service.
    """
    def dec(obj):
        obj.ENDPOINT = url
        obj.METHOD = method
        obj.EXPECTED_STATUS = expected_status
        return obj

    return dec


def abstractclass(cls):
    """abstractclass - class decorator.

    make sure the class is abstract and cannot be used on it's own.

    @abstractclass
    class A(object):
        def __init__(self, *args, **kwargs):
            # logic
            pass

    class B(A):
        pass

    a = A()   # results in an AssertionError
    b = B()   # works fine
    """
    setattr(cls, "_ISNEVER", cls.__bases__[0].__name__)
    origInit = cls.__dict__["__init__"]

    def wrapInit(self, *args, **kwargs):
        # when the class is instantiated we can check for bases
        # we don't want it to be the base class
        try:
            assert self.__class__.__bases__[-1].__name__ != self._ISNEVER
            origInit(self, *args, **kwargs)
        except AssertionError:
            raise TypeError("Use of abstract base class")

    # replace the original __init__
    setattr(wrapInit, "__doc__", getattr(origInit, "__doc__"))
    setattr(origInit, "__doc__", "")
    setattr(cls, "__init__", wrapInit)

    return cls


class extendargs(object):
    """'extendargs' decorator.

    Add extra arguments to the argumentlist of the constructor of the class.
    """

    def __init__(self, *loa):
        self.loa = loa

    def __call__(self, cls):
        # save parent class __init__
        origInit = cls.__bases__[0].__dict__["__init__"]

        def wrapInit(wself, *args, **kwargs):
            for extraArg in self.loa:
                if extraArg in kwargs:
                    setattr(cls, extraArg, kwargs[extraArg])
                    del kwargs[extraArg]
            origInit(wself, *args, **kwargs)
        setattr(cls, "__init__", wrapInit)

        return cls
