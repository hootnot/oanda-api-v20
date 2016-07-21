import unittest
from . import unittestsetup
from .unittestsetup import environment as environment
try:
    from nose_parameterized import parameterized
except:
    print("*** Please install 'nose_parameterized' to run these tests ***")
    exit(0)

import oandapyV20 as oandapy
import oandapyV20.endpoints.positions as positions

from . import helper

access_token = None
accountID = None
account_cur = None
api = None
verbose = False


class TestPositions(unittest.TestCase):

    def setUp(self):
        global access_token
        global accountID
        global account_cur
        global api
        global verbose
        # self.maxDiff = None
        try:
            accountID, account_cur, access_token = unittestsetup.auth()
        except Exception as e:
            print("{}".format(e))
            exit(0)

        api = oandapy.API(environment=environment, access_token=access_token,
                          headers={"Content-Type": "application/json"})

    @parameterized.expand([
                           ("EUR_USD", "long", [100, 1000]),
                           ("DE30_EUR", "short", [10, 10]),
                          ])
    def test__openpositions(self, instrument, side, units):
        """get open positions."""
        helper.close_pos(api, accountID, instrument, side)  # if any ... close
        # create a position by creating orders equivalent to units
        verify = 0
        for U in units:
            rv = helper.create_pos(api, accountID, instrument, side, U)
            verify += int(rv["orderCreateTransaction"]["units"])

        # fetch pos
        r = positions.OpenPositions(accountID)
        rv = api.request(r)

        posUnits = None
        # lookup the instrument in the positions array
        for P in rv["positions"]:
            if P["instrument"] == instrument:
                posUnits = int(P[side]["units"])

        self.assertEqual(verify, posUnits)

    @parameterized.expand([
                           ("EUR_USD", "long", [100, 1000]),
                           ("DE30_EUR", "short", [10, 10]),
                          ])
    def test__positions(self, instrument, side, units):
        # GET	/v3/accounts/{accountID}/positions
        r = positions.OpenPositions(accountID)
        rv = api.request(r)
        # make sure we have no open positions left for those instruments
        for P in rv["positions"]:
            instr = P["instrument"]
            helper.close_pos(api, accountID, instr, "long")
            helper.close_pos(api, accountID, instr, "short")

        # all positions are now reset to 0 units

        # now create new pos.
        # the units should be equal to those in Positions
        verify = 0
        for U in units:
            rv = helper.create_pos(api, accountID, instrument, side, U)
            verify += int(rv["orderCreateTransaction"]["units"])

        r = positions.Positions(accountID, op=positions.POSITION_LIST)
        rv = api.request(r)
        # lookup the instrument in the positions array
        posUnits = None
        for P in rv["positions"]:
            if P["instrument"] == instrument:
                posUnits = int(P[side]["units"])
        self.assertEqual(verify, posUnits)


if __name__ == "__main__":

    unittest.main()
