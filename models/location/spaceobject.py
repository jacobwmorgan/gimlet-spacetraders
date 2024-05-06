""" 
    Module for the SpaceObject class 
    Legit stole this from https://github.com/RebelKeithy/SpaceTradersPythonClient/blob/master/src/model/location.py
    because i couldnt work out how to do this
"""
from dataclasses import dataclass

@dataclass
class SpaceObject:
    """ A Base class for the rest of the location models  """ 
    symbol: str
    type: str
    x: str
    y: str
    # allows_contruction: bool
    # ships: list
    # # marketplace: list[Market]
    # structures: list

    def __init__(self, symbol: str, type: str, x: str, y: str):
        self.symbol = symbol
        self.type = type
        self.x = x
        self.y = y
