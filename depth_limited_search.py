
function depth_limited_search(node, goal, depth_limit):
    if node.state == goal:
        return solution(node)
    elif depth_limit == 0:
        return "cutoff"
    else:
        cutoff_occurred = False
        for child in node.expand():
            result = depth_limited_search(child, goal, depth_limit - 1)
            if result == "cutoff":
                cutoff_occurred = True
            elif result != "failure":
                return result
        if cutoff_occurred:
            return "cutoff"
        else:
            return "failure"

function depth_limited_search_start(initial_state, goal, max_depth):
    initial_node = Node(initial_state)
    return depth_limited_search(initial_node, goal, max_depth)
