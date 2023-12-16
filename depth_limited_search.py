function depth_limited_search(node, goal, depth_limit):
    if node.state == goal:
        return solution(node)  # Hedef durumu bulunduğunda çözümü döndür
    elif depth_limit == 0:
        return "cutoff"  # Derinlik limitine ulaşıldığında "cutoff" durumunu döndür
    else:
        cutoff_occurred = False
        for child in node.expand():
            result = depth_limited_search(child, goal, depth_limit - 1)
            if result == "cutoff":
                cutoff_occurred = True
            elif result != "failure":
                return result  # Başarılı bir çözüm bulunduğunda çözümü döndür
        if cutoff_occurred:
            return "cutoff"  # Alt düğümlerde "cutoff" durumu yaşandı
        else:
            return "failure"  # Bu düğümde başka bir çözüm bulunamadı

function depth_limited_search_start(initial_state, goal, max_depth):
    initial_node = Node(initial_state)
    return depth_limited_search(initial_node, goal, max_depth)
