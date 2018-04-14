# -*- coding: utf-8 -*-
"""Account Definitions."""

definitions = {
    "GuaranteedStopLossOrderMode": {
        "DISABLED": "The account is not permitted to create guaranteed "
                    "Stop Loss Orders.",
        "ALLOWED": "The account is able, but not required to have guaranteed "
                    "Stop Loss Orders for open Trades.",
        "REQUIRED": "The account is required to have guaranteed "
                    "Stop Loss Orders for open Trades.",
    },
    "AccountFinancingMode": {
        "NO_FINANCING": "No financing is paid/charged for open Trades "
                        "in the Account",
        "SECOND_BY_SECOND": "Second-by-second financing is paid/charged "
                            "for open Trades in the Account, both daily "
                            "and when the the Trade is closed",
        "DAILY": "A full day’s worth of financing is paid/charged for "
                 "open Trades in the Account daily at 5pm New York time"
    },
    "PositionAggregationMode": {
        "ABSOLUTE_SUM": "The Position value or margin for each side (long and"
                        " short) of the Position are computed independently "
                        "and added together.",
        "MAXIMAL_SIDE": "The Position value or margin for each side (long and"
                        " short) of the Position are computed independently. "
                        "The Position value or margin chosen is the maximal "
                        "absolute value of the two.",
        "NET_SUM": "The units for each side (long and short) of the Position "
                   "are netted together and the resulting value (long or "
                   "short) is used to compute the Position value or margin."
    }
}
