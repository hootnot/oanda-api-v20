# -*- coding: utf-8 -*-
"""Example demonstrating the contrib.request classes.

Create a MarketOrderRequest to enter 10000 EUR_USD LONG position along with
- a TakeProfitOrder to take profit @1.10
- a StopLossOrder to take loss @1.07

These values apply for this moment: EUR_USD 1.077
So when you run the example you may need to change the values.
"""
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

tpd = TakeProfitDetails(price=EUR_USD_TAKE_PROFIT)
print("Take Profit Details: \n{}".format(json.dumps(tpd.data, indent=4)))

sld = StopLossDetails(price=EUR_USD_STOP_LOSS)
print("Stop Loss Details: \n{}".format(json.dumps(sld.data, indent=4)))

# The orderspecs
specs = {"instrument": "EUR_USD",
         "units": 10000,
         "takeProfitOnFill": tpd.data,
         "stopLossOnFill": sld.data}

print("Full Market Order specs: \n{}".format(json.dumps(specs, indent=4)))

mktOrder = MarketOrderRequest(**specs)
print(mktOrder.data)

# create the OrderCreate request
r = orders.OrderCreate(accountID, data=mktOrder.data)

try:
    # create the OrderCreate request
    rv = api.request(r)
except oandapyV20.exceptions.V20Error as err:
    print(r.status_code, err)
else:
    print(json.dumps(rv, indent=2))

# or short: it could have been written as
mktOrder = MarketOrderRequest(
    instrument="EUR_USD",
    units=10000,
    takeProfitOnFill=TakeProfitDetails(price=EUR_USD_TAKE_PROFIT).data,
    stopLossOnFill=StopLossDetails(price=EUR_USD_STOP_LOSS).data)
