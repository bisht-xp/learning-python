def letterCombinations( digits: str) -> list[str]:
    my_dict = {"2": "abc", "3": "def", '4': "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result = []
    def helper(i, cur_str):
        if len(cur_str) == len(digits):
            result.append(cur_str)
            return
        
        for ch in my_dict[digits[i]]:
            helper(i+1, cur_str + ch)
        
    helper(0, "")
    return result


print(letterCombinations("23"))

        