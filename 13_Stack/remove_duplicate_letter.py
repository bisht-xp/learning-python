def removeDuplicateLetters(s: str) -> str:
    freq = dict()
    seen = dict()
    stack = []

    for ch in s:
        freq[ch] = freq.get(ch, 0)+1
    
    for i,ch in enumerate(s):
        if stack:
            while stack and freq[stack[-1]] > 0 and ch not in seen and stack[-1] > ch:
                val = stack.pop()
                seen.pop(val)

        if ch not in seen:
            stack.append(ch)
            seen[ch] = True
            freq[ch] = freq.get(ch) - 1

    return ''.join(stack)
    


print(removeDuplicateLetters("abacb"))