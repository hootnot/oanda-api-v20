# -*- encoding: utf-8 -*-
"""Retrieve candle data."""
import argparse
import json
import sys
from oandapyV20 import API
from oandapyV20.exceptions import V20Error
import oandapyV20.endpoints.instruments as instruments
from exampleauth import exampleAuth


# constants
granularities = instruments.definitions["CandlestickGranularity"].keys()
granularities = sorted(granularities)

# create the top-level parser
parser = argparse.ArgumentParser(prog='candle-data')
parser.add_argument('--nice', action='store_true', help='json indented')
parser.add_argument('--count', default=5, type=int, help='num recs')
parser.add_argument('--granularity', choices=granularities, required=True)
parser.add_argument('--instruments', type=str, nargs='?',
                    action='append', help='instruments')


class Main(object):
    def __init__(self, api, accountID, clargs):
        self._accountID = accountID
        self.clargs = clargs
        self.api = api

    def main(self):

        if self.clargs.instruments:
            params = {"count": self.clargs.count,
                      "granularity": self.clargs.granularity}
            for i in self.clargs.instruments:
                r = instruments.InstrumentsCandles(instrument=i, params=params)
                rv = self.api.request(r)
                kw = {}
                if self.clargs.nice:
                    kw = {"indent": self.clargs.nice}
                print("{}".format(json.dumps(rv, **kw)))

            return

        raise ValueError


if __name__ == "__main__":
    clargs = parser.parse_args()

    accountID, token = exampleAuth()
    api = API(access_token=token,
              headers={"Content-Type": "application/json"})
    try:
        m = Main(api=api, accountID=accountID, clargs=clargs)
        m.main()
    except ValueError as e:
        parser.parse_args(["--help"])
    except V20Error as v20e:
        print("ERROR {} {}".format(v20e.code, v20e.msg))
    else:
        print("Unkown error: {}".format(e))
