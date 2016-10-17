OANDA REST-V20 API wrapper
==========================

The REST-V20 API specs are not completely released yet. Support for 'pricing history' and 'forex labs' endpoints will be integrated when OANDA releases the specs of those endpoints.

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
------

 * The endpoint specs known till this moment are covered by the code.
 * Tests partially completed


Supported Python versions:

    +-------------------+-----+-----+-----+-----+------+
    | Python            | 2.7 | 3.3 | 3.4 | 3.5 | Pypy |
    +===================+=====+=====+=====+=====+======+
    | **oanda-api-v20** | YES | YES | YES | YES | YES  |
    +-------------------+-----+-----+-----+-----+------+



Install
-------

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
------

I have choosen a different approach regarding the design of the new library versus the
'oandapy' library which is based on 'mixin' classes.

In the V20-library endpoints are represented as APIRequest objects derived from the
APIRequest base class. Each endpoint group (accounts, trades, etc.) is represented
by it's own (abstract) class covering the functionality of all endpoints for that group. Each endpoint within that group is covered by a class derived from
the abstract class. These classes are provided with their endpoint and method
using the @endpoint decorator. If it concerns an endpoint based on a GET
request allowing query-parameters, then the @params decorator is applied also.

The V20-library has a client 'API'-class which processes APIRequest objects.

Examples
--------

API-endpoint access
~~~~~~~~~~~~~~~~~~~

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
             print("OOPS: {:d} {:s}".format(e.code, e.msg))

Output
``````

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


Streaming endpoints
~~~~~~~~~~~~~~~~~~~

Streaming quotes: use pricing.PricingStream.
Streaming transactions: use transactions.TransactionsEvents.

To fetch streaming data from a stream use the following pattern:

.. code-block:: python

    import json
    from oandapyV20 import API
    from oandapyV20.exceptions import V20Error
    from oandapyV20.endpoints.pricing import PricingStream

    accountID = "..."
    access_token="..."

    api = API(access_token=access_token, environment="practice")

    instruments = "DE30_EUR,EUR_USD,EUR_JPY"
    s = PricingStream(accountID=accountID, params={"instruments":instruments})
    try:
        n = 0
        for R in api.request(s):
            print(json.dumps(R, indent=2))
            n += 1
            if n > 10:
                api.disconnect()
    except V20Error as e:
        print("Error: {}".format(e))


Output
``````

.. code-block:: json

    {
      "status": "tradeable",
      "asks": [
        {
          "price": "10547.0",
          "liquidity": 25
        },
        {
          "price": "10547.2",
          "liquidity": 75
        },
        {
          "price": "10547.4",
          "liquidity": 150
        }
      ],
      "closeoutBid": "10546.6",
      "bids": [
        {
          "price": "10547.0",
          "liquidity": 25
        },
        {
          "price": "10546.8",
          "liquidity": 75
        },
        {
          "price": "10546.6",
          "liquidity": 150
        }
      ],
      "instrument": "DE30_EUR",
      "time": "2016-10-17T12:25:28.158741026Z",
      "closeoutAsk": "10547.4"
    }
    {
      "type": "HEARTBEAT",
      "time": "2016-10-17T12:25:37.447397298Z"
    }
    {
      "status": "tradeable",
      "asks": [
        {
          "price": "114.490",
          "liquidity": 1000000
        },
        {
          "price": "114.491",
          "liquidity": 2000000
        },
        {
          "price": "114.492",
          "liquidity": 5000000
        },
        {
          "price": "114.494",
          "liquidity": 10000000
        }
      ],
      "closeoutBid": "114.469",
      "bids": [
        {
          "price": "114.473",
          "liquidity": 1000000
        },
        {
          "price": "114.472",
          "liquidity": 2000000
        },
        {
          "price": "114.471",
          "liquidity": 5000000
        },
        {
          "price": "114.469",
          "liquidity": 10000000
        }
      ],
      "instrument": "EUR_JPY",
      "time": "2016-10-17T12:25:40.837289374Z",
      "closeoutAsk": "114.494"
    }
    {
      "type": "HEARTBEAT",
      "time": "2016-10-17T12:25:42.447922336Z"
    }
    {
      "status": "tradeable",
      "asks": [
        {
          "price": "1.09966",
          "liquidity": 10000000
        },
        {
          "price": "1.09968",
          "liquidity": 10000000
        }
      ],
      "closeoutBid": "1.09949",
      "bids": [
        {
          "price": "1.09953",
          "liquidity": 10000000
        },
        {
          "price": "1.09951",
          "liquidity": 10000000
        }
      ],
      "instrument": "EUR_USD",
      "time": "2016-10-17T12:25:43.689619691Z",
      "closeoutAsk": "1.09970"
    }
    {
      "status": "tradeable",
      "asks": [
        {
          "price": "114.486",
          "liquidity": 1000000
        },
        {
          "price": "114.487",
          "liquidity": 2000000
        },
        {
          "price": "114.488",
          "liquidity": 5000000
        },
        {
          "price": "114.490",
          "liquidity": 10000000
        }
      ],
      "closeoutBid": "114.466",
      "bids": [
        {
          "price": "114.470",
          "liquidity": 1000000
        },
        {
          "price": "114.469",
          "liquidity": 2000000
        },
        {
          "price": "114.468",
          "liquidity": 5000000
        },
        {
          "price": "114.466",
          "liquidity": 10000000
        }
      ],
      "instrument": "EUR_JPY",
      "time": "2016-10-17T12:25:43.635964725Z",
      "closeoutAsk": "114.490"
    }
    {
      "status": "tradeable",
      "asks": [
        {
          "price": "10547.3",
          "liquidity": 25
        },
        {
          "price": "10547.5",
          "liquidity": 75
        },
        {
          "price": "10547.7",
          "liquidity": 150
        }
      ],
      "closeoutBid": "10546.9",
      "bids": [
        {
          "price": "10547.3",
          "liquidity": 25
        },
        {
          "price": "10547.1",
          "liquidity": 75
        },
        {
          "price": "10546.9",
          "liquidity": 150
        }
      ],
      "instrument": "DE30_EUR",
      "time": "2016-10-17T12:25:44.900162113Z",
      "closeoutAsk": "10547.7"
    }
    {
      "status": "tradeable",
      "asks": [
        {
          "price": "10547.0",
          "liquidity": 25
        },
        {
          "price": "10547.2",
          "liquidity": 75
        },
        {
          "price": "10547.4",
          "liquidity": 150
        }
      ],
      "closeoutBid": "10546.6",
      "bids": [
        {
          "price": "10547.0",
          "liquidity": 25
        },
        {
          "price": "10546.8",
          "liquidity": 75
        },
        {
          "price": "10546.6",
          "liquidity": 150
        }
      ],
      "instrument": "DE30_EUR",
      "time": "2016-10-17T12:25:44.963539084Z",
      "closeoutAsk": "10547.4"
    }
    {
      "status": "tradeable",
      "asks": [
        {
          "price": "114.491",
          "liquidity": 1000000
        },
        {
          "price": "114.492",
          "liquidity": 2000000
        },
        {
          "price": "114.493",
          "liquidity": 5000000
        },
        {
          "price": "114.495",
          "liquidity": 10000000
        }
      ],
      "closeoutBid": "114.471",
      "bids": [
        {
          "price": "114.475",
          "liquidity": 1000000
        },
        {
          "price": "114.474",
          "liquidity": 2000000
        },
        {
          "price": "114.473",
          "liquidity": 5000000
        },
        {
          "price": "114.471",
          "liquidity": 10000000
        }
      ],
      "instrument": "EUR_JPY",
      "time": "2016-10-17T12:25:45.586100087Z",
      "closeoutAsk": "114.495"
    }
