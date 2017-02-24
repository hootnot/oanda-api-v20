# -*- coding: utf-8 -*-
import sys
import time
from datetime import datetime
import re
from oandapyV20.contrib.stream.streamrecord import HEARTBEAT, PRICE
import logging


atEndOfTimeFrame = 1
dancingBear = 2
dancingBearHighLowExtreme = 3

logger = logging.getLogger(__name__)


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


class CandleFactory(object):
    """CandleFactory - class to produce candle records.

    The CandleFactory class produces candle records for the specified
    instruments and timeframes.
    """

    def __init__(self, instruments):
        """instantiate a CandleFactory.

        Parameters
        ----------

        instruments: list of dicts
             a list the specifies the instruments and granularities, ex.:
             [ { "DE30_EUR": ["M1", "M5"]}, {"EUR_USD": ["M15", "H1"]} ]
        """
        self._halls = {}
        logger.info("set up candle factory ")
        for ih in instruments:
            instrument, grans = ih.items()[0]
            logger.info("set up candle factory grans: %s", ",".join(grans))
            self._halls.update(
                {instrument:
                 [CandleFactoryHall(instrument, g) for g in grans]})
            logger.info("set up candle factory for: %s %s",
                        instrument, ",".join(grans))

    def processTick(self, tick):
        """processTick - process a tick record.

        The tick record of a certain instrument is processed to make
        candle records for the instrument.
        In case the tick is a HEARTBEAT record, all instruments are processed
        to see if the heartbeat tick did complete the timeframe. If so, the
        record is returned as 'completed'.
        """
        if tick.recordtype() == TICK:
            instrument = tick["instrument"]
            logger.info("process PriceTick for: %s", instrument)
            for G in self._halls[instrument]:
                logger.info("process PriceTick for: %s", G.granularity)
                yield G.processTick(tick)
        else:
            for k, v in self._halls.items():
                logger.info("process HB-Tick for: %s ", k)
                for G in self._halls[k]:
                    logger.info("... for: %s ", G.granularity)
                    yield G.processTick(tick)


class CandleFactoryHall(object):
    """Create candle records for a given instruments/timeframes.

    process tickrecords until the timeframe is passed, then return the
    data as a 'completed'-candle.

    Parameters
    ----------

    instrument : sting
        the instrument to process the ticks for.

    granularity : string
        a granularity expressed in minutes(M), hours(H), days(D), ex.:
        M1, M2, M5, ... H4, D

    processingMode: string
        defaults to 'atEndOfTimeFrame'. Other options are:
        'dancingBear' which will return the incomplete status of the candle
        while processing ticks until the timeframe is reached and it is
        complete
        'dancingBearHighLowExtreme' returns the incomplete candle also, but
        only when a new high or a new low is set.

    Examples
    --------

    ...
    cfHall = {}
    for g in ["M1", "M5"]:
        cfHall[g] = CandleFactoryHall(instrument="EUR_USD", granularity=g)

    # start processing ticks
    r = PricingStream(accountID=accountID, params={"instruments", ["EUR_USD"])
    for tick in api.request(r):
        for g in ["M1", "M5"]:
            # the factory returns the candle record when it is completed
            rv = cfHall[g].processTick(tick)
            if rv:
                print(rv)
    """

    def __init__(self, instrument, granularity,
                 processingMode='atEndOfTimeFrame'):
        self.instrument = instrument
        self.frameTime = granularity_to_time(granularity)
        self.granularity = granularity
        self.data = None
        self.start = None
        self.end = None
        self.processing = None
        self.processingMode = processingMode
        try:
            self.processing = getattr(sys.modules[__name__],
                                      self.processingMode)
        except:
            logger.error("unknown processing mode: %s", self.processingMode)

            self.processingMode = "atEndOfTimeFrame"
            self.processing = getattr(sys.modules[__name__],
                                      self.processingMode)
            logger.info("fallback to processing mode: %s", self.processingMode)
        else:
            logger.info("processing mode: %s", self.processingMode)

    def _initData(self, tick):
        # init the frame
        # calculate the boundaries based on the tick timestamp
        self.start = tick.epoch - (tick.epoch % self.frameTime)
        self.end = tick.epoch - (tick.epoch % self.frameTime) + self.frameTime
        self.data = {
            "instrument": self.instrument,
            "start": "%s" % self.secs2time(self.start),
            "end": "%s" % self.secs2time(self.end),
            "granularity": self.granularity,
            "completed": False,
            "data": {
                "open": tick.data['value'],
                "high": tick.data['value'],
                "low": tick.data['value'],
                "last": tick.data['value'],
                "volume": 1
            }
        }

    def secs2time(self, e):
        w = time.gmtime(e)
        return datetime(*list(w)[0:6])

    def _make_candle(self, completed=False):
        self.data['completed'] = completed
        return self.data.copy()

    def processTick(self, tick):
        return self._processTick(tick)

    def _processTick(self, tick):
        if tick.recordtype() == HEARTBEAT:
            if self.data and tick.epoch > self.end:
                # this frame is completed based on the heartbeat timestamp
                candle = self._make_candle(completed=True)
                self.data = None     # clear it, reinitialized by the next tick
                logger.warn("infrequent ticks: %s, %s completed with "
                            "heartbeat (%d secs)" %
                            (self.instrument, self.granularity,
                             (tick.epoch - self.end)))
                return candle
            else:
                return None

        # so it is TICK record
        if not tick['instrument'] == self.instrument:
            return None

        if not self.data:
            # print "initData(...)"
            self._initData(tick)
            return None

        # ... we got data already
        # is this tick for this frame ? ... process it
        if tick.epoch >= self.start and tick.epoch < self.end:
            extremeChange = False
            lastChange = False
            if tick.data['value'] > self.data['data']['high']:
                self.data['data']['high'] = tick.data['value']
                extremeChange = True
            if tick.data['value'] < self.data['data']['low']:
                self.data['data']['low'] = tick.data['value']
                extremeChange = True
            if tick.data['value'] != self.data['data']['last']:
                self.data['data']['last'] = tick.data['value']
                lastChange = True
            self.data['data']['volume'] += 1
            if self.processing == dancingBear and lastChange or \
               self.processing == dancingBearHighLowExtreme and extremeChange:
                logger.info("mode: %s change of extremes for %s, %s",
                            self.processingMode, self.instrument,
                            self.granularity)
                return self._make_candle()
            return None

        # this tick not within boundaries ?
        # the 'current' is completed
        candle = self._make_candle(completed=True)
        self._initData(tick)
        return candle
