# -*- coding: utf-8 -*-

import time
from datetime import datetime
import calendar

import oandapyV20.endpoints.instruments as instruments
from oandapyV20.contrib.generic import granularity_to_time


def secs2time(e):
    w = time.gmtime(e)
    return datetime(*list(w)[0:6])


def CandleHistoryRequest(instrument, params):
    """create a CandleHistoryRequest.

    CandleHistoryRequest is used to retrieve historical data, automatically
    generating sequential requests when the OANDA limit of 'count' records is
    exceeded.

    This is known by:
    - count is specified as a number larger than 5000
    - difference between 'from' and 'to' with the granularity specified is
      larger than 5000


    If only count is specified, count should be <= the OANDA limit of 5000.
    If more we can't tell for sure where to start back in time because the
    startdate depends for instance  on the granularity and possible holidays.
    So, if more than 5000 records are specified a ValueError is raised.

    If more than 5000 records are needed, specify the 'from' date and
    optionally and 'to' date. If 'to' is not specified 'now' will be used.


    Parameters
    ----------

    instrument : string (required)
        the instrument to create the order for

    params: params (required)
        the parameters to specify the historical range,
        see the REST-V20 docs regarding 'instrument' at developer.oanda.com

    Example
    -------

    >>> import json
    >>> from oandapyV20 import API
    >>> import oandapyV20.endpoints.orders as orders
    >>> from oandapyV20.contrib.factories import CandleHistoryRequest
    >>>
    >>> accountID = "..."
    >>> client = API(access_token=...)
    >>> params = {
    ...    "from": "2017-01-01T00:00:00Z",
    ...    "to": "2017-03-01T00:00:00Z",
    ...    "granularity": "M5"
    ... }
    >>> ch = CandleHistoryRequest(instrument="EUR_USD", params=params)
    >>> # CandleHistoryRequest returns a generator, generating subsequent
    >>> # requests to retrieve full history from date 'from' till 'to'
    >>> with open("/tmp/hist", "w") as H:
    >>>     for r in ch:
    >>>         client.request(r)
    >>>         H.write(json.dumps(r.response, indent=2))
    """
    fmt = "%Y-%m-%dT%H:%M:%SZ"

    # if not specified use the default of 'S5' as OANDA does
    gs = granularity_to_time(params.get('granularity', 'S5'))

    _from = datetime.strptime(params.get('from'), fmt)

    _to = datetime.now()
    if 'to' in params:
        _to = datetime.strptime(params.get('to'), fmt)
    ep_from = int(calendar.timegm(_from.timetuple()))
    ep_to = int(calendar.timegm(_to.timetuple()))
    cnt = params.get('count', 500)

    delta = ep_to - ep_from
    nbars = delta/gs

    # a list of dates
    lod = [ep_from, ep_to]
    # do we need to split the range in a list ?
    if nbars > cnt:
        i = 1
        # insert the others
        while nbars - cnt > 0:
            nbars -= cnt
            lod.insert(i, lod[i-1]+cnt*gs)
            i += 1

    cpparams = params.copy()
    for k in ['from', 'to']:
        if k in cpparams:
            del cpparams[k]

    i = 0
    while i < len(lod)-1:
        params = cpparams.copy()
        params.update({"from": secs2time(lod[i]).strftime(fmt)})
        # if it is the secondlast date, skip the 'to' parameter
        # the default count will do, it avoids errors from OANDA regarding
        # future dates
        if i < len(lod)-2:
            params.update({"to": secs2time(lod[i+1]).strftime(fmt)})
        yield instruments.InstrumentsCandles(instrument=instrument,
                                             params=params)
        i += 1
