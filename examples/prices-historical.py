import json
from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.instruments import InstrumentsCandles
from exampleauth import exampleAuth

accountID, access_token = exampleAuth()

api = API(access_token=access_token, environment="practice")

params = {
          "granularity": "M5",
          "count": 5,
          }
r = InstrumentsCandles(instrument="DE30_EUR", params=params)

try:
    R = api.request(r)
    print json.dumps(R, indent=2)
except V20Error as e:
    print("Error: {}".format(e))
