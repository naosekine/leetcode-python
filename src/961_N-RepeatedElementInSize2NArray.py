class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        
        for num in nums:
            m = nums.count(num)
            if n == m:
                return num