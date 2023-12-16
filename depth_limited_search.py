# Türkçe: Derinlik sınırlı arama algoritması için ana fonksiyon.
# İngilizce: Main function for depth-limited search algorithm.
function depth_limited_search(node, goal, depth_limit):
    # Türkçe: Eğer düğümün durumu hedef durum ile eşleşiyorsa,
    # çözümü döndür.
    # İngilizce: If the state of the node matches the goal state,
    # return the solution.
    if node.state == goal:
        return solution(node)

    # Türkçe: Eğer derinlik limiti 0 ise, "cutoff" durumunu döndür.
    # İngilizce: If the depth limit is 0, return "cutoff".
    elif depth_limit == 0:
        return "cutoff"

    # Türkçe: Aksi takdirde, "cutoff" durumu yaşanıp yaşanmadığını kontrol et.
    # İngilizce: Otherwise, check whether the "cutoff" state occurred.
    else:
        cutoff_occurred = False

        # Türkçe: Düğümü genişlet ve her bir alt düğüm için derinlik
        # sınırlı aramayı tekrarla.
        # İngilizce: Expand the node and recursively perform depth-limited
        # search for each child node.
        for child in node.expand():
            result = depth_limited_search(child, goal, depth_limit - 1)
            if result == "cutoff":
                cutoff_occurred = True
            elif result != "failure":
                return result

        # Türkçe: Eğer alt düğümlerde "cutoff" durumu yaşandıysa,
        # "cutoff" durumunu döndür.
        # İngilizce: If the "cutoff" state occurred in any child node,
        # return "cutoff".
        if cutoff_occurred:
            return "cutoff"

        # Türkçe: Aksi takdirde, başka bir çözüm bulunamadığı için
        # "failure" durumunu döndür.
        # İngilizce: Otherwise, return "failure" as no other solution
        # was found at this node.
        else:
            return "failure"

# Türkçe: Derinlik sınırlı arama algoritmasını başlatan fonksiyon.
# İngilizce: Function that initiates the depth-limited search algorithm.
function depth_limited_search_start(initial_state, goal, max_depth):
    # Türkçe: Başlangıç durumundan bir düğüm oluştur.
    # İngilizce: Create a node from the initial state.
    initial_node = Node(initial_state)

    # Türkçe: Derinlik sınırlı arama fonksiyonunu başlat ve sonucu döndür.
    # İngilizce: Initiate the depth-limited search function and return the result.
    return depth_limited_search(initial_node, goal, max_depth)
