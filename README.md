
# 🤖 Yapay Zeka Algoritmaları

Bu depo, yapay zeka dersinde öğrenilen temel arama algoritmalarının kaba kodlarını içermektedir.

## Algoritmalar

### 1. Genişlik Öncelikli Arama (Breadth First Search)
   - **Dosya Adı:** [breadth_first_search.py](algoritmalar/breadth_first_search.py)
   
   Genişlik öncelikli arama, ağaç veya grafik yapılarda kökten başlayarak düğümleri geniş bir şekilde tarayan bir algoritmadır.

### 2. Maliyet Öncelikli Arama (Uniform Cost Search)
   - **Dosya Adı:** [uniform_cost_search.py](algoritmalar/uniform_cost_search.py)
   
   Maliyet öncelikli arama, düğümleri maliyetlerine göre sıralayarak en düşük maliyetli düğüme öncelik veren bir arama algoritmasıdır.

### 3. Derinlik Öncelikli Arama (Depth First Search)
   - **Dosya Adı:** [depth_first_search.py](algoritmalar/depth_first_search.py)
   
   Derinlik öncelikli arama, bir yoldan sona kadar derine inen ve ardından geri dönen bir arama algoritmasıdır.

### 4. Sınırlı Derinlik Arama (Depth Limited Search)
   - **Dosya Adı:** [depth_limited_search.py](algoritmalar/depth_limited_search.py)
   
   Sınırlı derinlik arama, derinlik öncelikli aramaya benzer ancak belirli bir derinlik sınırlaması getirir.

### 5. İteratif Derinleme Arama (Iterative Deepening Search)
   - **Dosya Adı:** [iterative_deepening_search.py](algoritmalar/iterative_deepening_search.py)
   
   İteratif derinleme arama, derinlik sınırlamasını artırarak daha geniş bir arama alanı kapsayan bir algoritmadır.

### 6. En İyi Öncelikli Arama (Best First Search)
   - **Dosya Adı:** [best_first_search.py](algoritmalar/best_first_search.py)
   
   En iyi öncelikli arama, bir hedefe ulaşmak için en "iyi" düğümü seçerek ilerleyen bir arama algoritmasıdır.

### 7. Cimri En İyi Öncelikli Arama (Greedy Best First Search)
   - **Dosya Adı:** [greedy_best_first_search.py](algoritmalar/greedy_best_first_search.py)
   
   Cimri en iyi öncelikli arama, her adımda en küçük tahmini maliyeti olan düğüme öncelik veren bir algoritmadır.

### 8. A Yıldızı Arama (A* Search)
   - **Dosya Adı:** [a_star_search.py](algoritmalar/a_star_search.py)
   
   A* arama, hem gerçek maliyet hem de tahmini maliyeti içeren bir değeri minimize ederek en iyi yolun bulunmasını amaçlar.

### 9. Özyinelemeli Genişlik Öncelikli Arama (Recursive BFS)
   - **Dosya Adı:** [recursive_bfs.py](algoritmalar/recursive_bfs.py)
   
   Özyinelemeli genişlik öncelikli arama, genişlik öncelikli aramayı özyinelemeli bir şekilde uygulayan bir algoritmadır.

## Kullanım

Her bir algoritma kendi dosyasında bağımsız olarak bulunmaktadır. İlgili algoritmayı çalıştırmak için ilgili dosyayı seçin ve çalıştırın.

```bash
python breadth_first_search.py
