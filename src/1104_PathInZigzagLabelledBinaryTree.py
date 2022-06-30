class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        n = 0
        while label >= 2 ** n:
            n += 1
        
        trueNum = label
        if n % 2 == 0:
            trueNum = 2**n - 1 + 2**(n-1) - label
        print(n, trueNum)
        
        ans = []
        while trueNum >= 1:
            ans.append(trueNum)
            trueNum //= 2
                
        ans.reverse()
        
        for i, num in enumerate(ans):
            if i % 2 != 0:
                ans[i] = 2 ** (i + 1) -1 + 2 ** i - num
        
        return ans
        