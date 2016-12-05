oandapyV20.types
================

The :mod:`oandapyV20.types` module contains the types representing the types
that are used in the API-specs of OANDA, check developer.oanda.com_.
These types offer a convenient interface between Python types and
the types used in the REST-API.

.. _developer.oanda.com: http://developer.oanda.com

Take for instance the `PriceValue` type. It is the string representation of
a float.

.. code-block:: python

    from oandapyV20.types import PriceValue

    pv1 = PriceValue(122.345)
    pv2 = PriceValue("122.345")
    pv1.value
    "122.345"
    pv1.value == pv2.value
    True

Regardless the value we instantiate it with, a float or a string,
the PriceValue instance will allways be a string value.

The types also validate the values passed. Invalid values will raise an
exception.


.. toctree::
   :maxdepth: 4
   :glob:

   types/*
