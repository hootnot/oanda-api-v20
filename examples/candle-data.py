import json
from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.instruments import InstrumentsCandles
from exampleauth import exampleAuth

accountID, access_token = exampleAuth()

api = API(access_token=access_token, environment="practice")

instruments = ["DE30_EUR", "EUR_USD", "EUR_JPY"]
params = {"count": 5,
          "granularity": "M5"}

for instrument in instruments:
    try:
        r = InstrumentsCandles(instrument=instrument, params=params)
        rv = api.request(r)
        print("{}".format(json.dumps(rv, indent=2)))

    except V20Error as e:
        print("Error: {}".format(e))
