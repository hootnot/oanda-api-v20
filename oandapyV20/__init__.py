__title__ = "OANDA REST V20 API Wrapper"
__version__ = "0.1.0"
__author__ = "Feite Brekeveld"
__license__ = "MIT"
__copyright__ = "Copyright 2016 Feite Brekeveld"

# Version synonym
VERSION = __version__
from .oandapyV20 import API
from .exceptions import V20Error
