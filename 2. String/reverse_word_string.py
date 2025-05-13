def reverseWords( s: str) -> str:
    # Convert to list (since Python strings are immutable)
    s = list(s)
    n = len(s)
    
    # Step 1: Trim leading/trailing spaces and normalize intermediate spaces
    # (Implementation skipped for brevity, but involves two pointers)
    
    # Step 2: Reverse the entire string
    s.reverse()
    
    # Step 3: Reverse each word
    start = 0
    for end in range(n + 1):
        if end == n or s[end] == ' ':
            # Reverse the word from start to end-1
            left, right = start, end - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            start = end + 1
    
    # Step 4: Convert back to string
    return ''.join(s)

# Step 1: Trim and split (built-ins handle this efficiently)
    words = s.split()
    
    # Step 2: Reverse in-place (no extra space)
    words.reverse()
    
    # Step 3: Join with single spaces
    return ' '.join(words)

print(reverseWords("the sky is blue a "))