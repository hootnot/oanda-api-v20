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
        print R
        n += 1
        if n > 10:
            api.disconnect()
except V20Error as e:
    print("Error: {}".format(e))
