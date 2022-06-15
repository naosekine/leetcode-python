class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minnum = min(nums)
        maxnum = max(nums)
        gcd = 1
        for i in range(1,minnum + 1):
            if minnum % i == 0 and maxnum % i == 0:
                gcd = i
        return gcd
