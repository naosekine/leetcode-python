from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_S = Counter(s)
        counter_T = Counter(t)
        return counter_S == counter_T