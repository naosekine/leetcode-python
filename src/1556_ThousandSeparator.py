class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = list(str(n))[::-1]
        for i in range(len(res)):
            if i % 3 == 0 and i != 0:
                res[i] = res[i] + '.'
        
        return ''.join(res[::-1])