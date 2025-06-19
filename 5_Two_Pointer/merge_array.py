def merge( nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    k = m+n-1
    i=m-1
    j=n-1

    while i >= 0 and j >= 0:
        if nums1[i] < nums2[j]:
            nums1[k] = nums2[j]
            j -= 1
        else:
            nums1[k] = nums1[i]
            i -= 1
            
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j-=1
        k-=1

    return nums1




nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [4,5,6]
n = 3
print(merge(nums1,m,nums2,n))
