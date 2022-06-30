class Solution:
    def reformat(self, s: str) -> str:
        if len(s) == 1:
            return s
        alp = []
        inte = []
        for ele in s:
            if ele.isdigit():
                inte.append(ele)
            else:
                alp.append(ele)
        if not alp or not inte:
            return ''

        ans = ''
        print(alp, inte)
        if len(alp) == len(inte):
            while alp and inte:
                ans += alp.pop() + inte.pop()            
        elif len(alp) == len(inte) -1:
            while alp and inte:
                ans += inte.pop() + alp.pop()
            if inte:
                ans += inte.pop()
        elif len(alp)-1 == len(inte):
            while alp and inte:
                ans += alp.pop() + inte.pop()
            if alp:
                ans += alp.pop()
        return ans