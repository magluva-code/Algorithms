# Just an example of a main running the algorithms.

import numpy as np
from graph_utils import Graph as gr
from graph_utils import GraphObj as go
import DFS as dfs_search
import BFS as bfs_search
import Dijkstra as fsp_search

def run_DFS():
    N = 5
    vertices = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
    G = gr.Graph(N, vertices)
    G.create_adj_dict()
    start = 1
    adj_dict = G.get_adj_dict()
    dfs = dfs_search.DFS(adj_dict)
    path = dfs(start)
    return adj_dict, path

def run_BFS():
    N = 5
    vertices = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
    G = gr.Graph(N, vertices)
    G.create_adj_dict()
    start = 1
    adj_dict = G.get_adj_dict()
    bfs = bfs_search.BFS(adj_dict)
    path = bfs(start)
    return adj_dict, path

def run_Dijkstra():
    N = 6
    graph = go.GraphObj(N)
    # For loop goes here!
    # Possible to shorten code by over 10 lines...
    graph.add_node(go.Node(0), go.Node(1, dist=5))
    graph.add_node(go.Node(0), go.Node(2, dist=1))
    graph.add_node(go.Node(0), go.Node(3, dist=4))
    graph.add_node(go.Node(1), go.Node(0, dist=5))
    graph.add_node(go.Node(1), go.Node(2, dist=3))
    graph.add_node(go.Node(1), go.Node(4, dist=8))
    graph.add_node(go.Node(2), go.Node(0, dist=1))
    graph.add_node(go.Node(2), go.Node(1, dist=3))
    graph.add_node(go.Node(2), go.Node(3, dist=2))
    graph.add_node(go.Node(2), go.Node(4, dist=1))
    graph.add_node(go.Node(3), go.Node(0, dist=4))
    graph.add_node(go.Node(3), go.Node(2, dist=2))
    graph.add_node(go.Node(3), go.Node(4, dist=2))
    graph.add_node(go.Node(3), go.Node(5, dist=1))
    graph.add_node(go.Node(4), go.Node(1, dist=8))
    graph.add_node(go.Node(4), go.Node(2, dist=1))
    graph.add_node(go.Node(4), go.Node(3, dist=2))
    graph.add_node(go.Node(4), go.Node(5, dist=3))
    graph.add_node(go.Node(5), go.Node(3, dist=1))
    graph.add_node(go.Node(5), go.Node(4, dist=3))
    graph.create("dict", dt=np.object)
    start = 0
    dijkstra = fsp_search.Dijkstra(graph.get())
    path = dijkstra(start)
    return start, path

def print_res(headers, args, line_length=70):
    for i in range(len(headers)):
        print("{0}:".format(headers[i]))
        [print("-", end="") for i in range(line_length)]
        [print("\n{0}".format(args[i])) for i in range(len(args))]
        [print("=", end="") for i in range(line_length)]
        print("\n")

if __name__ == "__main__":

    ############################################################################
    # Depth First Search
    ############################################################################

    adj_dict, path = run_DFS()
    print_res(["Adjacency Dictionary", "Depth Search First"],
              [adj_dict, path])

    ############################################################################
    # Breadth First Search
    ############################################################################

    path = run_BFS()[1]
    print_res(["Breadth Search First"],
              [path])

    ############################################################################
    # Dijkstra Shortest Path
    ############################################################################

    start, path = run_Dijkstra()
    ls = ["src: {0} ---> dest: {1} = {2}".format(start, i, path[i]) for i in range(len(path))]
    print_res(["Dijkstra Shortest Path"],
              ls)
    #[print("src: {0} ---> dest: {1} = {2}".format(src, i, dist[i])) for i in range(len(graph_test))]

# Output:
"""
Adjacency Dictionary:
----------------------------------------------------------------------
{0: [1, 4], 1: [0, 2, 3, 4], 2: [1, 3], 3: [1, 2, 4], 4: [0, 1, 3]}
======================================================================

\Depth First Search:
----------------------------------------------------------------------
[1, 0, 4, 3, 2]
======================================================================

Breadth Search First:
----------------------------------------------------------------------
[1, 0, 2, 3, 4]
======================================================================

Dijkstra Shortest Path:
----------------------------------------------------------------------
src: 0 ---> dest: 0 = 0

src: 0 ---> dest: 1 = 4

src: 0 ---> dest: 2 = 1

src: 0 ---> dest: 3 = 3

src: 0 ---> dest: 4 = 2

src: 0 ---> dest: 5 = 4
======================================================================

"""
