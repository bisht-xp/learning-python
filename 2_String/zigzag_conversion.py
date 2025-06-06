def convert(s: str, numRows: int) -> str:
    n = len(s)
    ans_str = [""]*numRows

    i = 0
    while i < n:
        j=0
        while i < n and j < numRows:
            ans_str[j] += s[i]
            i += 1
            j += 1

        j = numRows-2

        while i < n and j > 0:
            ans_str[j] += s[i]
            i+= 1
            j -= 1
        
    
    ans = ""
    for st in ans_str:
        ans += st

    return ans


print(convert( s = "A", numRows = 4))
          