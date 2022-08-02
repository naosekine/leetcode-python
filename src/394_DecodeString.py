class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        s_list = []
        
        for ele in s:
            if ele.isdigit():
                if s_list and s_list[-1].isdigit():
                    s_list[-1] += ele
                else:
                    s_list.append(ele)
                    
            else:
                s_list.append(ele)
        print(s_list)
        
        ans = ''
        for ele in s_list:
            if ele.isdigit():
                stack.append(ele)
            elif ele.isalpha():
                # print(ele)
                if stack and stack[-1].isalpha():
                    stack[-1] += ele
                else:
                    stack.append(ele)
                    
            elif ele == ']':
                # print(stack)
                alp = stack.pop()
                num = stack.pop()
                dc_str=alp*int(num)
                if stack and stack[-1].isalpha():
                    stack[-1]+=dc_str
                else:
                    stack.append(dc_str)
        if stack:
            for ele in stack:
                ans += ele
        return ans