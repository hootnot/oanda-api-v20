# -*- coding: utf-8 -*-

from datetime import datetime
import calendar
import logging

import oandapyV20.endpoints.instruments as instruments
from oandapyV20.contrib.generic import granularity_to_time, secs2time


logger = logging.getLogger(__name__)

MAX_BATCH = 5000
DEFAULT_BATCH = 500


def InstrumentsCandlesFactory(instrument, params=None):
    """InstrumentsCandlesFactory - generate InstrumentCandles requests.

    InstrumentsCandlesFactory is used to retrieve historical data by
    automatically generating consecutive requests when the OANDA limit
    of *count* records is exceeded.

    This is known by calculating the number of candles between *from* and
    *to*. If *to* is not specified *to* will be equal to *now*.

    The *count* parameter is only used to control the number of records to
    retrieve in a single request.

    The *includeFirst* parameter is forced to make sure that results do
    no have a 1-record gap between consecutive requests.

    Parameters
    ----------

    instrument : string (required)
        the instrument to create the order for

    params: params (optional)
        the parameters to specify the historical range,
        see the REST-V20 docs regarding 'instrument' at developer.oanda.com
        If no params are specified, just a single InstrumentsCandles request
        will be generated acting the same as if you had just created it
        directly.

    Example
    -------

    The *oandapyV20.API* client processes requests as objects. So,
    downloading large historical batches simply comes down to:

    >>> import json
    >>> from oandapyV20 import API
    >>> from oandapyV20.contrib.factories import InstrumentsCandlesFactory
    >>>
    >>> client = API(access_token=...)
    >>> instrument, granularity = "EUR_USD", "M15"
    >>> _from = "2017-01-01T00:00:00Z"
    >>> params = {
    ...    "from": _from,
    ...    "granularity": granularity,
    ...    "count": 2500,
    ... }
    >>> with open("/tmp/{}.{}".format(instrument, granularity), "w") as OUT:
    >>>     # The factory returns a generator generating consecutive
    >>>     # requests to retrieve full history from date 'from' till 'to'
    >>>     for r in InstrumentsCandlesFactory(instrument=instrument,
    ...                                        params=params)
    >>>         client.request(r)
    >>>         OUT.write(json.dumps(r.response.get('candles'), indent=2))

    .. note:: Normally you can't combine *from*, *to* and *count*.
              When *count* specified, it is used to calculate the gap between
              *to* and *from*. The *params* passed to the generated request
              itself does contain the *count* parameter.

    """
    RFC3339 = "%Y-%m-%dT%H:%M:%SZ"

    # if not specified use the default of 'S5' as OANDA does
    gs = granularity_to_time(params.get('granularity', 'S5'))

    _from = None
    _epoch_from = None
    if 'from' in params:
        _from = datetime.strptime(params.get('from'), RFC3339)
        _epoch_from = int(calendar.timegm(_from.timetuple()))

    _to = datetime.utcnow()
    if 'to' in params:
        _tmp = datetime.strptime(params.get('to'), RFC3339)
        # if specified datetime > now, we use 'now' instead
        if _tmp > _to:
            logger.info("datetime %s is in the future, will be set to 'now'",
                        params.get('to'))
        else:
            _to = _tmp

    _epoch_to = int(calendar.timegm(_to.timetuple()))

    _count = params.get('count', DEFAULT_BATCH)
    # OANDA will respond with a V20Error if count > MAX_BATCH

    if 'to' in params and 'from' not in params:
        raise ValueError("'to' specified without 'from'")

    if not params or 'from' not in params:
        yield instruments.InstrumentsCandles(instrument=instrument,
                                             params=params)

    else:
        delta = _epoch_to - _epoch_from
        nbars = delta / gs

        cpparams = params.copy()
        for k in ['count', 'from', 'to']:
            if k in cpparams:
                del cpparams[k]
        # force includeFirst
        cpparams.update({"includeFirst": True})

        # generate InstrumentsCandles requests for all 'bars', each request
        # requesting max. count records
        for _ in range(_count, int(((nbars//_count)+1))*_count+1, _count):
            to = _epoch_from + _count * gs
            if to > _epoch_to:
                to = _epoch_to
            yparams = cpparams.copy()
            yparams.update({"from": secs2time(_epoch_from).strftime(RFC3339)})
            yparams.update({"to": secs2time(to).strftime(RFC3339)})
            yield instruments.InstrumentsCandles(instrument=instrument,
                                                 params=yparams)
            _epoch_from = to
