    # max_len=0
    # i=0
    # max_char_freq=0
    # char_count = [0]*26
    # for j,char in enumerate(s):
    #     char_count[ord(char) - ord('A')] += 1 

    #     max_char_freq = max(max_char_freq, char_count[char])

    #     if j-i+1 - max_char_freq > k:
    #         while  j-i+1 - max_char_freq > k:
    #             char_count[s[i]] -= 1
    #             max_char_freq = 0
    #             for val in char_count:
    #                 max_char_freq=max(max_char_freq, val)
    #             i += 1 

    #     max_len = max(max_len, j-i+1)
        

    # return max_len
#binary search opproch with sliding window
# def can_make_valid_substring(s,sub_len,k):
#     char_freq={}
#     max_freq=0
#     start=0
#     for end in range(len(s)):
#         char_freq[s[end]] = char_freq.get(s[end], 0) + 1

#         if end+1-start > sub_len:
#             char_freq[s[start]] -= 1
#             start += 1
        
#         max_freq = max(max_freq, char_freq[s[end]])
#         if sub_len - max_freq <= k:
#             return True
     
#     return False

# def characterReplacement( s: str, k: int) -> int:
#     lo,hi=0,len(s)+1

#     while lo+1 < hi:
#         mid = (lo+hi)//2
#         if can_make_valid_substring(s,mid,k):
#             lo  = mid
#         else:
#             hi = mid

#     return lo     

# def is_window_valid(start, end, count, k):

#     return end + 1 - start - count  <= k

# def characterReplacement( s: str, k: int) -> int:
#     all_letter = set(s)
#     max_len = 0

#     for letter in all_letter:
#         start = 0
#         count = 0

#         for end,char in enumerate(s):
#             if char == letter:
#                 count += 1
            
#             while not is_window_valid(start,end,count, k):
#                 if s[start] == letter:
#                     count -= 1
                
#                 start += 1
        
#             max_len = max(max_len, end+1-start)
    
#     return max_len

def characterReplacement( s: str, k: int) -> int:
    start,end=0,0
    freq_map={}
    max_len=0
    max_freq=0

    for end,char in enumerate(s):
        freq_map[char] = freq_map.get(char, 0) + 1
        max_freq = max(max_freq, freq_map[char])

        is_valid = (end + 1 - start - max_freq <= k)
        if not is_valid:
            freq_map[s[start]] -= 1
            start += 1
        
        max_len = end+1-start
    
    return max_len

print(characterReplacement("AABBCCBC", 1))