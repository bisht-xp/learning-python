def spiralOrder( matrix: list[list[int]]) -> list[int]:
    result=[]
    top=0
    left=0
    bottom=len(matrix)-1
    right=len(matrix[0])-1

    while top <= bottom and left <= right:
        for i in range(top,right+1):
            result.append(matrix[top][i])
        top+=1

        for j in range(top,bottom+1):
            result.append(matrix[j][right])
        
        right -=1

        if top <= bottom:
            for i in range(right,left-1, -1):
                result.append(matrix[bottom][i])
            
            bottom -= 1
        
        if left <= right:
            for j in range(bottom,top-1,-1):
                result.append(matrix[j][left])
            left +=1
    
    return result


print(spiralOrder([[7],[9],[6]]))