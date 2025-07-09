def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ""
    
    freq_map = {}
    k = len(t)
    for ch in t:
        freq_map[ch] = 1 + freq_map.get(ch, 0)
    
    left=0
    min_len = float('inf')
    ans = ""
    for right,ch in enumerate(s):
        if ch in freq_map:
            if freq_map[ch] > 0:
                k -= 1
            freq_map[ch] -= 1
        
        while k <= 0:
           
            if min_len > right-left+1:
                min_len = right-left+1
                ans = s[left:right+1]

            if s[left] in freq_map:
                freq_map[s[left]] += 1
                if freq_map[s[left]] > 0:
                    k += 1
            left += 1
    
    return ans

print(minWindow("cabwefgewcwaefgcf", "cae"))
            