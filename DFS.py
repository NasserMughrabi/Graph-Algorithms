# Depth-First-Search
def BFS(startNode) :    
    stack = []
    visited = []
    stack.append(startNode)

    currNode = startNode    
    while len(stack) > 0 : # O(V)
        currNode = stack.pop()
        for n in range(currNode.neighbors) : #O(E)
            if n not in visited :
                stack.append(currNode)
                visited.append(currNode)