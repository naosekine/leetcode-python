class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        ans = 0
        for s in columnTitle:
            tmp = ord(s)-ord('A')+1
            for _ in range(n-1):
                tmp *= 26
            ans += tmp
            n -= 1 
        return ans