"""
    Model for the Waypoint class's
"""
import requests
import sys
from models.location.spaceobject import SpaceObject
from models.location.system import System
from api import authentication


class Waypoint(SpaceObject):
    """
        Space Waypoint
        https://spacetraders.stoplight.io/docs/spacetraders/86a14c74e1c69-system
        Args:
            SpaceObject (System): _description_
    """
    def __init__(self, symbol):
        self.symbol = symbol
        stripped_symbol = self.symbol.split('-')
        self.system = System(f"{stripped_symbol[0]}-{stripped_symbol[1]}")
        self.waypoint_symbol = stripped_symbol[-1]
        data = self.get_waypoint_info()['data']
        super().__init__(symbol,data['type'],data['x'],data['y'])
        if data['orbitals'] is not None:
            self.orbitals = [Orbital(i['symbol'],self) for i in data['orbitals']]

    def get_waypoint_info(self):
        """Get system information

        Returns:
            json: system information
        """
        return requests.get(
            f'https://api.spacetraders.io/v2/systems/{self.system.symbol}/waypoints/{self.symbol}', 
            headers=authentication.header(),
            timeout=5
        ).json()


class Orbital(Waypoint):
    """
        Space Orbital, Orbits a waypoint
    """

    def __init__(self,symbol, orbits_from):
        super().__init__(symbol)
        self.orbits = orbits_from