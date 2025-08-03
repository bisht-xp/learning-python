def longestValidParentheses(s: str) -> int:
    stack=[]
    stack.append(-1)

    maxLen = 0

    for i,ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) <= 0:
                stack.append(i)
            else:
                maxLen = max(maxLen, i - stack[-1])

    return maxLen

print(longestValidParentheses("((()))())"))