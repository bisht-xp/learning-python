from collections import deque

def shortestPathBinaryMatrix(grid: list[list[int]]) -> int:
    rows,cols = len(grid),len(grid[0])
    directions = [[-1,0],[1,0],[0,1],[0,-1],[-1,-1],[1,1],[1,-1],[-1,1]]

    def bfs(r,c):
        queue = deque()
        visited = set()
        queue.append((r,c))
        count = 1

        if(grid[r][c] == 1): 
            return -1

        visited.add((r,c))
        while queue:
            current_length = len(queue)
            for _ in range(current_length):
                (ro,co) = queue.popleft()
                if ro == rows-1 and co == cols-1:
                    return count

                for dr,dc in directions:
                    nr,nc = ro+dr,co+dc

                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 1 or (nr,nc) in visited:
                        continue

                    queue.append((nr,nc))
                    visited.add((nr,nc))

            count += 1

        return -1

    return bfs(0,0)


grid = [[0,0,0],[1,1,0],[1,1,0]]
print(shortestPathBinaryMatrix(grid))
