# -*- coding: utf-8 -*-
import json
import calendar
from iso8601 import parse_date

"""
pricingstream record example:

{
  "status": "tradeable",
  "asks": [
    {
      "price": "1.08186",
      "liquidity": 10000000.0
    },
    {
      "price": "1.08188",
      "liquidity": 10000000.0
    }
  ],
  "closeoutBid": "1.08169",
  "bids": [
    {
      "price": "1.08173",
      "liquidity": 10000000.0
    },
    {
      "price": "1.08171",
      "liquidity": 10000000.0
    }
  ],
  "instrument": "EUR_USD",
  "time": "2017-02-02T15:03:27.355655179Z",
  "closeoutAsk": "1.08190",
  "type": "PRICE",
  "tradeable": true
}
"""
mid_bid_ask = 4

TICK = 1
HEARTBEAT = 2


class StreamRecord(object):
    """StreamRecord - convert OANDA streamrecord."""

    def __init__(self, s, mode=mid_bid_ask):
        # accept JSON data aswell as stringdata to convert to JSON
        j = json.loads(s) if isinstance(s, str) else s
        # use calendar.timegm, this gives back the correct time without
        # timezone differences
        self.rtype = None
        self.data = {}
        if j["type"] == "PRICE":
            self.rtype = TICK
            self.data['instrument'] = j["instrument"]
            self.data['bid'] = float(j["closeoutBid"])
            self.data['ask'] = float(j["closeoutAsk"])
            self.data['mid'] = (self.data['bid'] + self.data['ask'])/2.0
            self.data['value'] = self.data['mid']
        elif j["type"] == "HEARTBEAT":
            self.rtype = HEARTBEAT
        else:
            raise ValueError("Unknown stream record type {}".format(s))

        self.dt = parse_date(j['time'])
        self.epoch = int(calendar.timegm(self.dt.timetuple()))
        self.data['time'] = j["time"]

    def recordtype(self):
        return self.rtype

    def __getitem__(self, k):
        return self.data[k]

    def __repr__(self):
        return json.dumps(self.data)
