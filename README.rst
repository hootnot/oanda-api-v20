OANDA REST-V20 API wrapper
==========================

.. _Top:

As of march 2018 OANDA no longer supports the v1 REST-API. The only pending
V20 endpoint was the *forexlabs endpoint*. Instead of launching *forexlabs*
as a *V20-endpoint*, OANDA choose to support this endpoint from the v1
REST interface, see: http://developer.oanda.com/rest-live-v20/forexlabs-ep/.


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

.. image:: https://badge.fury.io/py/oandapyV20.svg
   :target: https://badge.fury.io/py/oandapyV20
   :alt: Pypi

.. image:: https://api.codacy.com/project/badge/Grade/5946514e3a7c407291f76e630ce3553b 
   :target: https://www.codacy.com/app/hootnot/oandaapiv20utm_source=github.com&amp;utm_medium=referral&amp;utm_content=hootnot/oanda-api-v20&amp;utm_campaign=Badge_Grade
   :alt: Codacy

Supported Python versions:

    +-------------------+-----+-----+-----+-----+-----+------+
    | Python            | 2.7 | 3.3 | 3.4 | 3.5 | 3.6 | Pypy |
    +===================+=====+=====+=====+=====+=====+======+
    | **oanda-api-v20** | YES | YES | YES | YES | YES | YES  |
    +-------------------+-----+-----+-----+-----+-----+------+


Interactive
-----------

.. image:: https://jupyter.readthedocs.io/en/latest/_static/_images/jupyter.svg
   :target: ./jupyter
   :alt: Jupyter

Using the Jupyter `notebook`_ it is easy to play with the
*oandapyV20* library.

.. _notebook: ./jupyter/index.ipynb

TOC
---

   + `Install`_
   + `Design`_
   + `Client`_
       - `contrib.requests`_
       - `contrib.factories`_
       - `API-endpoint access`_
       - `Placing a MarketOrder with TakeProfitOrder and StopLossOrder`_
       - `Processing series of requests`_
       - `Streaming endpoints`_

Install
-------

.. code-block:: bash

    $ pip install oandapyV20


or the latest development version from github:

.. code-block:: bash

    $ pip install git+https://github.com/hootnot/oanda-api-v20.git

If you want to run the tests, clone the repository:

.. code-block:: bash

    $ git clone https://github.com/hootnot/oanda-api-v20
    $ cd oanda-api-v20

    # install necessary packages for testing
    $ grep "\- pip install" .travis.yml |
    > while read LNE
    > do `echo $LNE| cut -c2-` ; done

    $ python setup.py test
    $ python setup.py install

Examples are provided in the https://github.com/hootnot/oandapyV20-examples
repository.



Design
------

In the V20-library endpoints are represented as APIRequest objects derived from the
APIRequest base class. Each endpoint group (accounts, trades, etc.) is represented
by it's own (abstract) class covering the functionality of all endpoints for that group. Each endpoint within that group is covered by a class derived from
the abstract class.

Top_

Client
~~~~~~

The V20-library has a client class (API) which processes APIRequest objects.

Top_

contrib.requests
~~~~~~~~~~~~~~~~

The contrib.request package offers classes providing an easy way
to construct the data for the *data* parameter of the OrderCreate endpoint
or the TradeCRCDO (Create/Replace/Cancel Dependent Orders).

.. code-block:: python

    mktOrder = MarketOrderRequest(instrument="EUR_USD",
         units=10000,
         takeProfitOnFill=TakeProfitDetails(price=1.10).data,
         stopLossOnFill=StopLossDetails(price=1.07).data
    ).data


    instead of:

.. code-block:: python

    mktOrder = {'order': {
                   'timeInForce': 'FOK',
                   'instrument': 'EUR_USD',
                   'positionFill': 'DEFAULT',
                   'units': '10000',
                   'type': 'MARKET',
                   'takeProfitOnFill': {
                       'timeInForce': 'GTC',
                       'price': '1.10000'}
                   }
                   'stopLossOnFill': {
                       'timeInForce': 'GTC',
                       'price': '1.07000'}
                   }
               }


Top_

contrib.factories
~~~~~~~~~~~~~~~~~

The contrib.factories module offers classes providing an easy way
generate requests.
Downloading historical data is limited to 5000 records per request. This
means that you have to make consecutive requests with change of parameters
if you want more than 5000 records.

The *InstrumentsCandlesFactory* solves this by generating the requests for you,
example:

.. code-block:: python

   import sys
   import json

   from oandapyV20.contrib.factories import InstrumentsCandlesFactory
   from oandapyV20 import API

   access_token = "..."

   client = API(access_token=access_token)

   _from = sys.argv[1]
   _to = sys.argv[2]
   gran = sys.argv[3]
   instr = sys.argv[4]

   params = {
       "granularity": gran,
       "from": _from,
       "to": _to
   }

   def cnv(r, h):
       for candle in r.get('candles'):
           ctime = candle.get('time')[0:19]
           try:
               rec = "{time},{complete},{o},{h},{l},{c},{v}".format(
                   time=ctime,
                   complete=candle['complete'],
                   o=candle['mid']['o'],
                   h=candle['mid']['h'],
                   l=candle['mid']['l'],
                   c=candle['mid']['c'],
                   v=candle['volume'],
               )
           except Exception as e:
               print(e, r)
           else:
               h.write(rec+"\n")

   with open("/tmp/{}.{}.out".format(instr, gran), "w") as O:
       for r in InstrumentsCandlesFactory(instrument=instr, params=params):
           print("REQUEST: {} {} {}".format(r, r.__class__.__name__, r.params))
           rv = client.request(r)
           cnv(r.response, O)


When running this:

.. code-block:: shell

   $ python oandahist.py 2017-01-01T00:00:00Z 2017-06-30T00:00:00Z H4 EUR_USD
   REQUEST: v3/instruments/EUR_USD/candles InstrumentsCandles
   {'to': '2017-03-25T08:00:00Z',
    'from': '2017-01-01T00:00:00Z', 'granularity': 'H4'}
   REQUEST: v3/instruments/EUR_USD/candles InstrumentsCandles
   {'to': '2017-06-16T20:00:00Z', 'from': '2017-03-25T12:00:00Z',
    'granularity': 'H4'}
   REQUEST: v3/instruments/EUR_USD/candles InstrumentsCandles
   {'to': '2017-06-30T00:00:00Z', 'from': '2017-06-17T00:00:00Z',
    'granularity': 'H4'}


The output shows it processed three *InstrumentsCandles* requests. The
data can be found in */tmp/EUR_USD.H4.out*:

.. code-block:: shell

   $ tail /tmp/EUR_USD.H4.out
   ...
   2017-06-28T01:00:0,True,1.13397,1.13557,1.13372,1.13468,1534
   2017-06-28T05:00:0,True,1.13465,1.13882,1.13454,1.13603,8486
   2017-06-28T09:00:0,True,1.13606,1.13802,1.12918,1.13315,12815
   2017-06-28T13:00:0,True,1.13317,1.13909,1.13283,1.13781,13255
   2017-06-28T17:00:0,True,1.13783,1.13852,1.13736,1.13771,2104
   2017-06-28T21:00:0,True,1.13789,1.13894,1.13747,1.13874,1454


Top_

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


Top_

Placing a *MarketOrder* with *TakeProfitOrder* and *StopLossOrder*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import json

    from oandapyV20.contrib.requests import MarketOrderRequest
    from oandapyV20.contrib.requests import TakeProfitDetails, StopLossDetails

    import oandapyV20.endpoints.orders as orders
    import oandapyV20

    from exampleauth import exampleAuth


    accountID, access_token = exampleAuth()
    api = oandapyV20.API(access_token=access_token)

    # EUR_USD (today 1.0750)
    EUR_USD_STOP_LOSS = 1.07
    EUR_USD_TAKE_PROFIT = 1.10

    mktOrder = MarketOrderRequest(
        instrument="EUR_USD",
        units=10000,
        takeProfitOnFill=TakeProfitDetails(price=EUR_USD_TAKE_PROFIT).data,
        stopLossOnFill=StopLossDetails(price=EUR_USD_STOP_LOSS).data)

    # create the OrderCreate request
    r = orders.OrderCreate(accountID, data=mktOrder.data)
    try:
        # create the OrderCreate request
        rv = api.request(r)
    except oandapyV20.exceptions.V20Error as err:
        print(r.status_code, err)
    else:
        print(json.dumps(rv, indent=2))


Top_

Processing series of requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     lor.append(trades.TradesList(accountID))
     # request accounts list
     lor.append(accounts.AccountList())
     # request pricing info
     params={"instruments": "DE30_EUR,EUR_GBP"}
     lor.append(pricing.PricingInfo(accountID, params=params))

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
            "closeoutAsk": "0.86465",
            "type": "PRICE"
          }
        ]
      }
    }

Top_

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
                s.terminate("maxrecs received: {}".format(MAXREC))

    except V20Error as e:
        print("Error: {}".format(e))

Check the 'examples' directory for more detailed examples.

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
      "closeoutAsk": "10547.4",
      "type": "PRICE",
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
      "closeoutAsk": "114.494",
      "type": "PRICE",
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
      "closeoutAsk": "1.09970",
      "type": "PRICE"
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
      "closeoutAsk": "114.490",
      "type": "PRICE"
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
      "closeoutAsk": "10547.7",
      "type": "PRICE"
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
      "closeoutAsk": "10547.4",
      "type": "PRICE"
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
      "closeoutAsk": "114.495",
      "type": "PRICE"
    }

Top_

About this software
-------------------
The *oanda-api-v20* software is a personal project.
I have no prior or existing relationship with OANDA.

If you have any questions regarding this software, please take a look at
the documentation first:

 * oandapyV20 : http://oanda-api-v20.readthedocs.io/en/latest/?badge=latest
 * OANDA developer docs : http://developer.oanda.com
 * examples : https://github.com/hootnot/oandapyV20-examples
 * Github: https://github.com/hootnot/oanda-api-v20 check the open and closed issues

If you still have questions/issues you can open an *issue* on Gitub: https://github.com/hootnot/oanda-api-v20
