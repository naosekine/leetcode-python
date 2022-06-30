class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        upper = 0
        lower = len(s)-1
        
        while upper < lower:
            s[upper], s[lower] = s[lower], s[upper]
            upper += 1
            lower -= 1
        