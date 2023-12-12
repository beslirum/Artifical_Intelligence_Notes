
def dfs(vertex, visited):
    if vertex not in visited:
        visited.add(vertex)
        process(vertex)
        for neighbor in get_neighbors(vertex):
            dfs(neighbor, visited)

def get_neighbors(vertex):
    # Bu fonksiyon, verilen düğümün komşularını döndürür.
    # Örneğin, bir grafikteki bağlı düğümleri alabilir.
    pass

def process(vertex):
    # Bu fonksiyon, her ziyaret edilen düğüm için özel işlemleri gerçekleştirir.
    # Örneğin, düğüm değerini yazdırabilir veya başka bir işlem yapabilir.
    pass

def main():
    visited = set()
    for vertex in get_all_vertices():
        dfs(vertex, visited)

if __name__ == "__main__":
    main()
