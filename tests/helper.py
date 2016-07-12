"""some functions used among tests."""
import oandapyV20.endpoints.positions as positions
import oandapyV20.endpoints.orders as orders
from oandapyV20.exceptions import V20Error


def close_pos(api, account_id, instrument, side, verbose=False):
    """close_pos: close a position by instrument."""
    try:
        r = positions.Positions(
                       account_id,
                       instrument=instrument,
                       subject="close",
                       configuration={"{}Units".format(side): "ALL"})
        api.request(r)
    except V20Error as e:
        # if there is no position an error response is returned
        if verbose:
            print(e)


def create_pos(api, account_id, instrument, side, units):
    """create_pos: create a position for instrument by a MARKET order."""
    units = units if side == "long" else -units
    orderSpec = {
      "order": {
        "units": str(units),
        "instrument": instrument,
        "timeInForce": "FOK",
        "type": "MARKET",
        "positionFill": "DEFAULT"
      }
    }
    r = orders.Orders(account_id, configuration=orderSpec)
    return api.request(r)
