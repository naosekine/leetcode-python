class Solution:
    def reverseWords(self, s: str) -> str:
        list_s = s.split()
        reverse_s = []
        for word in list_s:
            list_word = list(word)
            l, r = 0, len(list_word) - 1
            while l < r:
                list_word[l], list_word[r] = list_word[r], list_word[l]
                l += 1
                r -= 1
            reverse_s.append(''.join(list_word))
            
        return ' '.join(reverse_s)