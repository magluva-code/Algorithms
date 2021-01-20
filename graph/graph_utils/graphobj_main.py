import numpy as np
import GraphObj as go


if __name__ == "__main__":

    N = 5
    vertices = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
    G = go.GraphObj(N)

    incr_dist = 1
    for vertex in vertices:
        G.add_node(go.Node(vertex[0]), go.Node(vertex[1], dist=incr_dist))
        incr_dist += 1

    keys = G.get_key_obj()
    m, l, d = G.types
    line_length = 70

    print("\nAdjacency {0}:".format(m))
    G.create(m)
    [print("-", end="") for i in range(line_length)]
    print("\n{0}".format(G.get()))
    [print("=", end="") for i in range(line_length)]
    print("\n")
    print("\nAdjacency dist {0}:".format(m))
    G.create(m, dist=True)
    [print("-", end="") for i in range(line_length)]
    print("\n{0}".format(G.get()))
    [print("=", end="") for i in range(line_length)]
    print("\n")
    print("\nAdjacency object {0}:".format(m))
    G.create(m, dt=np.object)
    print("\n{0}".format(G.get()))
    [print("=", end="") for i in range(line_length)]
    print("\n")

    print("\nAdjacency {0}:".format(l))
    G.create(l)
    [print("-", end="") for i in range(line_length)]
    print("\n{0}".format(G.get()))
    [print("=", end="") for i in range(line_length)]
    print("\n")
    print("\nAdjacency object {0}:".format(l))
    G.create(l, dt=np.object)
    print("\n{0}".format(G.get()))
    [print("=", end="") for i in range(line_length)]
    print("\n")

    print("\nAdjacency {0}:".format(d))
    G.create(d)
    [print("-", end="") for i in range(line_length)]
    print("\n{0}".format(G.get()))
    [print("=", end="") for i in range(line_length)]
    print("\n")
    print("\nAdjacency object {0}:".format(d))
    G.create(d, dt=np.object)
    print("\n{0}".format(G.get()))
    [print("=", end="") for i in range(line_length)]
    print("\n")

# Output:
"""
Adjacency matrix:
----------------------------------------------------------------------
[[0 1 0 0 1]
 [1 0 1 1 1]
 [0 1 0 1 0]
 [0 1 1 0 1]
 [1 1 0 1 0]]
======================================================================


Adjacency dist matrix:
----------------------------------------------------------------------
[[0 1 0 0 2]
 [1 0 3 4 5]
 [0 3 0 6 0]
 [0 4 6 0 7]
 [2 5 0 7 0]]
======================================================================


Adjacency object matrix:

[[0 <GraphObj.Node object at 0x7fd4866344f0> 0 0
  <GraphObj.Node object at 0x7fd486634580>]
 [<GraphObj.Node object at 0x7fd4866344f0> 0
  <GraphObj.Node object at 0x7fd4866345e0>
  <GraphObj.Node object at 0x7fd4866346a0>
  <GraphObj.Node object at 0x7fd486634700>]
 [0 <GraphObj.Node object at 0x7fd4866345e0> 0
  <GraphObj.Node object at 0x7fd486634760> 0]
 [0 <GraphObj.Node object at 0x7fd4866346a0>
  <GraphObj.Node object at 0x7fd486634760> 0
  <GraphObj.Node object at 0x7fd486634820>]
 [<GraphObj.Node object at 0x7fd486634580>
  <GraphObj.Node object at 0x7fd486634700> 0
  <GraphObj.Node object at 0x7fd486634820> 0]]
======================================================================


Adjacency list:
----------------------------------------------------------------------
[[1, 4], [2, 3, 4], [3], [4], []]
======================================================================


Adjacency object list:

[[<GraphObj.Node object at 0x7fd4866344f0>,
<GraphObj.Node object at 0x7fd486634580>],
[<GraphObj.Node object at 0x7fd4866345e0>,
<GraphObj.Node object at 0x7fd4866346a0>,
<GraphObj.Node object at 0x7fd486634700>],
[<GraphObj.Node object at 0x7fd486634760>],
[<GraphObj.Node object at 0x7fd486634820>],
[]]
======================================================================


Adjacency dict:
----------------------------------------------------------------------
{0: [1, 4], 1: [2, 3, 4], 2: [3], 3: [4], 4: []}
======================================================================


Adjacency object dict:

{0: [<GraphObj.Node object at 0x7fd4866344f0>,
<GraphObj.Node object at 0x7fd486634580>],
1: [<GraphObj.Node object at 0x7fd4866345e0>,
<GraphObj.Node object at 0x7fd4866346a0>,
<GraphObj.Node object at 0x7fd486634700>],
2: [<GraphObj.Node object at 0x7fd486634760>],
3: [<GraphObj.Node object at 0x7fd486634820>],
4: []}
======================================================================


"""
