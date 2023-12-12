# Creating a class to represent a simple graph
class Graph:
    def __init__(self):
        # Creating a dictionary to represent the graph
        # Grafiği temsil etmek için bir sözlük oluşturuyoruz
        self.graph = {}

    # Adding an edge to the graph
    def add_edge(self, vertex, neighbor):
        # Adding an edge; creating the vertex if it doesn't exist yet
        # Bir kenar ekliyoruz; eğer düğüm henüz yoksa oluşturuyoruz
        if vertex not in self.graph:
            self.graph[vertex] = []
        self.graph[vertex].append(neighbor)

# Implementing the DFS algorithm
def dfs(graph, start, visited):
    # If the vertex has not been visited
    # Eğer düğüm ziyaret edilmemişse
    if start not in visited:
        # Mark the vertex as visited
        # Düğümü ziyaret edildi olarak işaretle
        print("Visiting:", start)
        visited.add(start)
        # Call DFS to visit the neighbors of the vertex
        # Düğümün komşularını ziyaret etmek için DFS'yi çağır
        for neighbor in graph.get(start, []):
            dfs(graph, neighbor, visited)

# Creating an example graph
# Örnek bir graf oluşturuyoruz
example_graph = Graph()
example_graph.add_edge(1, 2)
example_graph.add_edge(1, 3)
example_graph.add_edge(2, 4)
example_graph.add_edge(2, 5)
example_graph.add_edge(3, 6)

# Starting DFS
# DFS'yi başlatıyoruz
visited_nodes = set()
dfs(example_graph.graph, 1, visited_nodes)
