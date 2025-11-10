def exist(board: list[list[str]], word: str) -> bool:
    row,col=len(board),len(board[0])
    def helper(r,c,i):
        if i == len(word):
            return True
        
        if (r < 0 or c < 0 or r >= row or c >= col or word[i] != board[r][c] or board[r][c] == "#"):
            return False 

        board[r][c] = "#"
        res = (helper(r-1,c,i+1) or helper(r,c+1,i+1) or helper(r+1,c,i+1)or helper(r,c-1,i+1))

        board[r][c] = word[i]
        return res
    
    for i in range(row):
        for j in range(col):
            if(helper(i,j,0)):
                return True
            
    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))