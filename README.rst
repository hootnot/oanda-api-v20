OANDA REST-V20 API wrapper
--------------------------

The REST-V20 API specs are not completely released yet. Support for 'streaming', 'pricing history' and 'forex labs' endpoints will be integrated when OANDA releases the specs of those endpoints.

.. image:: https://travis-ci.org/hootnot/oanda-api-v20.svg?branch=master
   :target: https://travis-ci.org/hootnot/oanda-api-v20
   :alt: Build

.. image:: https://readthedocs.org/projects/oanda-api-v20/badge/?version=latest
   :target: http://oanda-api-v20.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
   
.. image:: https://landscape.io/github/hootnot/oanda-api-v20/master/landscape.svg?style=flat
   :target: https://landscape.io/github/hootnot/oanda-api-v20/master
   :alt: Code Health

.. image:: https://coveralls.io/repos/github/hootnot/oanda-api-v20/badge.svg?branch=master
   :target: https://coveralls.io/github/hootnot/oanda-api-v20?branch=master
   :alt: Coverage

Status
======

 * The endpoint specs known till this moment are covered by the code.
 * Tests partially completed


Supported versions (passing the available tests) of Python:

    +-------------------+-----+-----+-----+-----+
    |                   | 2.7 | 3.3 | 3.4 | 3.5 |
    +===================+=====+=====+=====+=====+
    | **oanda-api-v20** | YES | YES | YES | YES |
    +-------------------+-----+-----+-----+-----+


Integration with Travis and Coveralls will follow.

Install
=======

.. code-block:: bash

    $ pip install git+https://github.com/hootnot/oanda-api-v20.git

If you want to run the tests, clone the repository:

.. code-block:: bash

    $ git clone https://github.com/hootnot/oanda-api-v20
    $ cd oanda-api-v20
    # edit tests/account.txt and tests/token.txt ...
    $ python setup.py test
    $ python setup.py install




Design
======

I have choosen a different approach regarding the design of the new library versus the
'oandapy' library which is based on 'mixin' classes.

In the V20-library endpoints are represented as APIRequest objects derived from the
APIRequest base class. Each endpoint group (accounts, trades, etc.) is represented
by it's own (abstract) class covering the functionality of all endpoints for that group. Each endpoint within that group is covered by a class derived from
the abstract class. These classes are provided with their endpoint and method
using the @endpoint decorator. If it concerns an endpoint based on a GET
request allowing query-parameters, then the @params decorator is applied also.

The V20-library has a client 'API'-class which processes APIRequest objects.

So it comes down to:

.. code-block:: python

    import json
    from oandapyV20 import API    # the client
    import oandapyV20.endpoints.trades as trades

    access_token = "..."
    accountID = "..."
    client = API(access_token=access_token)

    # request trades list
    r = trades.TradesList(accountID)
    rv = client.request(r)
    print("RESPONSE:\n{}".format(json.dumps(rv, indent=2)))


Processing series of requests is also possible now by storing different requests in 
an array or from some 'request-factory' class. Below an array example:

.. code-block:: python

     import json
     from oandapyV20 import API    # the client
     from oandapyV20.exceptions import V20Error
     import oandapyV20.endpoints.accounts as accounts
     import oandapyV20.endpoints.trades as trades
     import oandapyV20.endpoints.pricing as pricing

     access_token = "..."
     accountID = "..."
     client = API(access_token=access_token)

     # list of requests
     lor = []
     # request trades list
     lor.append(trades.TradesList(accountID)
     # request accounts list
     lor.append(accounts.AccountList())
     # request pricing info
     params={"instruments": "DE30_EUR,EUR_GBP"}
     lor.append(pricing.PricingInfo(accountID, params=params)

     for r in lor:
         try:
             rv = client.request(r)
             # put request and response in 1 JSON structure
             print("{}".format(json.dumps({"request": "{}".format(r),
                                           "response": rv}, indent=2)))
         except V20Error as e:
             print("OOPS: {:d} {:d}".format(e.code, e.msg))

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

    {
      "request": "v3/accounts/101-004-1435156-001/pricing",
      "response": {
        "prices": [
          {
            "status": "tradeable",
            "quoteHomeConversionFactors": {
              "negativeUnits": "1.00000000",
              "positiveUnits": "1.00000000"
            },
            "asks": [
              {
                "price": "10295.1",
                "liquidity": 25
              },
              {
                "price": "10295.3",
                "liquidity": 75
              },
              {
                "price": "10295.5",
                "liquidity": 150
              }
            ],
            "unitsAvailable": {
              "default": {
                "short": "60",
                "long": "100"
              },
              "reduceOnly": {
                "short": "0",
                "long": "20"
              },
              "openOnly": {
                "short": "60",
                "long": "0"
              },
              "reduceFirst": {
                "short": "60",
                "long": "100"
              }
            },
            "closeoutBid": "10293.5",
            "bids": [
              {
                "price": "10293.9",
                "liquidity": 25
              },
              {
                "price": "10293.7",
                "liquidity": 75
              },
              {
                "price": "10293.5",
                "liquidity": 150
              }
            ],
            "instrument": "DE30_EUR",
            "time": "2016-09-29T17:07:19.598030528Z",
            "closeoutAsk": "10295.5"
          },
          {
            "status": "tradeable",
            "quoteHomeConversionFactors": {
              "negativeUnits": "1.15679152",
              "positiveUnits": "1.15659083"
            },
            "asks": [
              {
                "price": "0.86461",
                "liquidity": 1000000
              },
              {
                "price": "0.86462",
                "liquidity": 2000000
              },
              {
                "price": "0.86463",
                "liquidity": 5000000
              },
              {
                "price": "0.86465",
                "liquidity": 10000000
              }
            ],
            "unitsAvailable": {
              "default": {
                "short": "624261",
                "long": "624045"
              },
              "reduceOnly": {
                "short": "0",
                "long": "0"
              },
              "openOnly": {
                "short": "624261",
                "long": "624045"
              },
              "reduceFirst": {
                "short": "624261",
                "long": "624045"
              }
            },
            "closeoutBid": "0.86442",
            "bids": [
              {
                "price": "0.86446",
                "liquidity": 1000000
              },
              {
                "price": "0.86445",
                "liquidity": 2000000
              },
              {
                "price": "0.86444",
                "liquidity": 5000000
              },
              {
                "price": "0.86442",
                "liquidity": 10000000
              }
            ],
            "instrument": "EUR_GBP",
            "time": "2016-09-29T17:07:19.994271769Z",
            "closeoutAsk": "0.86465"
          }
        ]
      }
    }
