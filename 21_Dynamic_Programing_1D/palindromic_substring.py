def countSubstrings(s: str) -> int:
    ans = 0
    for i in range(len(s)):
        # odd
        left,right=i,i
        longest = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            
            ans += 1
            
            left -= 1
            right += 1
        
        left,right = i,i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            ans += 1
            
            left -= 1
            right += 1
        
    return ans

s = "aaa"
print(countSubstrings(s))

        