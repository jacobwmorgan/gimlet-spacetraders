"""

    Returns:
        _type_: _description_
"""

from api import helpers

def header(): # api calls should be in a wrapper
    """ 
        Authorize player

        Returns:
            dict: authentication header
    """
    headers = {
        'Authorization': f'Bearer {helpers.get_api_key().strip()}'
    }
    return headers
