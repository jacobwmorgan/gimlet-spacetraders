"""Player Module

Returns:
    json: response
"""

import requests
from rich.console import Console
from api import helpers
from api import authentication
from models.location.waypoint import Waypoint
class Player:
    """
        Player Class
    """

    def __init__(self):
        self.console = Console()
        self.token = helpers.get_api_key()
        data = self.get_player_info()['data']
        if 'error' in data:
            if data['error']['code'] == 401:
                helpers.register()
            else:
                self.console.print(f":x: {data['error']['message']}")
        self.username = data['symbol']
        self.headquaters = Waypoint(data['headquarters'])
        self.credits = data['credits']
        self.faction = data['startingFaction']
        self.ship_count = data['shipCount']
        self.contracts = {}

    def get_player_info(self):
        """ Get Player Info

            Returns:
                json: player info
        """

        return requests.get(
                            'https://api.spacetraders.io/v2/my/agent', 
                            headers=authentication.header(),
                            timeout=5
        ).json()

    def display_player_info(self):
        """ Printing Player info
        """
        # I cant do this on one line , I know it looks mega ugly
        self.console.print(f":trident: Username: {self.username}")
        self.console.print(f":stadium: Headquaters: {self.headquaters.symbol}")
        self.console.print(f":shamrock: Credits: {self.credits}")
        self.console.print(f":shield: Faction: {self.faction}")
        self.console.print(f":rocket: Ship Count: {self.ship_count}")

    def get_player_contracts(self):
        """ Get Player Contracts

            Returns:
                json: all players contracts
        """
        return requests.get(
                            'https://api.spacetraders.io/v2/my/contracts', 
                            headers=authentication.header(),
                            timeout=5
        ).json()

    def build_player_contracts(self):
        """ Builds Player Contracts

            json -> Contract object
            
            
            Returns: 
                Contract objects
        """
        contracts = self.get_player_contracts()['data']

        for i in contracts:
            print(i)
        