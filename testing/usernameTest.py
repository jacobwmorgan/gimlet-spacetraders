"""
This is a test file for the username generator
"""

import re
USERNAME = ""


if len(USERNAME) > 14:
    USERNAME = USERNAME[:14]


USERNAMENUMBERS = re.match(r"([a-z]+)([0-9]+)", USERNAME, re.I)

if USERNAMENUMBERS:
    items = USERNAMENUMBERS.groups()

    new_number = int(items[1]) + 1

    new_username = items[0] + str(new_number)

    USERNAME = new_username

else:
    USERNAME = chr(ord(USERNAME[0]) + 1) + USERNAME[1:]

print(USERNAME)
