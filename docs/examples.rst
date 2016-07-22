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
   
    # use of the Trades class to demonstrate the use of various 'op'-flags
    import json
    import requests
    from oandapyV20 import API
    
    
    import oandapyV20.endpoints.trades as trades
    import sys
 
    access_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
    accountID = "zzz-zzzz-zzzzz"

    api = API(access_token=access_token, headers={ "Content-Type": "application/json"} )
 
    if chc == 'list':
       r = trades.Trades(accountID, op=trades.TRADE_LIST)
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
           r = trades.Trades(accountID, tradeID=O, op=trades.TRADE_DETAILS)
           rv = api.request(r)
           print("RESP:\n{} ".format(json.dumps(rv, indent=2)))
 
    if chc == 'close':
       X = iter(sys.argv[2:])
       for O in X:
           cfg = { "units": X.next() }
           r = trades.Trades(accountID, tradeID=O, op=trades.TRADE_CLOSE, data=cfg)
           rv = api.request(r)
           print("RESP:\n{} ".format(json.dumps(rv, indent=2)))
 
    if chc == 'cltext':
       for O in sys.argv[2:]:  # tradeIDs
           cfg = { "clientExtensions": {
                   "id": "myID{}".format(O),
                   "comment": "myComment",
                }
             }
           r = trades.Trades(accountID, tradeID=O, data=cfg, op=trades.TRADE_UPDATE)
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
           r = trades.Trades(accountID, tradeID=O, data=cfg, op=trades.TRADE_CRC_DO)
           rv = api.request(r)
           print("RESP:\n{} ".format(json.dumps(rv, indent=2)))
