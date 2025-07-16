def setZeroes( matrix: list[list[int]]) -> None:
    zero_pairs = []
    m,n=len(matrix),len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                pair = (i,j)
                zero_pairs.append(pair)

    for pair in zero_pairs:  
        i,j = pair[0],pair[1]
        #left
        for right in range(j-1,-1,-1):
            matrix[i][right] = 0

        #right
        for left in range(j+1,n):
            matrix[i][left] = 0

        #top
        for bottom in range(i-1, -1, -1):
            matrix[bottom][j]=0
        
        #bttom
        for top in range(i+1,m):
            matrix[top][j] = 0

    print(matrix)


setZeroes([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]])