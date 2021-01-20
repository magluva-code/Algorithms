import numpy as np

class Node(object):
    def __init__(self, name, dist=None, reverse=False):
        self._name = name
        self._connected = False
        self._reverse = reverse
        self._dist = dist

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    @property
    def connected(self):
        return self._connected

    @connected.setter
    def connected(self, c):
        self._connected = c

    @property
    def reverse(self):
        return self._reverse

    @reverse.setter
    def reverse(self, r):
        self._reverse = r

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, d):
        self._dist = d


class GraphObj(object):
    def __init__(self, N):
        self.g = {Node(0) : []}
        self.n = N
        self.types = ["matrix", "list", "dict"]

    def add_node(self, src, node):
        exists = False
        for i in self.g.keys():
            if i.name == src.name:
                self.g[i].append(node)
                exists = True
                break
        if not exists:
            self.g[src] = []
            self.g[src].append(node)

    def get_key_obj(self):
        return list(self.g.keys())

    def get_key_names(self):
        return [i.name for i in self.g.keys()]

    def create(self, type, dist=False, dt=np.int32):
        keys = list(self.g.keys())
        self.m = np.zeros((self.n, self.n), dtype=dt)
        self.d = {i : list() for i in range(self.n)}
        self.ls = [list() for i in range(self.n)]
        if type not in self.types:
            raise Exception("Type: '{0}' is not supported..".format(type))
        self.t = type
        for k in keys:
            for v in self.g[k]:
                if self.t == "matrix":
                    if dt is np.object:
                        self._obj_matrix(k, v)
                    else:
                        self._matrix(k, v, dist)
                if self.t == "list":
                    if dt is np.object:
                        self._obj_list(k, v)
                    else:
                        self._list(k, v)
                if self.t == "dict":
                    if dt is np.object:
                        self._obj_dict(k, v)
                    else:
                        self._dict(k, v)

    def _obj_matrix(self, k, v):
        self.m[k.name][v.name] = v
        self.m[v.name][k.name] = v

    def _matrix(self, k, v, d):
        if d:
            self.m[k.name][v.name] = v.dist
            self.m[v.name][k.name] = v.dist
        else:
            self.m[k.name][v.name] = 1
            self.m[v.name][k.name] = 1

    def _obj_list(self, k, v):
        self.ls[k.name].append(v)

    def _list(self, k, v):
        self.ls[k.name].append(v.name)

    def _obj_dict(self, k, v):
        self.d[k.name].append(v)

    def _dict(self, k, v):
        self.d[k.name].append(v.name)

    def get(self):
        if self.t == "matrix":
            return self.m
        elif self.t == "list":
            return self.ls
        elif self.t == "dict":
            return self.d
        elif self.t == "graph":
            return self.g




if __name__ == "__main__":
    N = 4
    g = GraphObj(N)
    g.add_node(Node(0), Node(1, dist=3))
    g.add_node(Node(0), Node(3, dist=5))
    g.add_node(Node(1), Node(3, dist=4))
    g.add_node(Node(2), Node(1, dist=1))
    g.add_node(Node(3), Node(1, dist=4))
    m = g.get("graph")
    print(m)
    #print("{}: [{}, {}]\n{}: [{}]".format(keys[0].name, g.g[keys[0]][0].name, g.g[keys[0]][1].name,
                                          #keys[1].name, g.g[keys[1]][0].name))
    #g.add_node(2, Node(3, dist=2))
    #g.add_node(3, Node(0, dist=7))
