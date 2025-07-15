def rotate( matrix: list[list[int]]) -> None:
    # transpose
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if i==j:
                break
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]


    left,right=0,n-1
    while left < right:
        for i in range(n):
            matrix[i][left],matrix[i][right] = matrix[i][right],matrix[i][left]
        
        left+=1
        right-=1
    
    print(matrix)

            
        


rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])