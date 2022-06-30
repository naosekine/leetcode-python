class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''
        for b in s:
            if b.isalpha():
                a += b.lower()
            elif b.isdigit():
                a += b
        left = 0
        right = len(a)-1
        while left < right:
            if a[left] != a[right]:
                return False
            left += 1
            right -= 1
        return True