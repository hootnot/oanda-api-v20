# -*- coding: utf-8 -*-
import re


def granularity_to_time(granularity):
    """get value in seconds for named granularities: M1, M5 ... H1 etc.

    Parameters
    ----------

    granularity : string
        granularity string specifying seconds, minitues, hours, days
        Granularities of days is of no use for generating candles
        from a stream.
    """
    mfact = {
        'S': 1,
        'M': 60,
        'H': 3600,
        'D': 86400,
    }
    try:
        f, n = re.match("(?P<f>[SMHD])(?:(?P<n>\d+)|)", granularity).groups()
        n = int(n) if n else 1
        return mfact[f] * n
    except:
        raise ValueError("Can't handle granularity: {}".format(granularity))


