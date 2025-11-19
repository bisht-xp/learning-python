def validTree(n: int, edges: list[list[int]]) -> bool:
    nodes = {i: [] for i in range(n)}
    for a,b in edges:
        nodes[a].append(b)
        nodes[b].append(a)

    visited = set()
    def dfs(node, prev):
        if node in visited:
            return False
        
        visited.add(node)
        for e in nodes[node]:
            if(e == prev):
                continue

            if not dfs(e, node):
                return False
        
        return True

    if(not dfs(0,-1)):
        return False
    
    return len(visited) == n

n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
print(validTree(n,edges))