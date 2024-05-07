"""
    Space traders API test
"""

from datetime import datetime
import requests
from rich.console import Console

from models.player import Player



console = Console()
player = Player()
STYLE = 'white on blue'


"""
    How do i wanna approach the models?
    Do i want a main like "Object file" which everyother thing will inherit from
    E.g. 
        SpaceObject (#What is another name for a location ? This sucks )
            > Sector
                > Contains Systems which contains waypoints
            > System
                > A bunch of waypoints in a system
                
            > Waypoints etc etc (makes no sense for the waypoints to inherit from the system imo)
                > Waypoints have types which inherit from the waypoint ?
            
"""


if __name__ == '__main__':
    test = requests.get('https://api.spacetraders.io/v2/',timeout=5).json()
    next_server_reset = datetime.strptime(test['serverResets']['next'],"%Y-%m-%dT%H:%M:%S.%fZ")
    console.print("Welcome to Space Traders API test",style=STYLE, justify="center")
    console.print(f":zap: Next Server Reset -> {next_server_reset}")
    player.display_player_info()
    console.print(player.headquaters)
    console.print(player.headquaters.orbitals)
    console.print(player.get_player_contracts())
    player.build_player_contracts()