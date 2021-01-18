# Depth Search First class.

class DFS(object):
    """
    Class: DFS(object):
    ----------------------------------------------------------------------------
    This is a class that takes a dictionary of a tree or graph structure
    and performs a dfs via the depth_first_search method.
    Object is callable and returns dfs path.
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

    def __call__(self, src):
        return self.depth_first_search(src)

    def depth_first_search(self, src, path=list()):
        """
        @param:
            src (int) - Starting position for the search.
            path (list) - Ordered list of search results.
        @return:
            path (list) - Ordered list of search results.
        """
        if src not in path:
            path.append(src)
            if src not in self.d:
                return path
            for adj in self.d[src]:
                path = self.depth_first_search(adj, path)
        return path
