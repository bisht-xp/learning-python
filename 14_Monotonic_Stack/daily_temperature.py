def dailyTemperatures( temperatures: list[int]) -> list[int]:
    n = len(temperatures)

    result = [0]*n
    stack = []

    for i in range(n):
        while len(stack) and temperatures[i] > temperatures[stack[-1]]:
            val = stack.pop()
            result[val] = i-val
        
        stack.append(i)
    
    return result



print(dailyTemperatures([73,74,75,71,69,72,76,73]))
            
