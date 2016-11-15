# -*- coding: UTF-8 -*-
"""decorators."""


def dyndoc_insert(src):
    """docstring_insert - a decorator to insert API-docparts dynamically."""
    # manipulating docstrings this way is tricky due to indentation
    # the JSON needs leading whitespace to be interpreted correctly
    import json
    import re

    def mkblock(d, flag=0):
        # response, pretty formatted
        v = json.dumps(d, indent=2)
        if flag == 1:
            # strip the '[' and ']' in case of a list holding items
            # that stand on their own (example: tick records from a stream)
            nw = re.findall('.*?\[(.*)\]', v, flags=re.S)
            v = nw[0]
        # add leading whitespace for each line and start with a newline
        return "\n{}".format("".join(["{0:>16}{1}\n".format("", L)
                             for L in v.split('\n')]))

    def dec(obj):
        allSlots = re.findall("\{(_v3.*?)\}", obj.__doc__)
        docsub = {}
        sub = {}
        for k in allSlots:
            p = re.findall("^(_v3.*)_(.*)", k)
            p = list(*p)
            sub.update({p[1]: p[0]})

        for v in sub.values():
            for k in sub.keys():
                docsub["{}_url".format(v)] = "{}".format(src[v]["url"])
                if "resp" == k:
                    docsub.update({"{}_resp".format(v):
                                   mkblock(src[v]["response"])})
                if "body" == k:
                    docsub.update({"{}_body".format(v):
                                   mkblock(src[v]["body"])})

                if "params" == k:
                    docsub.update({"{}_params".format(v):
                                   mkblock(src[v]["params"])})
                if "ciresp" == k:
                    docsub.update({"{}_ciresp".format(v):
                                   mkblock(src[v]["response"], 1)})

        obj.__doc__ = obj.__doc__.format(**docsub)

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
                    setattr(wself, extraArg, kwargs[extraArg])
                    del kwargs[extraArg]
            origInit(wself, *args, **kwargs)
        setattr(cls, "__init__", wrapInit)

        return cls
