"""
    Model for the System class
"""
from spaceobject import SpaceObject

class System(SpaceObject):
    def __init__(self, symbol):
        self.symbol = symbol
    
    def get_system_info(self):
        
        