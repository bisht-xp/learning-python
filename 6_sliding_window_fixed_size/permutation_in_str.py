def checkInclusion( s1: str, s2: str) -> bool:
    n,k=len(s2),len(s1)
    p_count=[0]*26
    window_count = [0]*26
    
    for s in s1:
        p_count[ord(s) - ord('a')] += 1

    for i in range(n):
        window_count[ord(s2[i]) - ord('a')] += 1

        if i >= k:
            window_count[ord(s2[i-k]) - ord('a')] -= 1
        
        if window_count == p_count:
            return True
    
    return False

print(checkInclusion("ab", "eidboaoo"))