from collections import deque;

def orangesRotting(grid: list[list[int]]) -> int:
    rows,cols = len(grid),len(grid[0])
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    time_taken = 0
    visited = set()
    queue = deque()

    fresh_count = 0


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r,c))
                visited.add((r,c))
            elif grid[r][c] == 1:
                fresh_count += 1

    if fresh_count == 0:
        return 0

    while queue:
        for _ in range(len(queue)):
            (ro,co) = queue.popleft()
            for dr,dc in directions:
                nr,nc = ro+dr,dc+co
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 2 or grid[nr][nc] == 0 or (nr,nc) in visited:
                    continue
                queue.append((nr,nc))
                fresh_count -= 1
                visited.add((nr,nc))
        
        time_taken += 1
    


    return time_taken-1 if fresh_count == 0 else -1


grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))