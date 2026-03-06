def dailyTemperatures(temperatures: list[int]) -> list[int]:
    result = [0]*len(temperatures)
    stack = []
    for i in range(len(temperatures)):
        while stack and temperatures[i] > stack[-1][0]:
            hotest_day = i - stack[-1][1]
            result[stack[-1][1]] = hotest_day
            stack.pop()
        
        stack.append((temperatures[i], i))
    
    return result

temperatures = [30,38,30,36,35,40,28]
print(dailyTemperatures(temperatures))
