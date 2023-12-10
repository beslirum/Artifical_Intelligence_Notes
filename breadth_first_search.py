
from collections import deque

def breadth_first_search(problem):
    # Başlangıç durumu ve maliyeti sıfır olan bir düğüm oluştur
    node = Node(state=problem.initial_state, path_cost=0)

    # Eğer başlangıç durumu hedef durumu karşılıyorsa, başarıyla tamamlanmış bir çözüm döndür
    if problem.goal_test(node.state):
        return solution(node)

    # Genişlik öncelikli arama için FIFO kuyruğu oluştur, başlangıç düğümü ile başlat
    frontier = deque([node])

    # Daha önce incelenmiş durumları tutmak için boş bir küme oluştur
    explored = set()

    # Ana döngü
    while True:
        # Eğer kuyruk boşsa, başarısızlık durumu döndür
        if not frontier:
            return failure()

        # Kuyruğun başındaki düğümü çıkar (en sığ düğümü seçer)
        node = frontier.popleft()

        # Düğümün durumunu incelenmiş durumlar kümesine ekle
        explored.add(node.state)

        # Düğümün durumunda uygulanabilen her eylem için
        for action in problem.actions(node.state):
            # Çocuk düğümü oluştur
            child = child_node(problem, node, action)

            # Eğer çocuğun durumu daha önce incelenmemişse ve kuyrukta değilse
            if child.state not in explored and child not in frontier:
                # Eğer çocuk durumu hedef durumu karşılıyorsa, çözüm döndür
                if problem.goal_test(child.state):
                    return solution(child)

                # Çocuk düğümü kuyruğa ekle
                frontier.append(child)
