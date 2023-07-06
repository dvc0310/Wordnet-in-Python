import copy
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, v):
        if v not in self.adjacency_list:
            self.adjacency_list[v] = set()

    def add_edge(self, v, w):
        self.add_vertex(v)
        self.add_vertex(w)
        self.adjacency_list[v].add(w)
        
    def adj(self, v):
        return self.adjacency_list[v]

    def V(self):
        return len(self.adjacency_list)
    
    def _dfs(self, v, visited):
        visited.add(v)
        for neighbor in self.adj(v):
            if neighbor not in visited:
                self._dfs(neighbor, visited)

    
    def has_vertex(self, v):
        return v in self.adjacency_list
    
    def make_rooted(self):
        root = "entity"
        vertices = list(self.adjacency_list.keys())
        for v in vertices:
            self.add_edge(root, v)

    def is_rooted(self):
        visited = set()
        start_vertex = next(iter(self.adjacency_list))  # select a starting vertex
        self._dfs(start_vertex, visited)
        return len(visited) == self.V()  # return True if all vertices were visited, False otherwise
    
    def print_graph(self):
        for v, neighbors in self.adjacency_list.items():
            print(f"{v}: {' '.join(map(str, neighbors))}")
    
    def _detect_cycle_helper(self, vertex, state):
        state[vertex] = "visiting"
        
        for neighbour in self.adjacency_list[vertex]:
            if state[neighbour] == "visiting":
                return True
            elif state[neighbour] == "unvisited":
                if self._detect_cycle_helper(neighbour, state):
                    return True

        state[vertex] = "visited"
        return False

    def has_cycle(self):
        state = {v: "unvisited" for v in self.adjacency_list}

        for vertex in self.adjacency_list:
            if state[vertex] == "unvisited":
                if self._detect_cycle_helper(vertex, state):
                    return True

        return False

    def find_euler_path(self):
        graph_copy = copy.deepcopy(self.adjacency_list)
        degrees = {v: len(neighbours) for v, neighbours in graph_copy.items()}
        start = 0
        odd_degrees = [v for v, degree in degrees.items() if degree % 2 == 1]
        
        if len(odd_degrees) == 2:
            start = odd_degrees[0]
        elif len(odd_degrees) > 2:
            return None  

        stack = [start]
        path = []

        while stack:
            v = stack[-1]
            if degrees[v] == 0:  
                path.append(stack.pop())
            else:
                for neighbor in graph_copy[v]:
                    if neighbor in graph_copy[v]:
                        stack.append(neighbor)
                        graph_copy[v].remove(neighbor)
                        graph_copy[neighbor].remove(v)
                        degrees[v] -= 1
                        degrees[neighbor] -= 1
                        break

        return path[::-1] 


