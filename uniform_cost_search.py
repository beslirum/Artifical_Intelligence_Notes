# UNIFORM-COST-SEARCH algorithm using priority queue
function UNIFORM-COST-SEARCH(problem) returns a solution, or failure
    # Initialize the initial node with the initial state and path cost of 0
    #İlk düğümü, ilk durumu ve yol maliyetini SIFIR ile başlatın.
    node ← a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
    
    # Initialize the frontier with the initial node as the only element
    #Frontier'ı tek eleman olarak başlangıç düğümü ile başlatın
    frontier ← a priority queue ordered by PATH-COST, with node as the only element
    
    # Initialize the set of explored states as empty
    #explored state'leri boş bırakalım.
    explored ← an empty set
    
    # Main search loop
    loop do
        # Check if the frontier is empty, return failure if so
        #Frontierin boş olup olmadığını kontrol edin, boşsa failure döndürün
        if EMPTY?(frontier) then return failure
        
        # Choose the lowest-cost node from the frontier
        #Frontierden en düşük maliyetli düğümü seçin
        node ← POP(frontier)
        
        # Check if the goal state is reached, return the solution if true
        #Hedef duruma ulaşılıp ulaşılmadığını kontrol edin, doğruysa çözümü döndürün
        if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
        
        # Add the current node's state to the set of explored states
        #Geçerli düğümün durumunu explored states kümesine ekleyin
        add node.STATE to explored
        
        # Expand the current node by generating child nodes for each possible action
        #Her olası eylem için alt düğümler oluşturarak mevcut düğümü genişletin
        for each action in problem.ACTIONS(node.STATE) do
            # Generate a child node based on the current action
            #Geçerli eyleme göre bir alt düğüm oluştur
            child ← CHILD-NODE(problem, node, action)
            
            # Check if the child state is not in explored or frontier
            #child state'in explored veya frontierde olup olmadığını kontrol et
            if child.STATE is not in explored or frontier then
                # Add the child to the frontier
                #child node'u frontier node'a ekle
                frontier ← INSERT(child, frontier)
            else if child.STATE is in frontier with higher PATH-COST then
                # Replace the frontier node with the child if it has a lower path cost
                #Daha düşük bir yol maliyetine sahipse frontier düğümünü alt düğümle değiştirin
                replace that frontier node with child
