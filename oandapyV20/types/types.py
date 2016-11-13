# -*- encoding: utf-8 -*-
"""types."""

import json
import six
from abc import ABCMeta


@six.add_metaclass(ABCMeta)
class OAType(object):
    """baseclass for OANDA types."""

    @property
    def value(self):
        """value property."""
        return self._v


class OrderID(OAType):
    """representation of an orderID, string value of an integer."""

    def __init__(self, v):
        if int(v) < 0:
            raise ValueError("OrderID must be a positive integer value")
        self._v = "{:d}".format(int(v))


class TradeID(OAType):
    """representation of a tradeID, string value of an integer."""

    def __init__(self, v):
        if int(v) < 0:
            raise ValueError("TradeID must be a positive integer value")
        self._v = "{:d}".format(int(v))


class AccountUnits(OAType):
    """representation AccountUnits, string value of a float."""

    def __init__(self, v):
        self._v = "{:.5f}".format(float(v))


class PriceValue(OAType):
    """representation PriceValue, string value of a float."""

    def __init__(self, v):
        self._v = "{:.5f}".format(float(v))


class Units(OAType):
    """representation Units, string value of an integer."""

    def __init__(self, v):
        self._v = "{:d}".format(int(v))


class ClientID(OAType):
    """representation of ClientID, a string value of max 128 chars."""

    def __init__(self, v):
        length = len(v)
        if not length or length > 128:
            raise ValueError("ClientID: length {}".format(length))

        self._v = v


class OrderIdentifier(OAType):
    """representation of the OrderIdentifier object."""

    def __init__(self, orderID, clientID):
        self._v = {
            "orderID": OrderID(orderID).value,
            "clientOrderID": ClientID(clientID).value
        }


class OrderSpecifier(OAType):
    """representation of the OrderSpecifier."""

    def __init__(self, specifier):
        if str(specifier).startswith('@'):
            self._v = ClientID(specifier.lstrip('@')).value
        else:
            self._v = OrderID(specifier).value
