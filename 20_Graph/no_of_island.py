def numIslands(grid: list[list[str]]) -> int:
    count = 0
    def helper(r,c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
            return

        grid[r][c] = "0"
        (helper(r-1,c) or helper(r+1,c) or helper(r,c-1) or helper(r,c+1))

        return; 

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                helper(r,c)
                count += 1
    
    return count



grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid))
