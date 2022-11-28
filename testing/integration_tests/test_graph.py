import pytest, json
from src.utils.graph import Graph
import networkx as nx

'''
Tests for graph.py behavior.
'''

def test_get_travel_time_single():
    '''
    Test an API call for a graph with a single stop.
    '''
    # Load test response data
    with open('testing/integration_tests/test_get_travel_time_single.json') as f:
        test_data = json.load(f)

    # Create test graph
    start = 'Boston%2CMA'
    end = 'Lexington%2CMA'
    midpoints = ['Needham%2CMA']
    graph = Graph(start=start, end=end)
    graph.add_nodes(midpoints=midpoints)
    graph.add_edges(response=test_data, midpoints=midpoints)

    # Calculate travel time
    (cycle, h, m) = graph.get_travel_time()

    # This should always work because the response is static
    assert (h == 0) & (m == 53)

def test_get_travel_time_multiple():
    '''
    Test an API call for a graph with multiple stops.
    '''
    # Load test response data
    with open('testing/integration_tests/test_get_travel_time_multiple.json') as f:
        test_data = json.load(f)

    # Create test graph
    start = 'Boston%2CMA'
    end = 'Lexington%2CMA'
    midpoints = ['Charleston%2CMA', 'Concord%2CMA', 'Sudbury%2CMA', 'Westwood%2CMA', 'Arlington%2CMA', 'Needham%2CMA']
    graph = Graph(start=start, end=end)
    graph.add_nodes(midpoints=midpoints)
    graph.add_edges(response=test_data, midpoints=midpoints)

    # Calculate travel time
    (cycle, h, m) = graph.get_travel_time()

    # This should always work because the response is static
    assert (h == 2) & (m == 11)