# def longestPalindrome(s: str) -> str:
#     ans = [0, 0]
    
#     for i in range(len(s)):
#         l,r=i,i

#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             if((r-l+1) > ans[1]):
#                 ans[0] = l
#                 ans[1] = r-l+1
            
#             l -= 1
#             r += 1
        
#         l,r=i,i+1
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             if (r-l+1) > ans[1]:
#                 ans[0] = l
#                 ans[1] = r-l+1
            
#             l -= 1
#             r += 1
        
#     return s[ans[0]: ans[0] + ans[1]]

def longestPalindrome(s: str) -> str:
    
    def check(i, j):
        left = i
        right = j - 1

        print(left,right)

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True


    for length in range(len(s),0,-1):
        print("length: ", length)
        for start in range(len(s)-length+1):
            print("start: ", start)
            if(check(start,start +length)):
                return s[start: start+length]                
    
    return ""

print(longestPalindrome("babad"))