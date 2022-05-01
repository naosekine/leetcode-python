class Solution:
    def minSubsequence(self, nums):
        if len(nums) == 1:
            return nums
        nums.sort(reverse=True)
        for i in range(1, len(nums)):
            front = nums[:i]
            back = nums[i:]
            print(front, back)
            if sum(front) > sum(back):
                return front
        return nums