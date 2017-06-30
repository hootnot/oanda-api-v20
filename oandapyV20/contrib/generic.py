import re


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
