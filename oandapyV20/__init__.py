import logging
from .oandapyV20 import API
from .exceptions import V20Error

__title__ = "OANDA REST V20 API Wrapper"
__version__ = "0.7.2"
__author__ = "Feite Brekeveld"
__license__ = "MIT"
__copyright__ = "Copyright 2016 - 2018 Feite Brekeveld"

# Version synonym
VERSION = __version__

# Set default logging handler to avoid "No handler found" warnings.
try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())

__all__ = (
    'API',
    'V20Error'
)
