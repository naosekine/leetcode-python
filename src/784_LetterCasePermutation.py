class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [[]]
        
        for cha in s:
            n = len(ans)
            if cha.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(cha.upper())
                    ans[n+i].append(cha.lower())
                    
            else:
                for i in range(n):
                    ans[i].append(cha)
        return [''.join(a) for a in ans]