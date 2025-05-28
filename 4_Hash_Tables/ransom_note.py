def canConstruct(ransomNote: str, magazine: str) -> bool:
    map_char = {}
    for ch in magazine:
        if ch in map_char:
            map_char[ch] += 1
        else:
            map_char[ch] = 1
    
    for ch in ransomNote:
        if ch not in map_char or map_char[ch] == 0:
            return False
        map_char[ch] -= 1
    
    return True

print(canConstruct("aa", "aab"))