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

PRICE = 1
HEARTBEAT = 2


class StreamRecord(object):
    """StreamRecord - convert OANDA streamrecord."""

    def __init__(self, sr):
        self._rtype = None

        # accept JSON data aswell as stringdata to convert to JSON
        if isinstance(sr, (str, unicode)):
            sr = json.loads(sr)

        self.data = {}
        self.convert(sr)

    def convert(self, sr):
        if sr["type"] == "PRICE":
            self._rtype = PRICE
            self.data['instrument'] = sr["instrument"]
            self.data['bid'] = float(sr["closeoutBid"])
            self.data['ask'] = float(sr["closeoutAsk"])
            self.data['mid'] = (self.data['bid'] + self.data['ask'])/2.0
            self.data['value'] = self.data['mid']
        elif sr["type"] == "HEARTBEAT":
            self._rtype = HEARTBEAT
        else:
            raise ValueError("Unknown stream record type {}".format(s))

        # use calendar.timegm, this gives back the correct time without
        # timezone differences
        dt = parse_date(sr['time'])
        self.epoch = int(calendar.timegm(dt.timetuple()))
        self.data['time'] = sr["time"]

    @property
    def recordtype(self):
        return self._rtype

    def __getitem__(self, k):
        return self.data[k]

    def __repr__(self):
        return json.dumps(self.data)
