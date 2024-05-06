"""
    Model for the Waypoint class
"""
import requests
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
        data = self.get_waypoint_info()

    def get_waypoint_info(self):
        """Get system information

        Returns:
            json: system information
        """
        return requests.get(
                            'https://api.spacetraders.io/v2/my/agent', 
                            headers=authentication.header(),
                            timeout=5
        ).json()
        