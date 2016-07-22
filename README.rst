OANDA REST-V20 API wrapper
--------------------------

The REST-V20 API specs are not completely released yet. Support for 'streaming', 'pricing history' and 'forex labs' endpoints will be integrated when OANDA releases the specs of those endpoints.


.. image:: https://landscape.io/github/hootnot/oanda-api-v20/master/landscape.svg?style=flat
   :target: https://landscape.io/github/hootnot/oanda-api-v20/master
   :alt: Code Health

.. image:: https://readthedocs.org/projects/oanda-api-v20/badge/?version=latest
   :target: http://oanda-api-v20.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
   

Status
======

 * The endpoint specs known till this moment are covered by the code.
 * Tests partially completed


Supported versions (passing the available tests) of Python:

    +-------------------+----------+----------+ 
    |                   | ** 2.7** | ** 3.5** |
    +===================+==========+==========+ 
    | **oanda-api-v20** | YES      | YES      |
    +-------------------+----------+----------+ 


Integration with Travis and Coveralls will follow.

Design
======

I have choosen a different approach regarding the design of the new library versus the
'oandapy' library which is based on 'mixin' classes.

In the V20-library endpoints are represented as APIRequest objects derived from the
APIRequest base class. Each endpoint group (accounts, trades, etc.) is represented
by it's own class covering the functionality of all endpoints for that group.

The V20-library has a client 'API'-class which processes APIRequest objects.

So it comes down to:

.. code-block:: python

     import json
     from oandapyv20 import API    # the client
     import oandapyv20.endpoints.trades as trades

     access_token = "..."
     accountID = "..."
     client = API(access_token="...")

     # request trades list
     r = trades.Trades(accountID, op=trades.TRADES_LIST)
     rv = client.request(r)
     print("RESPONSE:\n{}".format(json.dumps(rv, indent=2)))


Processing series of requests is also possible now by storing different requests in 
an array or from some 'request-factory' class. Below an array example:

.. code-block:: python

     import json
     from oandapyV20 import API    # the client
     import oandapyV20.endpoints.accounts as accounts
     import oandapyV20.endpoints.trades as trades

     access_token = "..."
     accountID = "..."
     client = API(access_token="...")

     # list of requests
     lor = []
     # request trades list
     lor.append(trades.Trades(accountID, op=trades.TRADE_LIST))
     # request accounts list
     lor.append(accounts.Accounts(op=accounts.ACCOUNT_LIST))


     for r in lor:
         rv = client.request(r)
         # put request and response in 1 JSON structure
         print("{}".format(json.dumps({"request": "{}".format(r), 
                                       "response": rv}, indent=2)))


Output
~~~~~~

.. code-block:: json

    {
      "request": "v3/accounts/101-004-1435156-001/trades",
      "response": {
        "lastTransactionID": "1109",
        "trades": [
          {
            "unrealizedPL": "23.0000",
            "financing": "-0.5556",
            "state": "OPEN",
            "price": "10159.4",
            "realizedPL": "0.0000",
            "currentUnits": "-10",
            "openTime": "2016-07-22T16:47:04.315211198Z",
            "initialUnits": "-10",
            "instrument": "DE30_EUR",
            "id": "1105"
          },
          {
            "unrealizedPL": "23.0000",
            "financing": "-0.5556",
            "state": "OPEN",
            "price": "10159.4",
            "realizedPL": "0.0000",
            "currentUnits": "-10",
            "openTime": "2016-07-22T16:47:04.141436468Z",
            "initialUnits": "-10",
            "instrument": "DE30_EUR",
            "id": "1103"
          }
        ]
      }
    }
    
    {
      "request": "v3/accounts",
      "response": {
        "accounts": [
          {
            "tags": [],
            "id": "101-004-1435156-002"
          },
          {
            "tags": [],
            "id": "101-004-1435156-001"
          }
        ]
      }
    }
