# -*- coding: utf-8 -*-
"""Transactions definitions."""

definitions = {
    "TransactionType": {
        "CREATE": "Account Create Transaction",
        "CLOSE": "Account Close Transaction",
        "REOPEN": "Account Reopen Transaction",
        "CLIENT_CONFIGURE": "Client Configuration Transaction",
        "CLIENT_CONFIGURE_REJECT": "Client Configuration Reject Transaction",
        "TRANSFER_FUNDS": "Transfer Funds Transaction",
        "TRANSFER_FUNDS_REJECT": "Transfer Funds Reject Transaction",
        "MARKET_ORDER": "Market Order Transaction",
        "MARKET_ORDER_REJECT": "Market Order Reject Transaction",
        "LIMIT_ORDER": "Limit Order Transaction",
        "LIMIT_ORDER_REJECT": "Limit Order Reject Transaction",
        "STOP_ORDER": "Stop Order Transaction",
        "STOP_ORDER_REJECT": "Stop Order Reject Transaction",
        "MARKET_IF_TOUCHED_ORDER": "Market if Touched Order Transaction",
        "MARKET_IF_TOUCHED_ORDER_REJECT": "Market if Touched Order "
                                          "Reject Transaction",
        "TAKE_PROFIT_ORDER": "Take Profit Order Transaction",
        "TAKE_PROFIT_ORDER_REJECT": "Take Profit Order Reject Transaction",
        "STOP_LOSS_ORDER": "Stop Loss Order Transaction",
        "STOP_LOSS_ORDER_REJECT": "Stop Loss Order Reject Transaction",
        "TRAILING_STOP_LOSS_ORDER": "Trailing Stop Loss Order Transaction",
        "TRAILING_STOP_LOSS_ORDER_REJECT": "Trailing Stop Loss Order "
                                           "Reject Transaction",
        "ORDER_FILL": "Order Fill Transaction",
        "ORDER_CANCEL": "Order Cancel Transaction",
        "ORDER_CLIENT_EXTENSIONS_MODIFY": "Order Client Extensions "
                                          "Modify Transaction",
        "ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT": "Order Client Extensions "
                                          "Modify Reject Transaction",
        "TRADE_CLIENT_EXTENSIONS_MODIFY": "Trade Client Extensions "
                                          "Modify Transaction",
        "TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT": "Trade Client Extensions "
                                                 "Modify Reject Transaction",
        "MARGIN_CALL_ENTER": "Margin Call Enter Transaction",
        "MARGIN_CALL_EXTEND": "Margin Call Extend Transaction",
        "MARGIN_CALL_EXIT": "Margin Call Exit Transaction",
        "DAILY_FINANCING": "Daily Financing Transaction",
        "RESET_RESETTABLE_PL": "Reset Resettable PL Transaction",
    },
    "FundingReason": {
        "CLIENT_FUNDING": "The client has initiated a funds transfer",
        "ACCOUNT_TRANSFER": "Funds are being transfered between "
                            "two Accounts.",
        "DIVISION_MIGRATION": "Funds are being transfered as part of a "
                              "Division migration",
        "SITE_MIGRATION": "Funds are being transfered as part of a "
                          "Site migration",
        "ADJUSTMENT": "Funds are being transfered as part of an "
                      "Account adjustment"
    },
    "MarketOrderReason": {
        "CLIENT_ORDER": "The Market Order was created at the request "
                        "of a client",
        "TRADE_CLOSE": "The Market Order was created to close a Trade "
                       "at the request of a client",
        "POSITION_CLOSEOUT": "The Market Order was created to close a "
                             "Position at the request of a client",
        "MARGIN_CLOSEOUT": "The Market Order was created as part of a "
                           "Margin Closeout",
        "DELAYED_TRADE_CLOSE": "The Market Order was created to close a "
                               "trade marked for delayed closure",
    },
    "LimitOrderReason": {
        "CLIENT_ORDER": "The Limit Order was initiated at the request of a "
                        "client",
        "REPLACEMENT": "The Limit Order was initiated as a replacement for "
                       "an existing Order",
    },
    "StopOrderReason": {
        "CLIENT_ORDER": "The Stop Order was initiated at the request of a "
                        "client",
        "REPLACEMENT": "The Stop Order was initiated as a replacement for "
                       "an existing Order",
    },
    "MarketIfTouchedOrderReason": {
        "CLIENT_ORDER": "The Market-if-touched Order was initiated at the "
                        "request of a client",
        "REPLACEMENT": "The Market-if-touched Order was initiated as a "
                       "replacement for an existing Order",
    },
    "TakeProfitOrderReason": {
        "CLIENT_ORDER": "The Take Profit Order was initiated at the request "
                        "of a client",
        "REPLACEMENT": "The Take Profit Order was initiated as a replacement "
                       "for an existing Order",
        "ON_FILL": "The Take Profit Order was initiated automatically when "
                   "an Order was filled that opened a new Trade requiring "
                   "a Take Profit Order.",
    },
    "StopLossOrderReason": {
        "CLIENT_ORDER": "The Stop Loss Order was initiated at the request "
                        "of a client",
        "REPLACEMENT": "The Stop Loss Order was initiated as a replacement "
                       "for an existing Order",
        "ON_FILL": "The Stop Loss Order was initiated automatically when "
                   "an Order was filled that opened a new Trade requiring "
                   "a Stop Loss Order.",
    },
    "TrailingStopLossOrderReason": {
        "CLIENT_ORDER": "The Trailing Stop Loss Order was initiated at the "
                        "request of a client",
        "REPLACEMENT": "The Trailing Stop Loss Order was initiated as a "
                       "replacement for an existing Order",
        "ON_FILL": "The Trailing Stop Loss Order was initiated automatically "
                   "when an Order was filled that opened a new Trade "
                   "requiring a Trailing Stop Loss Order.",
    },
    "OrderFillReason": {
        "LIMIT_ORDER": "The Order filled was a Limit Order",
        "STOP_ORDER": "The Order filled was a Stop Order",
        "MARKET_IF_TOUCHED_ORDER": "The Order filled was a "
                                   "Market-if-touched Order",
        "TAKE_PROFIT_ORDER": "The Order filled was a Take Profit Order",
        "STOP_LOSS_ORDER": "The Order filled was a Stop Loss Order",
        "TRAILING_STOP_LOSS_ORDER": "The Order filled was a Trailing Stop "
                                    "Loss Order",
        "MARKET_ORDER": "The Order filled was a Market Order",
        "MARKET_ORDER_TRADE_CLOSE": "The Order filled was a Market Order "
                                    "used to explicitly close a Trade",
        "MARKET_ORDER_POSITION_CLOSEOUT": "The Order filled was a Market "
                                          "Order used to explicitly close "
                                          "a Position",
        "MARKET_ORDER_MARGIN_CLOSEOUT": "The Order filled was a Market Order "
                                        "used for a Margin Closeout",
        "MARKET_ORDER_DELAYED_TRADE_CLOSE": "The Order filled was a Market "
                                            "Order used for a delayed Trade "
                                            "close",
    },
    "OrderCancelReason": {
        "INTERNAL_SERVER_ERROR": "The Order was cancelled because at the"
                                 "time of filling, an unexpected internal "
                                 "server error occurred.",
        "ACCOUNT_LOCKED": "The Order was cancelled because at the time of "
                          "filling the account was locked.",
        "ACCOUNT_NEW_POSITIONS_LOCKED": "The order was to be filled, "
                                        "however the account is configured "
                                        "to not allow new positions to be "
                                        "created.",
        "ACCOUNT_ORDER_CREATION_LOCKED": "Filling the Order wasn’t possible "
                                         "because it required the creation "
                                         "of a dependent Order and the "
                                         "Account is locked for Order "
                                         "creation.",
        "ACCOUNT_ORDER_FILL_LOCKED": "Filling the Order was not possible "
                                     "because the Account is locked for "
                                     "filling Orders.",
        "CLIENT_REQUEST": "The Order was cancelled explicitly at the request "
                          "of the client.",
        "MIGRATION": "The Order cancelled because it is being migrated to "
                     "another account.",
        "MARKET_HALTED": "Filling the Order wasn’t possible because the "
                         "Order’s instrument was halted.",
        "LINKED_TRADE_CLOSED": "The Order is linked to an open Trade that "
                               "was closed.",
        "TIME_IN_FORCE_EXPIRED": "The time in force specified for this order "
                                 "has passed.",
        "INSUFFICIENT_MARGIN": "Filling the Order wasn’t possible because "
                               "the Account had insufficient margin.",
        "FIFO_VIOLATION": "Filling the Order would have resulted in a FIFO "
                          "violation.",
        "BOUNDS_VIOLATION": "Filling the Order would have violated the "
                            "Order’s price bound.",
        "CLIENT_REQUEST_REPLACED": "The Order was cancelled for replacement "
                                   "at the request of the client.",
        "INSUFFICIENT_LIQUIDITY": "Filling the Order wasn’t possible "
                                  "because enough liquidity available.",
        "TAKE_PROFIT_ON_FILL_GTD_TIMESTAMP_IN_PAST":
            "Filling the Order would have resulted in the creation "
            "of a Take Profit Order with a GTD time in the past.",
        "TAKE_PROFIT_ON_FILL_LOSS":
            "Filling the Order would result in the creation of a "
            "Take Profit Order that would have been filled immediately, "
            "closing the new Trade at a loss.",
        "LOSING_TAKE_PROFIT":
            "Filling the Order would result in the creation of a "
            "Take Profit Loss Order that would close the new Trade "
            "at a loss when filled.",
        "STOP_LOSS_ON_FILL_GTD_TIMESTAMP_IN_PAST":
            "Filling the Order would have resulted in the creation of a "
            "Stop Loss Order with a GTD time in the past.",
        "STOP_LOSS_ON_FILL_LOSS":
            "Filling the Order would result in the creation of a "
            "Stop Loss Order that would have been filled immediately, "
            "closing the new Trade at a loss.",
        "TRAILING_STOP_LOSS_ON_FILL_GTD_TIMESTAMP_IN_PAST":
            "Filling the Order would have resulted in the creation of a"
            "Trailing Stop Loss Order with a GTD time in the past.",
        "CLIENT_TRADE_ID_ALREADY_EXISTS":
            "Filling the Order would result in the creation of a "
            "new Open Trade with a client Trade ID already in use.",
        "POSITION_CLOSEOUT_FAILED": "Closing out a position wasn’t "
                                    "fully possible.",
        "OPEN_TRADES_ALLOWED_EXCEEDED":
            "Filling the Order would cause the maximum open trades "
            "allowed for the Account to be exceeded.",
        "PENDING_ORDERS_ALLOWED_EXCEEDED":
            "Filling the Order would have resulted in exceeding the "
            "number of pending Orders allowed for the Account.",
        "TAKE_PROFIT_ON_FILL_CLIENT_ORDER_ID_ALREADY_EXISTS":
            "Filling the Order would have resulted in the creation of "
            "a Take Profit Order with a client Order ID that is already "
            "in use.",
        "STOP_LOSS_ON_FILL_CLIENT_ORDER_ID_ALREADY_EXISTS":
            "Filling the Order would have resulted in the creation of a "
            "Stop Loss Order with a client Order ID that is already in use.",
        "TRAILING_STOP_LOSS_ON_FILL_CLIENT_ORDER_ID_ALREADY_EXISTS":
            "Filling the Order would have resulted in the creation of a "
            "Trailing Stop Loss Order with a client Order ID that is "
            "already in use.",
        "POSITION_SIZE_EXCEEDED":
            "Filling the Order would have resulted in the "
            "Account’s maximum position size limit being exceeded "
            "for the Order’s instrument.",
    },
}
