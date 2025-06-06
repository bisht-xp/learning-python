def mountain(arr):
    i,j=1,len(arr)-2
    longest = 0
    while i <= j:
        if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
            k = i
            ans = 1
            while k >= 1 and arr[k] > arr[k-1]:
                ans += 1
                k -= 1
            while i <= j and arr[i] > arr[i+1]:
                ans += 1
                i += 1
            
            longest = max(longest, ans)
        else: 
            i += 1
    

    return longest


arr = [5,6,1,2,3,4,5,4,3,2,0,1,2,3,-2,4]

print("print longest: ", mountain(arr))
        
