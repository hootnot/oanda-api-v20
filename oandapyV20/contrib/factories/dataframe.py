# -*- coding: utf-8 -*-
import pandas as pd

from .conv import convrec, column_map_tohlcv


def DataFrameFactory(r, column_map=column_map_tohlcv, conv=convrec):
    """DataFrameFactory - return a dataframe for candles.

    create a DataFrame from candle records by dynamically converting them
    accoring the column_map config.

    >>> column_map_tcv = OrderedDict([
    ...   ('time', 'Time'),
    ...   ('mid:c', 'Close'),
    ...   ('volume', 'Volume')
    ... ])
    >>> params = {"instruments": "EUR_USD,EUR_GBP"}
    >>> r = instruments.InstrumentsCandles(instrument=instr, params=params)
    >>> api.request(r)
    >>> for _r in DataFrameFactory(r.response):
    >>>     print(_r.head())
    >>> for _r in DataFrameFactory(r.response, column_map=column_map_tcv):
    >>>     print(_r.head())
    """
    df = pd.DataFrame([list(conv(_r, column_map)) for _r in r.get('candles')])
    df.columns = list(column_map.values())
    df = df.set_index('Time')
    return df
