class Solution:
    def minOperations(self, logs) -> int:
        count = 0
        dic = {"../": -1, "./":0}
        for log in logs:
            if log in dic:
                if count > 0:
                    count += dic[log]
            else:
                count += 1
        if count > 0:
            return count
        else:
            return 0