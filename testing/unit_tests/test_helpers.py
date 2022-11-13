import pytest, json
from src.utils.helpers import call_api

def test_call_api():
    start = 'Boston%2CMA'
    end = 'Lexington%2CMA'
    midpoints = ['Charleston%2CMA', 'Concord%2CMA', 'Sudbury%2CMA', 'Westwood%2CMA', 'Arlington%2CMA', 'Needham%2CMA']

    # Make API call to Google Distance Matrix
    data = call_api(start, end, midpoints)

    # Load sample data
    with open('testing/integration_tests/test_response.json') as f:
        sample_data = json.load(f)

    # Traffic data will vary
    assert (data['destination_addresses'] == sample_data['destination_addresses']) & (data['origin_addresses'] == sample_data['origin_addresses']) 