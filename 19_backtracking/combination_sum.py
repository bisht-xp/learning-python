def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    combination = []

    def helper(i, candiates, target, sum, comb):
        if sum[0] == target:
            combination.append(comb.copy())
            return
        
        if i >= len(candiates) or sum[0] > target:
            return
        
        comb.append(candiates[i])
        sum[0] += candidates[i]
        helper(i, candiates, target, sum, comb)
        sum[0] -= comb.pop()

        helper(i+1, candiates, target, sum, comb)

    helper(0,candidates, target, [0], [])
    return combination


print(combinationSum([8,7,4,3], 11))