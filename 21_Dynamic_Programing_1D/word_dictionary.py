# memoization
# def wordBreak( s: str, wordDict: list[str]) -> bool:
    # memo = [False]*len(s)
    
    # def is_valid(st):
    #     for word in wordDict:
    #         if word == st:
    #             return True
    #     return False


    # def dfs(i):
    #     if i >= len(s):
    #         return True
        
    #     if(i in memo):
    #         return memo[i]
        
    #     for j in range(i,len(s)):
    #         new_str = s[i: j+1]
    #         remaining_word = False
    #         if is_valid(new_str):
    #             memo[j] = dfs(j+1)
    #             return memo[j]
    #         memo[j] = remaining_word
        
    #     return False
    
    # return dfs(0)

# other bottom up approch:
def wordBreak( s: str, wordDict: list[str]) -> bool:
    def dfs(i):
        if i >= len(s):
            return True
        
        for word in wordDict:
            if s[i: i+len(word)] == word and dfs(i+len(word)):
                return True
        
        return False
    return dfs(0)

def wordBreak2( s: str, wordDict: list[str]) -> bool:
    dp = [False]*(len(s)+1)
    dp[0] = True
    for i in range(1,len(s)+1):
        for word in wordDict:
            word_len = len(word)
            if i >= word_len:
                if s[i-word_len: i] == word and dp[i-word_len]:
                    dp[i] = True
                    break
    
    return dp[len(s)]




# Bottom-up Approch
# def wordBreak( s: str, wordDict: list[str]) -> bool:
#     dp = [False]*(len(s)+1)
#     dp[0] = True
    
#     words = set(wordDict)

#     for i in range(1,len(s)+1):
#         for j in range(i):
#             curr_str = s[j:i]
#             if dp[j] and curr_str in words:
#                 dp[i] = True
#                 break
    
#     return dp[len(s)]
        

s = "leetcode"
wordDict = ["leet","code"]

print(wordBreak(s,wordDict))