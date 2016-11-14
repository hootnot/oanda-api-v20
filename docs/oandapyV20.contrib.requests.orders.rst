oandapyV20.contrib.requests
===========================

Support classes
---------------

The requests package contains several classes that can be used
optional when creating Order Requests.
When creating an order to create a position, it is possible to create
dependant orders that will be triggered when the position gets filled.
This goes typically for *Take Profit* and *Stop Loss*.

.. autoclass:: oandapyV20.contrib.requests.TakeProfitDetails
    :members:
    :undoc-members:
    :show-inheritance:
    :special-members: __init__

.. autoclass:: oandapyV20.contrib.requests.StopLossDetails
    :members:
    :undoc-members:
    :show-inheritance:
    :special-members: __init__

.. autoclass:: oandapyV20.contrib.requests.TrailingStopLossDetails
    :members:
    :undoc-members:
    :show-inheritance:
    :special-members: __init__


Order classes
-------------

.. autoclass:: oandapyV20.contrib.requests.MarketOrderRequest
    :members:
    :undoc-members:
    :show-inheritance:
    :special-members: __init__

.. autoclass:: oandapyV20.contrib.requests.LimitOrderRequest
    :members:
    :undoc-members:
    :show-inheritance:
    :special-members: __init__

.. autoclass:: oandapyV20.contrib.requests.MITOrderRequest
    :members:
    :undoc-members:
    :show-inheritance:
    :special-members: __init__

.. autoclass:: oandapyV20.contrib.requests.TakeProfitOrderRequest
    :members:
    :undoc-members:
    :show-inheritance:
    :special-members: __init__

.. autoclass:: oandapyV20.contrib.requests.StopLossOrderRequest
    :members:
    :undoc-members:
    :show-inheritance:
    :special-members: __init__

.. autoclass:: oandapyV20.contrib.requests.TrailingStopLossOrderRequest
    :members:
    :undoc-members:
    :show-inheritance:
    :special-members: __init__

.. autoclass:: oandapyV20.contrib.requests.StopOrderRequest
    :members:
    :undoc-members:
    :show-inheritance:
    :special-members: __init__

.. autoclass:: oandapyV20.contrib.requests.PositionCloseRequest
    :members:
    :undoc-members:
    :show-inheritance:
    :special-members: __init__

.. autoclass:: oandapyV20.contrib.requests.TradeCloseRequest
    :members:
    :undoc-members:
    :show-inheritance:
    :special-members: __init__
