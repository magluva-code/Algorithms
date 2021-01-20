# Dijkstra algorithm class.


class Dijkstra(object):
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)

    def __call__(self, src):
        return self.find_shortest_path(src)

    def find_shortest_path(self, src):
        dist = [float("inf")]*self.n
        dist[src] = 0
        dict_n_dist = {src : 0}

        while dict_n_dist:
            src_n = min(dict_n_dist, key = lambda k: dict_n_dist[k])
            del dict_n_dist[src_n]
            for dist_n in self.graph[src_n]:
                adj_n = dist_n.name
                adj_n_dist = dist_n.dist
                if dist[adj_n] > dist[src_n] + adj_n_dist:
                    dist[adj_n] = dist[src_n] + adj_n_dist
                    dict_n_dist[adj_n] = dist[adj_n]
        return dist
