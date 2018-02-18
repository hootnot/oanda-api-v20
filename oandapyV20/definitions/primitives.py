# -*- coding: utf-8 -*-
"""Primitives definitions."""

definitions = {
    "InstrumentType": {
        "CURRENCY": "Currency",
        "CFD": "Contract For Difference",
        "METAL": "Metal"
    },
    "AcceptDatetimeFormat": {
        "UNIX": "Unix timeformat: DateTime fields will be specified "
                "or returned in the “12345678.000000123” format.",
        "RFC3339": "RFC3339 timeformat: DateTime will be specified "
                "or returned in “YYYY-MM-DDTHH:MM:SS.nnnnnnnnnZ” format."
    },
    "Direction": {
       "LONG": "A long Order is used to to buy units of an Instrument. A "
               "Trade is long when it has bought units of an Instrument.",
       "SHORT": "A short Order is used to to sell units of an Instrument. A "
                "Trade is short when it has sold units of an Instrument"
    }
}
