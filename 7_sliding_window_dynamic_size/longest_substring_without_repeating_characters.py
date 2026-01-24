def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    i,j=0,0
    unique_char = {}
    ans = -1
    while j < n:
        if s[j] in unique_char and  unique_char[s[j]] != 0:
            # will something here
            while i < j and s[i] != s[j]:
                unique_char[s[i]] -= 1
                i += 1
            
            unique_char[s[i]]-= 1
            i += 1

        unique_char[s[j]] = unique_char.get(s[j], 0) + 1
        ans = max(ans, j-i+1)
        j += 1
    

    return ans

print(lengthOfLongestSubstring("zxyzxyz"))