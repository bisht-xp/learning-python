# def canJump(nums: list[int]) -> bool:
#     goal = len(nums)-1
    
#     for i in range(len(nums)-1,-1,-1):
#         if i + nums[i] >= goal:
#             goal = i

#     return True if goal == 0 else False


#dp

def canJump(nums: list[int]) -> bool:
    def dfs(i):
        if i >= len(nums)-1:
            return True
        
        max_jump = nums[i]
        for j in range(1,max_jump+1):
            if  dfs(i+j):
                return True
        
        return False

    return dfs(0)
        

nums = [2,3,1,1,4]
print(canJump(nums))           
                # [2,3,1,1,4]
            