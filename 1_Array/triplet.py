def tripletSolution(arr, target_sum): 
    n = len(arr)
    ans = []
    for i in range(len(arr)-2):
        new_target = target_sum - arr[i]
        j = i+1
        k = n-1
        while j < k:
            if arr[j] + arr[k] == new_target:
                ans.append([arr[i], arr[j], arr[k]])
                k -= 1
            elif arr[j] + arr[k] > new_target:
               k -= 1
            else:
                j += 1
    
    return ans
        
        

        






array:list[int] = [1,2,3,4,5,6,7,8,9,15]
sum = 18

print("printallTriplet: ", tripletSolution(array, sum))