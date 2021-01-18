import Graph as gr

if __name__ == "__main__":
    N = 5
    vertices = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
    G = gr.Graph(N, vertices)
    G.create_adj_matrix()
    G.create_adj_list()
    G.create_adj_dict()

    adj_matrix = G.get_adj_matrix()
    adj_list = G.get_adj_list()
    adj_dict = G.get_adj_dict()

    line_length = 70
    print("\nAdjacency Matrix:")
    [print("-", end="") for i in range(line_length)]
    print("\n{0}".format(adj_matrix))
    [print("=", end="") for i in range(line_length)]
    print("\n")

    print("\nAdjacency List:")
    [print("-", end="") for i in range(line_length)]
    print("\n{0}".format(adj_list))
    [print("=", end="") for i in range(line_length)]
    print("\n")

    print("\nAdjacency Dictionary:")
    [print("-", end="") for i in range(line_length)]
    print("\n{0}".format(adj_dict))
    [print("=", end="") for i in range(line_length)]
    print("\n")

    G.show_graph()

# Output:
"""

Adjacency Matrix:
----------------------------------------------------------------------
[[0 1 0 0 1]
 [1 0 1 1 1]
 [0 1 0 1 0]
 [0 1 1 0 1]
 [1 1 0 1 0]]
======================================================================


Adjacency List:
----------------------------------------------------------------------
[[1, 4], [0, 2, 3, 4], [1, 3], [1, 2, 4], [0, 1, 3]]
======================================================================


Adjacency Dictionary:
----------------------------------------------------------------------
{0: [1, 4], 1: [0, 2, 3, 4], 2: [1, 3], 3: [1, 2, 4], 4: [0, 1, 3]}
======================================================================

"""
