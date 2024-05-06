"""
    Model for the System class
"""
import requests
from models.location.spaceobject import SpaceObject
from api import authentication
class System(SpaceObject):
    """
        Space system
        
        https://spacetraders.stoplight.io/docs/spacetraders/86a14c74e1c69-system
        Args:
            SpaceObject (System): _description_
    """
    def __init__(self, symbol):
        self.symbol = symbol
        data = self.get_system_info()
        self.sector = data['sectorSymbol']
        self.type = data['type']
        self.x = data['x']
        self.y = data['y']
        #self.waypoints = self.build_waypoints(data['waypoints'])

    def get_system_info(self):
        """
            Get system information

            Returns:
                json: system information
        """
        return requests.get(
                            f'https://api.spacetraders.io/v2/systems/{self.symbol}', 
                            headers=authentication.header(),
                            timeout=5
        ).json()['data']
    
    def build_waypoints(self, waypoints):
        """
            Build All Waypoints linked to system

        """
        for waypoint in waypoints:
            print(waypoint)
        