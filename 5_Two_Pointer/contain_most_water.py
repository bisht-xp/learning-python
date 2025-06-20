def maxArea(height: list[int]) -> int:
    ans = 0
    i,j=0,len(height)-1

    while i < j:
        result = (j-i)*min(height[i], height[j])
        ans = max(ans,result)
        if height[i] < height[j]:
            i +=1
        else:
            j -=1
    
    return ans

print(maxArea([0,1,3]))