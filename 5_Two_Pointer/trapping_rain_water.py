def trap( height: list[int]) -> int:
    n = len(height)
    l_arr = [0]*n
    r_arr = [0]*n
    l_arr[0] = height[0]
    r_arr[n-1] = height[n-1]

    for i in range(1,n):
        l_arr[i] = max(l_arr[i-1], height[i])
        r_arr[n-1-i] = max(r_arr[n-i], height[n-1-i])
    
    ans = 0

    # print(l_arr, r_arr)
    for i in range(n):
        ans += min(l_arr[i], r_arr[i]) - height[i] 

    return ans

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))