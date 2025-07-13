def maxScoreSightseeingPair( values: list[int]) -> int:
    max_spot = float('-inf')
    max_so_far = values[0]+0

    for j in range(1,len(values)):
        result = max_so_far + values[j]-j
        if max_spot < result:
            max_spot = result

        max_so_far = max(max_so_far, values[j] + j)

    return max_spot

print(maxScoreSightseeingPair([8,1,2,6,7]))