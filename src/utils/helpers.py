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

    # Create URL
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={start}%7C{midpoint_str}&destinations={end}%7C{midpoint_str}&departure_time=now&key={API_KEY}"

    # Make HTTP request
    response = requests.request("GET", url, headers={}, data={})

    print(response.text)
    print(API_KEY)

    return response.json()
