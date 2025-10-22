def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    i,j=0,len(matrix[0])-1

    while(i>=0 and j>=0 and i<len(matrix) and j<len(matrix[0])):
        if(matrix[i][j] == target):
            return True

        if(matrix[i][j] >= target):
            j-=1
        else:
            i+=1
    

    return False


matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]] 
target = 15

print(searchMatrix(matrix, target))