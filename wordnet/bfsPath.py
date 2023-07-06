from queue import Queue
from collections.abc import Iterable

class BreadthFirstDirectedPaths:
    INFINITY = float('inf')

    def __init__(self, G, s):
        self.marked = [False]*G.V()
        self.edgeTo = [0]*G.V()
        self.distTo = [self.INFINITY]*G.V()
        if isinstance(s, Iterable):
            self.validate_vertices(s)
        else:
            self.validate_vertex(s)
        self.bfs(G, s)

    def bfs(self, G, s):
        q = Queue()
        if isinstance(s, Iterable):
            for source in s:
                self.marked[source] = True
                self.distTo[source] = 0
                q.put(source)
        else:
            self.marked[s] = True
            self.distTo[s] = 0
            q.put(s)
        while not q.empty():
            v = q.get()
            for w in G.adj(v):
                if not self.marked[w]:
                    self.edgeTo[w] = v
                    self.distTo[w] = self.distTo[v] + 1
                    self.marked[w] = True
                    q.put(w)

    # ... rest of the class ...
    def has_path_to(self, v):
        self.validate_vertex(v)
        return self.marked[v]

    def dist_to(self, v):
        self.validate_vertex(v)
        return self.distTo[v]

    def path_to(self, v):
        self.validate_vertex(v)
        if not self.has_path_to(v):
            return None
        path = []
        x = v
        while self.distTo[x] != 0:
            path.append(x)
            x = self.edgeTo[x]
        path.append(x)
        return path[::-1]  # reverse the path

    def validate_vertex(self, v):
        V = len(self.marked)
        if v < 0 or v >= V:
            raise ValueError("vertex " + str(v) + " is not between 0 and " + str(V-1))

    def validate_vertices(self, vertices):
        if vertices is None:
            raise ValueError("argument is null")
        vertex_count = 0
        for v in vertices:
            vertex_count += 1
            if v is None:
                raise ValueError("vertex is null")
            self.validate_vertex(v)
        if vertex_count == 0:
            raise ValueError("zero vertices")