from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.transactions import TransactionsStream
from exampleauth import exampleAuth

accountID, access_token = exampleAuth()
api = API(access_token=access_token, environment="practice")

s = TransactionsStream(accountID=accountID)
try:
    n = 0
    for R in api.request(s):
        print R
        n += 1
        if n > 10:
            api.disconnect()
except V20Error as e:
    print("Error: {}".format(e))
