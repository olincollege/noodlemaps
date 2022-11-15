"""
Module to build graphs
"""
# import requests, json
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    """
    Class to build and use graphs to solve the TSP

    Attributes:
        graph: A networkx digraph where nodes are locations and edges are 
            travel times. Note that the start and end locations share a
            single node.
    """

    def __init__(self, start: str, end: str):
        """
        Initializes a digraph and its start/end.

        Args:
            start: String representing start location.
            end: String representing destination.
        """
        self.graph = nx.DiGraph()
        self._start = start
        self._end = end
        self._se_node = f'{start}&{end}'

    def add_nodes(self, midpoints):
        """
        Adds all non-origin and non-destination nodes.

        Arg:
            midpoints: [str] of locations in URL format
        """
        self.graph.add_node(self._se_node)
        self.graph.add_nodes_from(midpoints)

    def add_edges(self, response, midpoints):
        """
        Add weights from edges

        Args:
            response: [JSON] The HTTP response from GETting the API, in JSON format
            midpoints: [str] of locations in URL format
        """
        origins = [self._start] + midpoints
        dests = [self._end] + midpoints
        for i, row in enumerate(response['rows']):
            for j, element in enumerate(row['elements']):
                # Don't connect a node to itself
                if i == j:
                    continue
                if element["duration"]["value"] > 0:
                    orig = self._se_node if i == 0 else origins[i]
                    dest = self._se_node if j == 0 else dests[j]
                    self.graph.add_weighted_edges_from([(orig, dest, element["duration"]["value"])])

    def draw(self):
        """
        Draws graph using matplotlib.
        """
        nx.draw_circular(self.graph,
                         node_color='C0',
                         node_size=2000,
                         with_labels=True)

    def get_travel_time(self):
        """
        Runs a greedy TSP algorithm and times the outcome.

        Returns:
            (h, m): (int, int) representing travel time in (hours, minutes)
        """
        cycle = nx.approximation.greedy_tsp(self.graph, source=self._se_node)
        time = 0
        for i, n in enumerate(cycle):
            if i == 0:
                continue
            time += self.graph[cycle[i - 1]][n]['weight']
        h, m = divmod(time // 60, 60)
        return (h, m)