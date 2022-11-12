import pytest, json
from src.utils.graph import Graph
import networkx as nx

# Load sample response data
# This file path might break with automated testing
with open('testing/integration_tests/test_response.json') as f:
    sample_data = json.load(f)

# Create a truth graph to compare
known_graph = nx.DiGraph()
start = 'Boston%2CMA'
end = 'Lexington%2CMA'
se_node = 'Boston%2CMA&Lexington%2CMA'
midpoints = ['Charleston%2CMA', 'Concord%2CMA', 'Sudbury%2CMA', 'Westwood%2CMA', 'Arlington%2CMA', 'Needham%2CMA']
origins = [start] + midpoints
dests = [end] + midpoints

def test_graph():
    # Create test graph
    graph = Graph(start=start, end=end)

    # Compare
    assert graph._se_node == se_node

def test_add_nodes():
    # Create test graph
    graph = Graph(start=start, end=end)
    graph.add_nodes(midpoints=midpoints)

    # Add nodes to truth graph
    known_graph.add_node(se_node)
    known_graph.add_nodes_from(midpoints)

    # Compare
    DiGM = nx.isomorphism.DiGraphMatcher(graph.graph, known_graph)
    assert DiGM.is_isomorphic()

def test_add_edges():
    # Create test graph
    graph = Graph(start=start, end=end)
    graph.add_nodes(midpoints=midpoints)
    graph.add_edges(response=sample_data, midpoints=midpoints)

    # Add edges to truth graph
    for i, row in enumerate(sample_data['rows']):
        for j, element in enumerate(row['elements']):
            if i == j:
                continue
            if element["duration"]["value"] > 0:
                orig = se_node if i == 0 else origins[i]
                dest = se_node if j == 0 else dests[j]
                known_graph.add_weighted_edges_from([(orig, dest, element["duration"]["value"])])

    # Compare graph to truth graph
    DiGM = nx.isomorphism.DiGraphMatcher(graph.graph, known_graph)
    assert DiGM.is_isomorphic()

def test_get_travel_time():
    # Create test graph
    graph = Graph(start=start, end=end)
    graph.add_nodes(midpoints=midpoints)
    graph.add_edges(response=sample_data, midpoints=midpoints)

    # Calculate travel time
    (h, m) = graph.get_travel_time()

    # This should always work because the response is static
    assert (h == 2) & (m == 11)