def dfs(vertex, visited):
    # Eğer düğüm ziyaret edilmemişse
    if vertex not in visited:
        # Düğümü ziyaret edildi olarak işaretle
        visited.add(vertex)
        # Düğümü işle (örneğin, yazdır veya özel bir işlem yap)
        process(vertex)
        # Düğümün komşularını ziyaret etmek için DFS'yi çağır
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
    # Ziyaret edilen düğümleri takip etmek için bir küme oluştur
    visited = set()
    # Tüm düğümleri başlatma noktası olarak alarak DFS'yi başlat
    for vertex in get_all_vertices():
        dfs(vertex, visited)

if __name__ == "__main__":
    # Ana fonksiyonu çağır
    main()
