from collections import deque

def breadth_first_search(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            print(current_node)  # Düğümü ziyaret et
            visited.add(current_node)
            queue.extend(neighbor for neighbor in graph[current_node] if neighbor not in visited)

# Örnek bir graf yapısı
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Başlangıç düğümünü belirle
start_node = 'A'

# Genişlik öncelikli aramayı başlat
breadth_first_search(graph, start_node)

