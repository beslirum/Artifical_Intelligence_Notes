
# Basit bir graf sınıfı oluşturuyoruz
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, neighbor):
        if vertex not in self.graph:
            self.graph[vertex] = []
        self.graph[vertex].append(neighbor)

def dfs(graph, start, visited):
    if start not in visited:
        print("Visiting:", start)
        visited.add(start)
        for neighbor in graph.get(start, []):
            dfs(graph, neighbor, visited)

# Örnek bir graf oluşturuyoruz
example_graph = Graph()
example_graph.add_edge(1, 2)
example_graph.add_edge(1, 3)
example_graph.add_edge(2, 4)
example_graph.add_edge(2, 5)
example_graph.add_edge(3, 6)

# DFS'yi başlatıyoruz
visited_nodes = set()
dfs(example_graph.graph, 1, visited_nodes)
