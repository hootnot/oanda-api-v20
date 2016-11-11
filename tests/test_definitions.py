import sys
import unittest
import requests_mock

import oandapyV20.definitions as allDEF
from oandapyV20.definitions.orders import definitions as orderDefs


class TestDefinitions(unittest.TestCase):
    """Tests regarding the definitions."""

    def test__order_definitions(self):
        """test for the dynamically generated definition classes."""
        c = allDEF.orders.OrderType()
        self.assertTrue(isinstance(c, allDEF.orders.OrderType) and
                        c['MARKET'] == orderDefs['OrderType']['MARKET'])


if __name__ == "__main__":

    unittest.main()
