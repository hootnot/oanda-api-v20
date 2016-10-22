OANDA REST-V20 API
==================

Interface to the OANDA V20 REST-service
---------------------------------------

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

The OANDA REST-V20 package has *logging* integrated. Logging can be
simply applied by enabling a *logger* .
The example below will log INFO-level logging to the file *v20.log*.
For details check the *logger* module in the standard Python documentation.


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
