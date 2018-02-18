# -*- coding: utf-8 -*-
"""Trades definitions."""

definitions = {
    "TradeState": {
        "OPEN": "The Trade is currently open",
        "CLOSED": "The Trade has been fully closed",
        "CLOSE_WHEN_TRADABLE": "The Trade will be closed as soon as the "
                               "trade’s instrument becomes tradeable"
    },
    "TradeStateFilter": {
        "OPEN": "The Trades that are currently open",
        "CLOSED": "The Trades that have been fully closed",
        "CLOSE_WHEN_TRADEABLE": "The Trades that will be closed as soon as "
                                "the trades' instrument becomes tradeable",
        "ALL": "The Trades that are in any of the possible states listed "
               "above."
    },
    "TradePL": {
        "POSITIVE": "An open Trade currently has a positive (profitable) "
                    "unrealized P/L, or a closed Trade realized a positive "
                    "amount of P/L.",
        "NEGATIVE": "An open Trade currently has a negative (losing) "
                    "unrealized P/L, or a closed Trade realized a negative "
                    "amount of P/L",
        "ZERO": "An open Trade currently has unrealized P/L of zero "
                "(neither profitable nor losing), or a closed Trade realized "
                "a P/L amount of zero."
    }
}
