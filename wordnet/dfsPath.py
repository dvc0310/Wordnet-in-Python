class DFSPath:
    def __init__(self, G, source):
        self.marked = {}
        self.edge_to = {}
        self.dist_to = {}
        self.G = G
        if source not in self.marked:
            self.DFS(G, source)

    def DFS(self, G, source):
        stack = []
        self.marked[source] = True
        self.dist_to[source] = 0
        stack.append(source)

        while stack:
            current_vertex = stack.pop()

            for neighbor in G.adj(current_vertex):
                if neighbor not in self.marked:
                    self.marked[neighbor] = True
                    self.edge_to[neighbor] = current_vertex
                    self.dist_to[neighbor] = self.dist_to[current_vertex] + 1
                    stack.append(neighbor)

    def has_path_to(self, w):
        return w in self.marked


    def dist_to_edge(self, v):
        return self.dist_to.get(v, float('inf'))
    

    def dfsPath(self, vertex):
        path = []
        while vertex is not None:
            path.append(vertex)
            vertex = self.edge_to.get(vertex, None)
        return path
