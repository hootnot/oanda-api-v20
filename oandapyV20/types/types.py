# -*- coding: utf-8 -*-
"""types."""

import six
import re
from abc import ABCMeta


@six.add_metaclass(ABCMeta)
class OAType(object):
    """baseclass for OANDA types."""

    @property
    def value(self):
        """value property."""
        return self._v


class AccountID(OAType):
    """representation of an AccountID, string value of an Account Identifier.

    Parameters
    ----------

    accountID : string (required)
        the accountID of a v20 account

    Example
    -------

        >>> print AccountID("001-011-5838423-001").value


    A ValueError exception is raised in case of an incorrect value.
    """

    def __init__(self, accountID):
        l = re.match(r"(?P<siteID>\d+)-(?P<divisionID>\d+)"
                     "-(?P<userID>\d+)-(?P<accountNumber>\d+)", accountID)
        if not l:
            msg = "AccountID {} not a valid V20 account".format(accountID)
            raise ValueError(msg)

        self._v = l.groupdict()


class OrderID(OAType):
    """representation of an orderID, string value of an integer.

    Parameters
    ----------

    orderID : integer or string (required)
        the orderID as a positive integer or as a string

    Example
    -------

        >>> print OrderID(1234).value


    A ValueError exception is raised in case of a negative integer value
    """

    def __init__(self, orderID):
        if int(orderID) < 0:
            raise ValueError("OrderID must be a positive integer value")
        self._v = "{:d}".format(int(orderID))


class TradeID(OAType):
    """representation of a tradeID, string value of an integer.

    Parameters
    ----------

    tradeID : integer or string (required)
        the tradeID as a positive integer or as a string

    Example
    -------

        >>> print TradeID(1234).value


    A ValueError exception is raised in case of a negative integer value
    """

    def __init__(self, tradeID):
        if int(tradeID) < 0:
            raise ValueError("TradeID must be a positive integer value")
        self._v = "{:d}".format(int(tradeID))


class AccountUnits(OAType):
    """representation AccountUnits, string value of a float."""

    def __init__(self, units):
        self._v = "{:.5f}".format(float(units))


class PriceValue(OAType):
    """representation PriceValue, string value of a float."""

    def __init__(self, priceValue):
        self._v = "{:.5f}".format(float(priceValue))


class Units(OAType):
    """representation Units, string value of an integer."""

    def __init__(self, units):
        self._v = "{:d}".format(int(units))


class ClientID(OAType):
    """representation of ClientID, a string value of max 128 chars."""

    def __init__(self, clientID):
        length = len(clientID)
        if not length or length > 128:
            raise ValueError("ClientID: length {}".format(length))

        self._v = clientID


class ClientTag(OAType):
    """representation of ClientTag, a string value of max 128 chars."""

    def __init__(self, clientTag):
        length = len(clientTag)
        if not length or length > 128:
            raise ValueError("ClientTag: length {}".format(length))

        self._v = clientTag


class ClientComment(OAType):
    """representation of ClientComment, a string value of max 128 chars."""

    def __init__(self, clientComment):
        length = len(clientComment)
        if not length or length > 128:
            raise ValueError("ClientComment: length {}".format(length))

        self._v = clientComment


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
