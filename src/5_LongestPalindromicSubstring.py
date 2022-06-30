class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def searchPalindromic(start, end):
            while 0 <= start and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
                print(s[start+1:end],s[start], s[end])
            return s[start+1:end]
        
        max_palindronic = ''
        for i in range(len(s)):
            # odd case
            tmp = searchPalindromic(i-1, i+1)
            if len(tmp) > len(max_palindronic):
                max_palindronic = tmp

            # even case
            tmp = searchPalindromic(i, i+1)
            if len(tmp) > len(max_palindronic):
                max_palindronic = tmp
        
        return max_palindronic
        
#         if len(s) == 1:
#             return s
#         if len(s) == 2:
#             if s[0] == s[1]:
#                 return s
#             else:
#                 return s[0]
        
#         two_small_palindromics_idx = []
#         for i in range(len(s)-1):
#             if s[i] == s[i+1]:
#                 two_small_palindromics_idx.append(i)
                
#         three_small_palindromics_idx = []
#         for i in range(1, len(s)-1):
#             if s[i-1] == s[i+1]:
#                 three_small_palindromics_idx.append(i)
#         print(two_small_palindromics_idx)
#         print(three_small_palindromics_idx)
        
#         max_len = 0
#         max_idx = None
        
#         # Two search
#         for i in two_small_palindromics_idx:
#             length = 0
#             left = i
#             right = i+1
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 length += 2
#                 left -= 1
#                 right += 1
#             max_len = max(max_len, length)
#             if length == max_len:
#                 max_idx = left+1
                
#         # Three search
#         for i in three_small_palindromics_idx:
#             length = 1
#             left = i-1
#             right = i+1
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 length += 2
#                 left -= 1
#                 right += 1
#             max_len = max(max_len, length)
#             if length == max_len:
#                 max_idx = left+1

#         if max_idx is not None:
#             return s[max_idx:max_idx+max_len]
#         else:
#             return s[0]