# -*- coding: utf-8 -*-
from collections import OrderedDict

column_map_tohlcv = OrderedDict([
    ('time', 'Time'),
    ('mid:o', 'Open'),
    ('mid:h', 'High'),
    ('mid:l', 'Low'),
    ('mid:c', 'Close'),
    ('volume', 'Volume')
])


def convrec(r, m):
    """convrec - convert OANDA candle record.

    return array of values, dynamically constructed, corresponding
    with config in mapping m.
    """
    v = []
    for keys in [x.split(":") for x in m.keys()]:
        _v = r.get(keys[0])
        for k in keys[1:]:
            _v = _v.get(k)
        v.append(_v)

    return v
