support classes
---------------

The :mod:`oandapyV20.contrib.requests` module contains several classes 
that can be used optionally when creating Order Requests.

When creating an order to create a position, it is possible to create
dependant orders that will be triggered when the position gets filled.
This goes typically for *Take Profit* and *Stop Loss*.

These order specifications and additional data that goes with these order
specifications can be created by the contrib.requests.*Order* classes and
the contrib.requests.*Details classes. 

.. toctree::
   :maxdepth: 4
   :glob:

   support/*
