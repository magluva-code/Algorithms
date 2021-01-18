from graph_utils import Graph as gr
import DFS as search

if __name__ == "__main__":

    N = 5
    vertices = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
    G = gr.Graph(N, vertices)
    G.create_adj_dict()

    start = 1
    adj_dict = G.get_adj_dict()
    dfs = search.DFS(adj_dict)
    path = dfs(start)

    line_length = 70
    print("\nAdjacency Dictionary:")
    [print("-", end="") for i in range(line_length)]
    print("\n{0}".format(adj_dict))
    [print("=", end="") for i in range(line_length)]
    print("\n")

    print("\Depth First Search:")
    [print("-", end="") for i in range(line_length)]
    print("\n{0}".format(path))
    [print("=", end="") for i in range(line_length)]
    print("\n")

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

"""
