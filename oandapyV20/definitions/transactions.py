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
        "ORDER_CANCEL_REJECT": "Order Cancel Reject Transaction",
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
        "DELAYED_TRADE_CLOSURE": "Delayed Trade Closure Transaction",
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
    "MarketOrderMarginCloseoutReason": {
        "MARGIN_CHECK_VIOLATION": "Trade closures resulted from violating "
                                  "OANDA’s margin policy",
        "REGULATORY_MARGIN_CALL_VIOLATION":
            "Trade closures came from a margin closeout event resulting "
            "from regulatory conditions placed on the Account’s margin call"
    },
    "TransactionRejectReason": {
        "INTERNAL_SERVER_ERROR": "An unexpected internal server error has "
                                 "occurred",
        "INSTRUMENT_PRICE_UNKNOWN": "The system was unable to determine the "
                                    "current price for the Order’s instrument",
        "ACCOUNT_NOT_ACTIVE": "The Account is not active",
        "ACCOUNT_LOCKED": "The Account is locked",
        "ACCOUNT_ORDER_CREATION_LOCKED": "The Account is locked for Order "
                                         "creation",
        "ACCOUNT_CONFIGURATION_LOCKED": "The Account is locked for "
                                        "configuration",
        "ACCOUNT_DEPOSIT_LOCKED": "The Account is locked for deposits",
        "ACCOUNT_WITHDRAWAL_LOCKED": "The Account is locked for withdrawals",
        "ACCOUNT_ORDER_CANCEL_LOCKED": "The Account is locked for Order "
                                       "cancellation",
        "INSTRUMENT_NOT_TRADEABLE": "The instrument specified is not "
                                    "tradeable by the Account",
        "PENDING_ORDERS_ALLOWED_EXCEEDED": "Creating the Order would result "
                                           "in the maximum number of allowed "
                                           "pending Orders being exceeded",
        "ORDER_ID_UNSPECIFIED": "Neither the Order ID nor client Order ID "
                                "are specified",
        "ORDER_DOESNT_EXIST": "The Order specified does not exist",
        "ORDER_IDENTIFIER_INCONSISTENCY": "The Order ID and client Order ID "
                                          "specified do not identify the "
                                          "same Order",
        "TRADE_ID_UNSPECIFIED": "Neither the Trade ID nor client Trade ID "
                                "are specified",
        "TRADE_DOESNT_EXIST": "The Trade specified does not exist",
        "TRADE_IDENTIFIER_INCONSISTENCY": "The Trade ID and client Trade ID "
                                          "specified do not identify the "
                                          "same Trade",
        "INSTRUMENT_MISSING": "Order instrument has not been specified",
        "INSTRUMENT_UNKNOWN": "The instrument specified is unknown",
        "UNITS_MISSING": "Order units have not been not specified",
        "UNITS_INVALID": "Order units specified are invalid",
        "UNITS_PRECISION_EXCEEDED": "The units specified contain more "
                                    "precision than is allowed for the "
                                    "Order’s instrument",
        "UNITS_LIMIT_EXCEEDED": "The units specified exceeds the maximum "
                                "number of units allowed",
        "UNITS_MIMIMUM_NOT_MET": "The units specified is less than the "
                                 "minimum number of units required",
        "PRICE_MISSING": "The price has not been specified",
        "PRICE_INVALID": "The price specifed is invalid",
        "PRICE_PRECISION_EXCEEDED": "The price specified contains more "
                                    "precision than is allowed for the "
                                    "instrument",
        "PRICE_DISTANCE_MISSING": "The price distance has not been specified",
        "PRICE_DISTANCE_INVALID": "The price distance specifed is invalid",
        "PRICE_DISTANCE_PRECISION_EXCEEDED": "The price distance specified "
                                             "contains more precision than is "
                                             "allowed for the instrument",
        "PRICE_DISTANCE_MAXIMUM_EXCEEDED": "The price distance exceeds that "
                                           "maximum allowed amount",
        "PRICE_DISTANCE_MINIMUM_NOT_MET": "The price distance does not meet "
                                          "the minimum allowed amount",
        "TIME_IN_FORCE_MISSING": "The TimeInForce field has not been "
                                 "specified",
        "TIME_IN_FORCE_INVALID": "The TimeInForce specified is invalid",
        "TIME_IN_FORCE_GTD_TIMESTAMP_MISSING": "The TimeInForce is GTD but no "
                                               "GTD timestamp is provided",
        "TIME_IN_FORCE_GTD_TIMESTAMP_IN_PAST": "The TimeInForce is GTD but "
                                               "the GTD timestamp is in the "
                                               "past",
        "PRICE_BOUND_INVALID": "The price bound specified is invalid",
        "PRICE_BOUND_PRECISION_EXCEEDED": "The price bound specified contains "
                                          "more precision than is allowed for "
                                          "the Order’s instrument",
        "ORDERS_ON_FILL_DUPLICATE_CLIENT_ORDER_IDS":
            "Multiple Orders on fill share the same client Order ID",
        "TRADE_ON_FILL_CLIENT_EXTENSIONS_NOT_SUPPORTED":
            "The Order does not support Trade on fill client extensions "
            "because it cannot create a new Trade",
        "CLIENT_ORDER_ID_INVALID": "The client Order ID specified is invalid",
        "CLIENT_ORDER_ID_ALREADY_EXISTS":
            "The client Order ID specified is already assigned to another "
            "pending Order",
        "CLIENT_ORDER_TAG_INVALID":
            "The client Order tag specified is invalid",
        "CLIENT_ORDER_COMMENT_INVALID":
            "The client Order comment specified is invalid",
        "CLIENT_TRADE_ID_INVALID": "The client Trade ID specified is invalid",
        "CLIENT_TRADE_ID_ALREADY_EXISTS":
            "The client Trade ID specifed is already assigned to another "
            "open Trade",
        "CLIENT_TRADE_TAG_INVALID":
            "The client Trade tag specified is invalid",
        "CLIENT_TRADE_COMMENT_INVALID": "The client Trade comment is invalid",
        "ORDER_FILL_POSITION_ACTION_MISSING":
            "The OrderFillPositionAction field has not been specified",
        "ORDER_FILL_POSITION_ACTION_INVALID":
            "The OrderFillPositionAction specified is invalid",
        "TRIGGER_CONDITION_MISSING":
            "The TriggerCondition field has not been specified",
        "TRIGGER_CONDITION_INVALID":
            "The TriggerCondition specified is invalid",
        "ORDER_PARTIAL_FILL_OPTION_MISSING":
            "The OrderFillPositionAction field has not been specified",
        "ORDER_PARTIAL_FILL_OPTION_INVALID":
            "The OrderFillPositionAction specified is invalid.",
        "INVALID_REISSUE_IMMEDIATE_PARTIAL_FILL":
            "When attempting to reissue an order (currently only a "
            "MarketIfTouched) that was immediately partially filled, it is "
            "not possible to create a correct pending Order.",
        "TAKE_PROFIT_ORDER_ALREADY_EXISTS":
            "A Take Profit Order for the specified Trade already exists",
        "TAKE_PROFIT_ON_FILL_PRICE_MISSING":
            "The Take Profit on fill specified does not provide a price",
        "TAKE_PROFIT_ON_FILL_PRICE_INVALID":
            "The Take Profit on fill specified contains an invalid price",
        "TAKE_PROFIT_ON_FILL_PRICE_PRECISION_EXCEEDED":
            "The Take Profit on fill specified contains a price with more "
            "precision than is allowed by the Order’s instrument",
        "TAKE_PROFIT_ON_FILL_TIME_IN_FORCE_MISSING":
            "The Take Profit on fill specified does not provide a TimeInForce",
        "TAKE_PROFIT_ON_FILL_TIME_IN_FORCE_INVALID":
            "The Take Profit on fill specifies an invalid TimeInForce",
        "TAKE_PROFIT_ON_FILL_GTD_TIMESTAMP_MISSING":
            "The Take Profit on fill specifies a GTD TimeInForce but does "
            "not provide a GTD timestamp",
        "TAKE_PROFIT_ON_FILL_GTD_TIMESTAMP_IN_PAST":
            "The Take Profit on fill specifies a GTD timestamp that is in "
            "the past",
        "TAKE_PROFIT_ON_FILL_CLIENT_ORDER_ID_INVALID":
            "The Take Profit on fill client Order ID specified is invalid",
        "TAKE_PROFIT_ON_FILL_CLIENT_ORDER_TAG_INVALID":
            "The Take Profit on fill client Order tag specified is invalid",
        "TAKE_PROFIT_ON_FILL_CLIENT_ORDER_COMMENT_INVALID":
            "The Take Profit on fill client Order comment specified is "
            "invalid",
        "TAKE_PROFIT_ON_FILL_TRIGGER_CONDITION_MISSING":
            "The Take Profit on fill specified does not provide a "
            "TriggerCondition",
        "TAKE_PROFIT_ON_FILL_TRIGGER_CONDITION_INVALID":
            "The Take Profit on fill specifies an invalid TriggerCondition",
        "STOP_LOSS_ORDER_ALREADY_EXISTS":
            "A Stop Loss Order for the specified Trade already exists",
        "STOP_LOSS_ON_FILL_PRICE_MISSING":
            "The Stop Loss on fill specified does not provide a price",
        "STOP_LOSS_ON_FILL_PRICE_INVALID":
            "The Stop Loss on fill specifies an invalid price",
        "STOP_LOSS_ON_FILL_PRICE_PRECISION_EXCEEDED":
            "The Stop Loss on fill specifies a price with more precision "
            "than is allowed by the Order’s instrument",
        "STOP_LOSS_ON_FILL_TIME_IN_FORCE_MISSING":
            "The Stop Loss on fill specified does not provide a TimeInForce",
        "STOP_LOSS_ON_FILL_TIME_IN_FORCE_INVALID":
            "The Stop Loss on fill specifies an invalid TimeInForce",
        "STOP_LOSS_ON_FILL_GTD_TIMESTAMP_MISSING":
            "The Stop Loss on fill specifies a GTD TimeInForce but does "
            "not provide a GTD timestamp",
        "STOP_LOSS_ON_FILL_GTD_TIMESTAMP_IN_PAST":
            "The Stop Loss on fill specifies a GTD timestamp that is in "
            "the past",
        "STOP_LOSS_ON_FILL_CLIENT_ORDER_ID_INVALID":
            "The Stop Loss on fill client Order ID specified is invalid",
        "STOP_LOSS_ON_FILL_CLIENT_ORDER_TAG_INVALID":
            "The Stop Loss on fill client Order tag specified is invalid",
        "STOP_LOSS_ON_FILL_CLIENT_ORDER_COMMENT_INVALID":
            "The Stop Loss on fill client Order comment specified is invalid",
        "STOP_LOSS_ON_FILL_TRIGGER_CONDITION_MISSING":
            "The Stop Loss on fill specified does not provide a "
            "TriggerCondition",
        "STOP_LOSS_ON_FILL_TRIGGER_CONDITION_INVALID":
            "The Stop Loss on fill specifies an invalid TriggerCondition",
        "TRAILING_STOP_LOSS_ORDER_ALREADY_EXISTS":
            "A Trailing Stop Loss Order for the specified Trade already "
            "exists",
        "TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_MISSING":
            "The Trailing Stop Loss on fill specified does not provide a "
            "distance",
        "TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_INVALID":
            "The Trailing Stop Loss on fill distance is invalid",
        "TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_PRECISION_EXCEEDED":
            "The Trailing Stop Loss on fill distance contains more precision "
            "than is allowed by the instrument",
        "TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_MAXIMUM_EXCEEDED":
            "The Trailing Stop Loss on fill price distance exceeds the "
            "maximum allowed amount",
        "TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_MINIMUM_NOT_MET":
            "The Trailing Stop Loss on fill price distance does not meet "
            "the minimum allowed amount",
        "TRAILING_STOP_LOSS_ON_FILL_TIME_IN_FORCE_MISSING":
            "The Trailing Stop Loss on fill specified does not provide a "
            "TimeInForce",
        "TRAILING_STOP_LOSS_ON_FILL_TIME_IN_FORCE_INVALID":
            "The Trailing Stop Loss on fill specifies an invalid TimeInForce",
        "TRAILING_STOP_LOSS_ON_FILL_GTD_TIMESTAMP_MISSING":
            "The Trailing Stop Loss on fill TimeInForce is specified as GTD "
            "but no GTD timestamp is provided",
        "TRAILING_STOP_LOSS_ON_FILL_GTD_TIMESTAMP_IN_PAST":
            "The Trailing Stop Loss on fill GTD timestamp is in the past",
        "TRAILING_STOP_LOSS_ON_FILL_CLIENT_ORDER_ID_INVALID":
            "The Trailing Stop Loss on fill client Order ID specified is "
            "invalid",
        "TRAILING_STOP_LOSS_ON_FILL_CLIENT_ORDER_TAG_INVALID":
            "The Trailing Stop Loss on fill client Order tag specified is "
            "invalid",
        "TRAILING_STOP_LOSS_ON_FILL_CLIENT_ORDER_COMMENT_INVALID":
            "The Trailing Stop Loss on fill client Order comment specified "
            "is invalid",
        "TRAILING_STOP_LOSS_ORDERS_NOT_SUPPORTED":
            "A client attempted to create either a Trailing Stop Loss order "
            "or an order with a Trailing Stop Loss On Fill specified, which "
            "may not yet be supported.",
        "TRAILING_STOP_LOSS_ON_FILL_TRIGGER_CONDITION_MISSING":
            "The Trailing Stop Loss on fill specified does not provide a "
            "TriggerCondition",
        "TRAILING_STOP_LOSS_ON_FILL_TRIGGER_CONDITION_INVALID":
            "The Tailing Stop Loss on fill specifies an invalid "
            "TriggerCondition",
        "CLOSE_TRADE_TYPE_MISSING": "The request to close a Trade does not "
                                    "specify a full or partial close",
        "CLOSE_TRADE_PARTIAL_UNITS_MISSING":
            "The request to close a Trade partially did not specify the "
            "number of units to close",
        "CLOSE_TRADE_UNITS_EXCEED_TRADE_SIZE":
            "The request to partially close a Trade specifies a number of "
            "units that exceeds the current size of the given Trade",
        "CLOSEOUT_POSITION_DOESNT_EXIST":
            "The Position requested to be closed out does not exist",
        "CLOSEOUT_POSITION_INCOMPLETE_SPECIFICATION":
            "The request to closeout a Position was specified incompletely",
        "CLOSEOUT_POSITION_UNITS_EXCEED_POSITION_SIZE":
            "A partial Position closeout request specifies a number of units "
            "that exceeds the current Position",
        "CLOSEOUT_POSITION_REJECT":
            "The request to closeout a Position could not be fully satisfied",
        "CLOSEOUT_POSITION_PARTIAL_UNITS_MISSING":
            "The request to partially closeout a Position did not specify "
            "the number of units to close.",
        "MARKUP_GROUP_ID_INVALID": "The markup group ID provided is invalid",
        "POSITION_AGGREGATION_MODE_INVALID":
            "The PositionAggregationMode provided is not supported/valid.",
        "ADMIN_CONFIGURE_DATA_MISSING": "No configuration parameters provided",
        "MARGIN_RATE_INVALID": "The margin rate provided is invalid",
        "MARGIN_RATE_WOULD_TRIGGER_CLOSEOUT": "The margin rate provided "
                                              "would cause an immediate "
                                              "margin closeout",
        "ALIAS_INVALID": "The account alias string provided is invalid",
        "CLIENT_CONFIGURE_DATA_MISSING":
            "No configuration parameters provided",
        "MARGIN_RATE_WOULD_TRIGGER_MARGIN_CALL":
            "The margin rate provided would cause the Account to enter "
            "a margin call state.",
        "AMOUNT_INVALID": "Funding is not possible because the requested "
                          "transfer amount is invalid",
        "INSUFFICIENT_FUNDS": "The Account does not have sufficient "
                              "balance to complete the funding request",
        "AMOUNT_MISSING": "Funding amount has not been specified",
        "FUNDING_REASON_MISSING": "Funding reason has not been specified",
        "CLIENT_EXTENSIONS_DATA_MISSING":
            "Neither Order nor Trade on Fill client extensions were "
            "provided for modification",
        "REPLACING_ORDER_INVALID":
            "The Order to be replaced has a different type than the "
            "replacing Order.",
        "REPLACING_TRADE_ID_INVALID":
            "The replacing Order refers to a different Trade than the "
            "Order that is being replaced.",
     }
}
