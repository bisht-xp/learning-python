def largestRectangleArea(heights: list[int]) -> int:
    stack = []
    stack.append(-1)
    max_area = -1

    for i in range(len(heights)):
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            current_height = heights[stack.pop()]
            current_width = i - stack[-1] - 1
            max_area = max(max_area, current_height*current_width)
        
        stack.append(i)
    
    while stack[-1] != -1:
        current_height = heights[stack.pop()]
        current_width = len(heights) - stack[-1] - 1
        max_area = max(max_area, current_height*current_width)
    
    return max_area


print(largestRectangleArea([2,1,5,6,2,3]))