"""
    Api Helper Functions
    
    register => Registers User
    
    get_api_key => returns apikey
"""
import re
import json
import sys
import os
import requests
from rich.console import Console
from rich.progress import track


DEFAULT_CONSTANTS = {
    "API_KEY": ""
}

def register():
    """
        Registers Player to spacetraders
        
        Returns:
            api key in 
    """
    console = Console()

    console.print(":recycle: registering ...")
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
            console.print(f":x: {response['error']['message']}")
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
                console.print(":recycle: New username: ", username)
                continue

        else:
            console.print(":white_check_mark: Got new token")
            break
    set_constant("API_KEY",response['data']['token'])
    console.print(":recycle: Restart program\n*Spacetraders has to do something cringe?*")
    sys.exit()

def get_api_key():
    """ 
        Gets api key from constants json

        Returns:
            string: api key
    """
    constants_data = get_constants()
    if constants_data['API_KEY'] == "":
        register()
    return constants_data['API_KEY']

# Getters and Setters for constants

def create_constants():
    """
        Generates constants file

        Args:
            constants_names (list): names of constants
    """
    os.system('echo  > constants.json')

    with open("constants.json", "w", encoding='utf-8') as f:
        json.dump(DEFAULT_CONSTANTS, f)

def set_constant(constant_name, value=None):
    """
        Creates a new constant in constant file
    """
    constants_exists = False
    while constants_exists is not True:
        try:
            with open('constants.json', 'r+', encoding='utf-8') as f:
                data = json.load(f)
                data_value = ""
                if value is not None:
                    data_value = value
                data[constant_name] = data_value
                f.seek(0)        # <--- should reset file position to the beginning.
                json.dump(data, f, indent=4)
                f.truncate()
                constants_exists = True
        except FileNotFoundError:
            create_constants()

def get_constants():
    """
        Get contents of constants.json
        If constants.json doesnt exist, create it
        returns contents in json form
    """
    constants_exists = False
    while constants_exists is not True:
        try:
            with open('constants.json', encoding='utf-8') as f:
                data = json.load(f)
                constants_exists = True
        except FileNotFoundError:
            create_constants()
    return data
