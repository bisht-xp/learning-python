# def findSubstring( s: str, words: list[str]) -> list[int]:
#     if not s and not words:
#         return []
    
#     word_len = len(words[0])
#     window_len = len(words)*word_len
#     word_freq = {}

#     result = []
#     for word in words:
#         word_freq[word] = 1 + word_freq.get(word, 0)
    
#     for i in range(len(s) - window_len + 1):
#         substr_freq = {}
#         j = i

#         while j < i + window_len:
#             curr_word = s[j: j+word_len]

#             if curr_word not in word_freq:
#                 break
            
#             substr_freq[curr_word] = 1+substr_freq.get(curr_word, 0)

#             if word_freq[curr_word] < substr_freq[curr_word]:
#                 break

#             j += word_len
        
#         if j == i + window_len:
#             result.append(i)
        
    
#     return result

from collections import defaultdict

def findSubstring( s: str, words: list[str]) -> list[int]:
    if not s or not words:
        return []

    word_freq = {}

    for word in words:
        word_freq[word] = 1 + word_freq.get(word, 0)

    word_len = len(words[0]) 
    word_count = len(words)

    result = []

    for i in range(word_len):
        left = i
        substr_freq = {}
        count = 0

        for j in range(i, len(s)- word_len + 1, word_len):
                curr_word = s[j:j+word_len]

                if curr_word in word_freq:
                    substr_freq[curr_word] = 1 + substr_freq.get(curr_word, 0)
                    count += 1

                    while substr_freq[curr_word] > word_freq[curr_word]:
                        left_word = s[left: left+word_len]
                        substr_freq[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    if count == word_count:
                        result.append(left)
                else:
                   count = 0
                   substr_freq.clear()
                   left = j+word_len
        

    return result


print(findSubstring("barfootheafoobarman", ["foo","bar"]))


                


        
        
        
        


