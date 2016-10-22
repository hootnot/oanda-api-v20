Examples
--------


Example for trades-endpoints
````````````````````````````

Take the script below and name it 'trades.py'. From the shell:

::

    hootnot@dev:~/test$ python trades.py list
    hootnot@dev:~/test$ python trades.py open
    hootnot@dev:~/test$ python trades.py details <id1> [<id2> ...]
    hootnot@dev:~/test$ python trades.py close <id1> <numunits> [<id2> <numunits>...]
    hootnot@dev:~/test$ python trades.py clext <id1> [<id2> ...]
    hootnot@dev:~/test$ python trades.py crc_do <id1> <takeprofit> <stoploss> [<id2> ...]


.. code-block:: python
   
    # use of the Trades{..} classes
    import json
    import requests
    from oandapyV20 import API
    
    
    import oandapyV20.endpoints.trades as trades
    import sys
 
    access_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
    accountID = "zzz-zzzz-zzzzz"

    api = API(access_token=access_token)
 
    if chc == 'list':
       r = trades.TradesList(accountID)
       rv = api.request(r)
       print("RESP:\n{} ".format(json.dumps(rv, indent=2)))
 
    if chc == 'open':
       r = trades.OpenTrades(accountID)
       rv = api.request(r)
       print("RESP:\n{} ".format(json.dumps(rv, indent=2)))
       tradeIDs = [o["id"] for o in rv["trades"]]
       print("TRADE IDS: {}".format(tradeIDs))
 
    if chc == 'details':
       for O in sys.argv[2:]:
           r = trades.TradeDetails(accountID, tradeID=O)
           rv = api.request(r)
           print("RESP:\n{} ".format(json.dumps(rv, indent=2)))
 
    if chc == 'close':
       X = iter(sys.argv[2:])
       for O in X:
           cfg = { "units": X.next() }
           r = trades.TradeClose(accountID, tradeID=O, data=cfg)
           rv = api.request(r)
           print("RESP:\n{} ".format(json.dumps(rv, indent=2)))
 
    if chc == 'cltext':
       for O in sys.argv[2:]:  # tradeIDs
           cfg = { "clientExtensions": {
                   "id": "myID{}".format(O),
                   "comment": "myComment",
                }
             }
           r = trades.TradeClientExtensions(accountID, tradeID=O, data=cfg)
           rv = api.request(r)
           print("RESP:\n{} ".format(json.dumps(rv, indent=2)))
 
    if chc == 'crc_do':
       X = iter(sys.argv[2:])
       for O in X:
           cfg = {
                   "takeProfit": {
                     "timeInForce": "GTC",
                     "price": X.next(),
                   },
                   "stopLoss": {
                     "timeInForce": "GTC",
                     "price": X.next()
                   }
             }
           r = trades.TradeCRCDO(accountID, tradeID=O, data=cfg)
           rv = api.request(r)
           print("RESP:\n{} ".format(json.dumps(rv, indent=2)))
