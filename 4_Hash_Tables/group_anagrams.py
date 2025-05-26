def groupAnagrams(strs: list[str])-> list[list[str]]:
    sorted_anagram: dict[str, list[str]] = {} # type: ignore
    ans = []
    for str in strs:
        key = ''.join(sorted(str))
        if key in sorted_anagram:
            sorted_anagram[key].append(str)
        else:
            sorted_anagram[key] = [str]
    
    for value in sorted_anagram.values():
        ans.append(value)
    
    return ans

print(groupAnagrams(["a"]))
