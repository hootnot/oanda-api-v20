# -*- coding: utf-8 -*-
"""Order related definitions."""

definitions = {
    "OrderType": {
        "MARKET": "A Market Order",
        "LIMIT": "A Limit Order",
        "STOP": "A Stop Order",
        "MARKET_IF_TOUCHED": "A Market-if-touched Order",
        "TAKE_PROFIT": "A Take Profit Order",
        "STOP_LOSS": "A Stop Loss Order",
        "TRAILING_STOP_LOSS": "A Trailing Stop Loss Order"
    },
    "CancellableOrderType": {
        "LIMIT": "A Limit Order",
        "STOP": "A Stop Order",
        "MARKET_IF_TOUCHED": "A Market-if-touched Order",
        "TAKE_PROFIT": "A Take Profit Order",
        "STOP_LOSS": "A Stop Loss Order",
        "TRAILING_STOP_LOSS": "A Trailing Stop Loss Order",
    },
    "OrderState": {
        "PENDING": "The Order is currently pending execution",
        "FILLED": "The Order has been filled",
        "TRIGGERED": "The Order has been triggered",
        "CANCELLED": "The Order has been cancelled",
    },
    "OrderStateFilter": {
        "PENDING": "The orders that are currently pending execution",
        "FILLED": "The orders that have been filled",
        "TRIGGERED": "The orders that have been triggered",
        "CANCELLED": "The orders that have been cancelled",
        "ALL": "The orders that are in any of the possible states: "
               "PENDING, FILLED, TRIGGERED, CANCELLED",
    },
    "TimeInForce": {
        "GTC": "The Order is “Good unTil Cancelled”",
        "GTD": "The Order is “Good unTil Date” and will be cancelled at "
               "the provided time",
        "GFD": "The Order is “Good for Day” and will be cancelled at "
               "5pm New York time",
        "FOK": "The Order must be immediately “Filled Or Killed”",
        "IOC": "The Order must be “Immediately partially filled Or Killed”",
    },
    "OrderPositionFill": {
        "OPEN_ONLY": "When the Order is filled, only allow Positions to be "
                     "opened or extended.",
        "REDUCE_FIRST": "When the Order is filled, always fully reduce an "
                        "existing Position before opening a new Position.",
        "REDUCE_ONLY": "When the Order is filled, only reduce an existing "
                       "Position.",
        "DEFAULT": "When the Order is filled, use REDUCE_FIRST behaviour "
                   "for non-client hedging Accounts, and OPEN_ONLY behaviour "
                   "for client hedging Accounts."
    },
    "OrderTriggerCondition": {
        "DEFAULT": "Trigger an Order the “natural” way: compare its price to "
                   "the ask for long Orders and bid for short Orders",
        "INVERSE": "Trigger an Order the opposite of the “natural” way: "
                   "compare its price the bid for long Orders and ask for "
                   "short Orders.",
        "BID": "Trigger an Order by comparing its price to the bid regardless"
               " of whether it is long or short.",
        "ASK": "Trigger an Order by comparing its price to the ask regardless"
               " of whether it is long or short.",
        "MID": "Trigger an Order by comparing its price to the midpoint "
               "regardless of whether it is long or short."
    }
}
