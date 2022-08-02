class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ele in s:
            if stack and stack[-1][0] == ele:
                stack[-1][1] += 1
            else:
                stack.append([ele, 1])
            if stack[-1][1] == k:
                stack.pop()
        
        ans = ''
        for alp, i in stack:
            ans += alp*i
        return ans