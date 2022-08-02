class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
    
        dp1 = [0] * (len(nums)-1)
        dp2 = [0] * (len(nums)-1)
        first_flag = False
        for i in range(len(nums)-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+ nums[i])
        for i in range(1, len(nums)):
            dp2[i-1] = max(dp2[i-2], dp2[i-3]+ nums[i])
        
        max1 = max(dp1)
        max2 = max(dp2)
        
        return max(max1, max2)