import heapq

def reorganizeString( s: str) -> str:
    hash_map = [0]*26

    for st in s:
        hash_map[ord(st)- ord('a')] += 1

    max_count=0
    val=0
    for i in range(len(hash_map)):
        if max_count < hash_map[i]:
            max_count = hash_map[i]
            val = i

    if max_count > (len(s)+1)//2:
        return ""
    
    res = ['']*len(s)

    idx = 0
    while hash_map[val] > 0:
        res[idx] = chr(ord('a') + val)
        idx += 2
        hash_map[val] -= 1

    for i in range(len(hash_map)):
        while hash_map[i]:
            if idx >= len(s):  
                idx = 1

            res[idx] = chr(ord('a') + i)
            idx += 2
            hash_map[i] -= 1

    return ''.join(res)

print(reorganizeString("abbabbaaab"))
    
        
                
        

        
        