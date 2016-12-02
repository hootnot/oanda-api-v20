Interface OANDA's REST-V20
==========================

The client
----------

The `oandapyV20` package contains a client class, `oandapyV20.API`, to
communicate with the REST-V20 interface. It processes requests that
can be created from the endpoint classes.
For it's communication it relies on: requests_.

.. _requests: http://docs.python-requests.org/en/master/

The client keeps no state of a requests.
The response of a request is assigned to the request instance. The response
is also returned as a return value by the client.

.. autoclass:: oandapyV20.API
      :inherited-members:
      :show-inheritance:
      :special-members: __init__

Exceptions
----------

.. autoclass:: oandapyV20.V20Error
      :inherited-members:
      :show-inheritance:
      :special-members: __init__

Logging
-------

The `oandapyV20` package has `logging` integrated. Logging can be
simply applied by enabling a `logger`.
The example below will log INFO-level logging to the file *v20.log*.
For details check the :py:mod:`logger` module in the standard Python
documentation.


.. code-block:: python


    # code snippet
    from oandapyV20 import API
    import oandapyV20.endpoints.orders as orders
    from oandapyV20.exceptions import V20Error
    from exampleauth import exampleAuth
    import logging

    logging.basicConfig(
        filename="v20.log",
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(name)s : %(message)s',
    )

    accountID, token = exampleAuth()
    ...

Resulting loglines:

.. code-block:: text

    2016-10-22 17:50:37,988 [INFO] oandapyV20.oandapyV20 : setting up API-client for environment practice
    2016-10-22 17:50:37,990 [INFO] oandapyV20.oandapyV20 : performing request https://api-fxpractice.oanda.com/v3/accounts/101-004-1435156-001/orders
    2016-10-22 17:50:37,998 [INFO] requests.packages.urllib3.connectionpool : Starting new HTTPS connection (1): api-fxpractice.oanda.com
    2016-10-22 17:50:38,866 [INFO] oandapyV20.oandapyV20 : performing request https://api-fxpractice.oanda.com/v3/accounts/101-004-1435156-001/orders
    2016-10-22 17:50:39,066 [ERROR] oandapyV20.oandapyV20 : request https://api-fxpractice.oanda.com/v3/accounts/101-004-1435156-001/orders failed [400,{"errorMessage":"Invalid value specified for 'order.instrument'"}]
