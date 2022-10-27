# Breadth-First-Search
def BFS(startNode) :    
    queue = []
    visited = []
    queue.append(startNode)

    currNode = startNode    
    while len(queue) > 0 : # O(V)
        currNode = queue.pop(0)
        for n in range(currNode.neighbors) : #O(E)
            if n not in visited :
                queue.append(currNode)
                visited.append(currNode)