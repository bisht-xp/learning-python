def isPalindrome(s: str) -> bool:
        st = "".join(s.split()).lower()
        l,r=0,len(st)-1

        while l < len(st) and not st[l].isalnum():
            l += 1

        while r >= 0 and not st[r].isalnum():
            r -= 1
        

        while l <= r and st[l] == st[r]:
            l += 1
            r -= 1
            while l < len(st) and not st[l].isalnum():
                l += 1

            while r >= 0 and not st[r].isalnum():
                r -= 1
        
        return True if l > r else False

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))