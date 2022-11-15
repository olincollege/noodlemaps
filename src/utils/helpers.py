'''
Miscellaneous helper functions.
'''

import os, requests, json
from dotenv import load_dotenv

def call_api(start, end, midpoints):
    '''
    Calls the Google Maps Distance Matrix API

    Args:
        start: (str) Origin in URL format
        end: (str) Destination in URL format
        midpoints: [str] List of midpoints in URL format

    Returns:
        (JSON) Response in JSON format
    '''
    load_dotenv()
    API_KEY = os.getenv('API_KEY')

    # Join midpoints into string
    midpoint_str = '%7C'.join(midpoints)

    origins = f'origins={start}%7C{midpoint_str}'
    dests = f'destinations={end}%7C{midpoint_str}'
    departure_time = 'departure_time=now'
    key = f'key={API_KEY}'

    # Create URL
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?{'&'.join([origins, dests, departure_time, key])}"

    # Make HTTP request
    response = requests.request("GET", url, headers={}, data={})

    return response.json()
