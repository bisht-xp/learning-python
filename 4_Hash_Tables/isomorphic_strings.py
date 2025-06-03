from collections import defaultdict

def isIsomorphic( s: str, t: str) -> bool:
    map_s_chars = {}
    map_t_chars = {}
    n = len(s)
    for i in range(n):
        if s[i] in map_s_chars and map_s_chars[s[i]] != t[i]:
            return False    
        map_s_chars[s[i]] = t[i]
    for i in range(n):
        if t[i] in map_t_chars and map_t_chars[t[i]] != s[i]:
            return False
        map_t_chars[t[i]] = s[i]
    return True    
print(isIsomorphic("foo", "title"))