# Breadth First Search


class BFS(object):
    """
    Class: BFS(object):
    ----------------------------------------------------------------------------
    This is a class that takes a dictionary of a tree or graph structure
    and performs bfs via the breadth_search_first method.
    Object is callable and returns bfs path.
    ----------------------------------------------------------------------------
    @param:
        adj_dict (dictionary)
    @methods:
        depth_first_search(src, path)
    @return:
        path (list)
    ============================================================================
    """
    def __init__(self, adj_dict):
        self.d = adj_dict
        self.n = len(adj_dict)

    def __call__(self, src):
        return self.breadth_search_first(src)

    def breadth_search_first(self, src, path=list(), queue=list()):
        """
        @param:
            src (int) - Starting position for the search.
            queue (list) - List of queued nodes.
            path (list) - Ordered list of search results.
        @return:
            path (list) - Ordered list of search results.
        """
        path.append(src)
        queue.append(src)
        while queue:
            s = queue.pop(0)
            for adj in self.d[s]:
                if adj not in path:
                    path.append(adj)
                    queue.append(adj)
        return path
