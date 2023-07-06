from bfsPath import BreadthFirstDirectedPaths
from collections.abc import Iterable

class SAP:
    def __init__(self, G):
        self.G = G

    def is_valid(self, v):
        return v in self.G.adjacency_list

    def ancestor(self, v, w):
        shortest_ancestor = None
        shortest_path = float("inf")

        v_list = v if isinstance(v, Iterable) else [v]
        w_list = w if isinstance(w, Iterable) else [w]

        for v in v_list:
            for w in w_list:
                if not (self.is_valid(v) and self.is_valid(w)):
                    continue

                bfs_v = BreadthFirstDirectedPaths(self.G, v)
                bfs_w = BreadthFirstDirectedPaths(self.G, w)

                for vertex in self.G.adjacency_list:
                    if bfs_v.has_path_to(vertex) and bfs_w.has_path_to(vertex):
                        path_length = bfs_v.dist_to(vertex) + bfs_w.dist_to(vertex)

                        if path_length < shortest_path:
                            shortest_path = path_length
                            shortest_ancestor = vertex

        return shortest_ancestor

    def length(self, v, w):
        shortest_path = float("inf")

        v_list = v if isinstance(v, Iterable) else [v]
        w_list = w if isinstance(w, Iterable) else [w]

        for v in v_list:
            for w in w_list:
                if not ((v >= 0 and v <= self.G.V() - 1) and (w >= 0 and w <= self.G.V() - 1)):
                    continue

                bfs_v = BreadthFirstDirectedPaths(self.G, v)
                bfs_w = BreadthFirstDirectedPaths(self.G, w)

                ancestor = self.ancestor(v, w)

                if ancestor == -1:
                    continue

                path_length = bfs_v.dist_to(ancestor) + bfs_w.dist_to(ancestor)
                if path_length < shortest_path:
                    shortest_path = path_length

        if shortest_path == float("inf"):
            return -1

        return shortest_path
