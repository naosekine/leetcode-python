class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}', '[':']'}
        stack = []
        for ele in s:
            if ele in brackets:
                stack.append(ele)
            else:
                if len(stack) == 0 or brackets[stack.pop()] != ele:
                    return False
        return len(stack) == 0
        
if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()"))