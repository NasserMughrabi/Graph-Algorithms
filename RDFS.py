# Recursive-Depth-First-Search
def recursiveDFS(startNode, visited) :
    if startNode not in visited :
        visited.append(startNode)

    for n in startNode.neighbors :
            recursiveDFS(n, visited)
