def productExceptSelf( nums: list[int]) -> list[int]:
    n = len(nums)
    l_arr = [1] * n
    l_arr[0] = nums[0]
    for i in range(1, n):
        l_arr[i] = nums[i] * l_arr[i-1]

    r_arr = [1] * n
    r_arr[-1] = nums[-1]
    for i in range(n-2, -1, -1):
        r_arr[i] = nums[i] * r_arr[i+1]
    
    print(l_arr, r_arr)

    ans = [1]*n
    for i in range(n):
        if i == 0:
            ans[i] = r_arr[i+1]
        elif i == n-1:
            ans[i] = l_arr[i-1]
        else:
            ans[i] = r_arr[i+1]* l_arr[i-1]

    return ans

print("asn: ", productExceptSelf([1,2,3,4]))