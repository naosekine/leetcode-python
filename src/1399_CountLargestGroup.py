class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic = {}
        for i in range(1, n+1):
            total = 0
            for s in str(i):
                total += int(s)
            if total in dic:
                dic[total] += 1
            else:
                dic[total] = 1
        return list(dic.values()).count(max(dic.values()))