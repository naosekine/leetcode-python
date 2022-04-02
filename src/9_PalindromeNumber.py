class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = list(str(x))
        N = len(str_x)
        
        idx = 0
        while idx+1 <= N//2:
            if str_x[idx] != str_x.pop():
                return False
            idx += 1
        
        return True
    
if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))