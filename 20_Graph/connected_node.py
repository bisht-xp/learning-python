def countComponents(n: int, edges: list[list[int]]) -> int:
    nodes = {i: [] for i in range(n)}

    for a,b in edges:
        nodes[a].append(b)
        nodes[b].append(a)

    visited = set()
    count = 0
    def dfs(node):
        visited.add(node)

        for e in nodes[node]:
            if e not in visited:
                dfs(e)
        return
    

    for i in range(n):
        if i not in visited:
            count += 1
            dfs(i)
    
    return count

n=12
edges=[[0,1],[1,2],[2,3],[3,0],[4,5],[6,7],[7,4],[8,9],[10,11]]

print(countComponents(n,edges))