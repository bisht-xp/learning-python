from collections import deque

def maxAreaOfIsland( grid: list[list[int]]) -> int:
    max_area = 0
    rows,cols=len(grid),len(grid[0])
    visit = set()

    # DFS Approch
    # def helper(r, c):
    #     if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r,c) in visit:
    #         return 0
        
    #     visit.add((r,c))

    #     return 1 + (helper(r+1,c) + helper(r-1,c) + helper(r,c-1) + helper(r,c+1))
    
    # for r in range(rows):
    #     for c in range(cols):
    #         if grid[r][c] == 1:
    #             max_area = max(max_area, helper(r,c))

    # BFS Approach
    direction = [[-1,0], [1,0],[0,-1],[0,1]]
    def bfs(r,c):
        queue = deque()
        queue.append((r,c))
        count = 0
        visit.add((r,c))
        while(queue):
            (ro,co) = queue.pop()
            count += 1
            for dr,dc in direction:
                nr,nc = dr+ro,dc+co
                if nr < 0 or nc < 0 or nr >= rows or nc >=cols or grid[nr][nc] == 0 or (nr,nc) in visit:
                    continue
                queue.append((nr,nc))
                visit.add((nr,nc))
        
        return count
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_area = max(max_area, bfs(r,c))

    return max_area
    

    

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIsland(grid))