from graph_utils import Graph as gr
import DFS as dfs_search
import BFS as bfs_search

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

def print_res(headers, args, line_length=70):
    for i in range(len(headers)):
        print("{0}:".format(headers[i]))
        [print("-", end="") for i in range(line_length)]
        print("\n{0}".format(args[i]))
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

"""
