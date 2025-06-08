from collections import defaultdict,Counter
import bisect

def numMatchingSubseq( s: str, words: list[str]) -> int:
    char_indices = defaultdict(list)
    for idx, ch in enumerate(s):
        char_indices[ch].append(idx)
    ans = 0
    for word in words:
        ptr = -1
        isValid_sequence= True
        for ch in word:
            indices = char_indices[ch]
            i = bisect.bisect_right(indices, ptr)
            if i == len(indices):
                isValid_sequence = False
                break
            ptr = indices[i]
        if isValid_sequence:
            ans += 1
    return ans

print(numMatchingSubseq("abcde", ["a","bb","acd","ace"]))