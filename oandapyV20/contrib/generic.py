import re
import time
from datetime import datetime


def secs2time(e):
    """secs2time - convert epoch to datetime.

    >>> d = secs2time(1497499200)
    >>> d
    datetime.datetime(2017, 6, 15, 4, 0)
    >>> d.strftime("%Y%m%d-%H:%M:%S")
    '20170615-04:00:00'
    """
    w = time.gmtime(e)
    return datetime(*list(w)[0:6])


def granularity_to_time(s):
    """convert a named granularity into seconds.

    get value in seconds for named granularities: M1, M5 ... H1 etc.

    >>> print(granularity_to_time("M5"))
    300
    """
    mfact = {
        'S': 1,
        'M': 60,
        'H': 3600,
        'D': 86400,
    }
    try:
        f, n = re.match("(?P<f>[SMHD])(?:(?P<n>\d+)|)", s).groups()
        n = n if n else 1
        return mfact[f] * int(n)

    except Exception as e:
        raise ValueError(e)
