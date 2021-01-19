# Graph generator class.
# This does not track distance between points, as of yet at least.
# This is intended for use while exploring graph algorithms (undirected).

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class Graph(object):
    """
    Class: Graph(object):
    ----------------------------------------------------------------------------
    This is a class that takes the number of nodes and a list of tuples or
    a list of lists of vertices and generates a numpy array representing the
    graph.
    The graph can then be plotted, represented by an adjacency matrix,
    list or dictionary.
    ----------------------------------------------------------------------------
    @param:
        nodes (int)
        vertices (list of tuples) OR (list of lists)
    @methods:
        get_adj_matrix()
        get_adj_list()
        get_adj_dict()
        show_graph()
    ============================================================================
    """
    def __init__(self, nodes, vertices):
        self.n = nodes
        self.v = vertices

    def create_adj_matrix(self):
        m = np.zeros((self.n, self.n), dtype=np.int32)
        for vertex in self.v:
            m[vertex[0]][vertex[1]] = 1
            m[vertex[1]][vertex[0]] = 1
        self.m = m

    def create_adj_list(self):
        ls = [list() for i in range(self.n)]
        self.ls = self._helper(ls)

    def create_adj_dict(self):
        d = {i : list() for i in range(self.n)}
        self.d = self._helper(d)

    def _helper(self, obj):
        for vertex in self.v:
            obj[vertex[0]].append(vertex[1])
            obj[vertex[1]].append(vertex[0])
        return obj

    def get_adj_matrix(self):
        return self.m

    def get_adj_list(self):
        return self.ls

    def get_adj_dict(self):
        return self.d

    def show_graph(self):
        """
        Utilizes networkx and matplotlib.pyplot to plot a graph with
        n nodes and m edges.
        """
        g = nx.Graph()
        g.add_nodes_from([i for i in range(self.n)])
        g.add_edges_from(self.v)
        nx.draw(g)
        plt.show()
