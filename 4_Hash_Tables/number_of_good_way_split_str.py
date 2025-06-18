
def helper_func(s: str, start_left = False) -> list[int]:
    n = len(s)
    unique_set = set()
    unique_list = [0]*n
    unique_ele = 0

    for i in range(n):
        if start_left:
            if s[i] not in unique_set:
                unique_set.add(s[i])
                unique_ele += 1
        
            unique_list[i] = unique_ele
        else:
            if s[n-1-i] not in unique_set:
                unique_set.add(s[n-1-i])
                unique_ele += 1
        
            unique_list[n-1-i] = unique_ele
    
    return unique_list


def numSplits( s: str) -> int:
    n = len(s)
    s_left = helper_func(s, True)
    s_right = helper_func(s)
    ans = 0
    for i in range(n-1):
        if s_left[i] == s_right[i+1]:
            ans += 1

    return ans

print(numSplits("aacaba"))