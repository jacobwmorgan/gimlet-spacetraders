"""Player Module

Returns:
    json: response
"""

import json
import re
import requests
from rich.console import Console
from rich.progress import track

class Player:
    """
        Player Class
    """

    def __init__(self):
        self.console = Console()
        self.token = self.get_api_key()
        data = self.get_player_info()['data']
        if 'error' in data:
            if data['error']['code'] == 401:
                self.reregister()
            else:
                self.console.print(f":x: {data['error']['message']}")
        self.username = data['symbol']
        self.headquaters = data['headquarters']
        self.credits = data['credits']
        self.faction = data['startingFaction']
        self.ship_count = data['shipCount']

    def get_api_key(self):
        """ Gets api key from constants

        Returns:
            string: api key
        """

        with open('constants.json', encoding='utf-8') as f:
            data = json.load(f)
        if data['API_KEY'] == "":
            self.reregister()
        return data['API_KEY']

    def reregister(self):
        """
            Reregister player

            Returns:
                json: response
        """
        self.console.print(":recycle: re-registering ...")
        username = input("Username:")
        while track(True, description="Registering"):         
            response = requests.post(
                'https://api.spacetraders.io/v2/register',
                data = {
                    "symbol" : username,
                    "faction" : "COSMIC"
                },
                timeout=5
            ).json()

            if 'error' in response:
                self.console.print(f":x: {response['error']['message']}")
                if response['error']['code'] == 4111:
                    # not the most rebust way to do this but it works
                    if len(username) > 14:
                        username = username[:14]

                    username_numbers = re.match(r"([a-z]+)([0-9]+)", username, re.I)
                    if username_numbers:
                        items = username_numbers.groups()

                        new_number = int(items[1]) + 1

                        new_username = items[0] + str(new_number)

                        username = new_username

                    else:
                        if len(username) < 14:
                            username = username + "1"
                        else:
                            username = chr(ord(username[0]) + 1) + username[1:]
                    self.console.print(":recycle: New username: ", username)
                    continue

            else:
                self.console.print(":white_check_mark: Got new token")
                break

        with open('constants.json', 'w', encoding='utf-8') as f:
            json.dump({"API_KEY": response['data']['token']}, f, indent=4)

    def authentication_header(self):
        """ 
            Authorize player

            Returns:
                dict: authentication header
        """
        headers = {
            'Authorization': f'Bearer {self.token.strip()}'
        }
        return headers

    def get_player_info(self):
        """ Authorize player
        """

        return requests.get(
                            'https://api.spacetraders.io/v2/my/agent', 
                            headers=self.authentication_header(),
                            timeout=5
        ).json()


    def display_player_info(self):
        """ Player info

        Returns:
            json: response
        """
        # I cant do this on one line , I know it looks mega ugly
        self.console.print(f":trident: Username: {self.username}")
        self.console.print(f":stadium: Headquaters: {self.headquaters}")
        self.console.print(f":shamrock: Credits: {self.credits}")
        self.console.print(f":shield: Faction: {self.faction}")
        self.console.print(f":rocket: Ship Count: {self.ship_count}")
