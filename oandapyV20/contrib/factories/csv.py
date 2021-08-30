# -*- coding: utf-8 -*-
from .conv import convrec, column_map_tohlcv


def CSVFactory(r, conv=convrec, column_map=column_map_tohlcv, delim=","):
    """CSVFactory - convert candlerecords to CSV strings.

    Dynamically convert candlerecords to CSV strings by the configuration
    passed by *conf*.

    >>> column_map_tcv = OrderedDict([
    ...   ('time', 'Time'),
    ...   ('mid:c', 'Close'),
    ...   ('volume', 'Volume')
    ... ])
    >>> params = {"count": 50,
    ...           "granularity": "D"}
    >>> instr = "EUR_USD"
    >>> r = instruments.InstrumentsCandles(instrument=instr, params=params)
    >>> api.request(r)
    >>> for _r in CSVFactory(r.response):
    >>>     print(_r)
    >>> for _r in CSVFactory(r.response, column_map=column_map_tcv, delim="|"):
    >>>     print(_r)
    """
    for rec in r.get('candles'):
        # make all values strings before join
        yield delim.join([str(x) for x in list(conv(rec, column_map))])
