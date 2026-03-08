def largestRectangleArea(heights: list[int]) -> int:
    max_area = 0
    stack = []

    for i in range(len(heights)):
        index = i
        while stack and stack[-1][1] > heights[i]:
            max_area = max(max_area, stack[-1][1]*(i-stack[-1][0]))
            value = stack.pop()
            index = value[0]

        stack.append([index, heights[i]])
    
    while stack:
        max_area = max(max_area, stack[-1][1] * (len(heights) - stack[-1][0]))
        stack.pop()
    
    return max_area

        
heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))