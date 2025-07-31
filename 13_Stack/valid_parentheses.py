# def isValid(s: str) -> bool:
    # if(len(s) < 2):
    #     return False
    
    # character_stack = []

    # for ch in s:
    #     if ch == ')' and len(character_stack) > 0:
    #         pop_val = character_stack.pop()
    #         if(pop_val != "("):
    #             return False
    #     elif ch == '}' and len(character_stack) > 0:
    #         pop_val = character_stack.pop()
    #         if(pop_val != '{'):
    #             return False
        
    #     elif ch == ']' and len(character_stack) > 0:
    #         pop_val = character_stack.pop()
    #         if(pop_val !=  "["):
    #             return False
    #     else:
    #         character_stack.append(ch)
            

    # return len(character_stack) == 0


def isValid(s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)

    return not stack
print(isValid("(({}))"))