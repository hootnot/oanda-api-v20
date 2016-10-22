"""create order demo."""
import json
from oandapyV20 import API
import oandapyV20.endpoints.orders as orders
from oandapyV20.exceptions import V20Error
from exampleauth import exampleAuth
import logging

logging.basicConfig(
    filename="log.out",
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s : %(message)s',
)

accountID, token = exampleAuth()

orderConf = [
       # ok
       {
         "order": {
            "units": "100",
            "instrument": "EUR_USD",
            "timeInForce": "FOK",
            "type": "MARKET",
            "positionFill": "DEFAULT"
          }
        },
       # wrong instrument, gives an error
       {
         "order": {
            "units": "100",
            "instrument": "UR_USD",
            "timeInForce": "FOK",
            "type": "MARKET",
            "positionFill": "DEFAULT"
          }
        }
]

# client
api = API(access_token=token)

# create and process order requests
for O in orderConf:
    r = orders.OrderCreate(accountID=accountID, data=O)
    print("processing : {}".format(r))
    print("===============================")
    print(r.data)
    try:
        response = api.request(r)
    except V20Error as e:
        print("V20Error: {}".format(e))
    else:
        print("Response: {}\n{}".format(r.status_code,
                                        json.dumps(response, indent=2)))
