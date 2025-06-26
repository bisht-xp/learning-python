from collections import Counter

def findAnagrams(s: str, p: str) -> list[int]:
    n=len(s)
    k=len(p)
    map_dict=Counter(p)
    i,j=0,0
    
    ans=[]

    while j < n:
        if k == 0:
            ans.append(i)
            map_dict[s[i]] += 1
            i += 1
            k += 1
        elif s[j] not in map_dict:
            while i < j:
                map_dict[s[i]] += 1
                i += 1
                k += 1
            j+=1
            i+=1
        elif s[j] in map_dict and k > 0 and map_dict[s[j]] > 0:
            map_dict[s[j]] -= 1
            j+= 1
            k -= 1
        else:
            map_dict[s[i]] += 1
            i += 1
            k += 1

    if k == 0:
        ans.append(i)
    return ans


print(findAnagrams("cbaebabacd", "abc"))
