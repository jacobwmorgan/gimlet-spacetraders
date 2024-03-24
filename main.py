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


if __name__ == '__main__':
    test = requests.get('https://api.spacetraders.io/v2/',timeout=5).json()
    next_server_reset = datetime.strptime(test['serverResets']['next'],"%Y-%m-%dT%H:%M:%S.%fZ")
    console.print("Welcome to Space Traders API test",style=STYLE, justify="center")
    console.print(f":zap: Next Server Reset -> {next_server_reset}")
    player.display_player_info()
    