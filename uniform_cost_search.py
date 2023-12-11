# UNIFORM-COST-SEARCH algorithm using priority queue
function UNIFORM-COST-SEARCH(problem) returns a solution, or failure
    # Initialize the initial node with the initial state and path cost of 0
    node ← a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
    
    # Initialize the frontier with the initial node as the only element
    frontier ← a priority queue ordered by PATH-COST, with node as the only element
    
    # Initialize the set of explored states as empty
    explored ← an empty set
    
    # Main search loop
    loop do
        # Check if the frontier is empty, return failure if so
        if EMPTY?(frontier) then return failure
        
        # Choose the lowest-cost node from the frontier
        node ← POP(frontier)
        
        # Check if the goal state is reached, return the solution if true
        if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
        
        # Add the current node's state to the set of explored states
        add node.STATE to explored
        
        # Expand the current node by generating child nodes for each possible action
        for each action in problem.ACTIONS(node.STATE) do
            # Generate a child node based on the current action
            child ← CHILD-NODE(problem, node, action)
            
            # Check if the child state is not in explored or frontier
            if child.STATE is not in explored or frontier then
                # Add the child to the frontier
                frontier ← INSERT(child, frontier)
            else if child.STATE is in frontier with higher PATH-COST then
                # Replace the frontier node with the child if it has a lower path cost
                replace that frontier node with child
