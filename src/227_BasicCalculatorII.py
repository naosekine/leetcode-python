from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        l = list(s.replace(' ', ''))        
        stack = []
        divi_ope = None
        res = None
        for i, ele in enumerate(l):
            if ele.isdigit():
                if res is not None:
                    res = res*10 + int(ele)
                else:
                    res = int(ele)
            if i == len(l)-1 or not ele.isdigit():
                if divi_ope == '*' or divi_ope == '/':
                        last_num = stack.pop()
                        if divi_ope == '*':
                            stack.append(last_num * res)
                        elif divi_ope == '/':
                            stack.append(int(last_num / res))
                elif divi_ope == '+':
                    stack.append(res)
                elif divi_ope == '-':
                    stack.append(res * (-1))
                else:
                    stack.append(res)
                res = None
                divi_ope = ele
        
        ans = 0
        while stack:
            ans += stack.pop()
        
        return ans
            
                