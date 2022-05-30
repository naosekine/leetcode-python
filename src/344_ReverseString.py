class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        mid = len(s)//2
        n = len(s)-1
        for i in range(mid):
            memo = s[i]
            s[i] = s[n-i]
            s[n-i] = memo
