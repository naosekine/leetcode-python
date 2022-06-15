class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a':True, 'i':True,'u':True,'e':True, 'o':True}
        start = 0
        end = k-1
        max_count = 0
        for i in range(k):
            if s[i] in vowels:
                max_count += 1
        curr = max_count
        while end < len(s)-1:
            if s[start] in vowels:
                curr -= 1
            start += 1
            end += 1
            if s[end] in vowels:
                curr += 1
            max_count = max(max_count, curr)
        
        return max_count
