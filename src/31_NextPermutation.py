import heapq
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        target_idx = len(nums)
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                target_idx = i-1
                break
        if target_idx == len(nums):
            nums.sort()
            return
        
        trade_idx = len(nums)-1
        for i in range(target_idx+1, len(nums)):
            if nums[target_idx] >= nums[i]:
                trade_idx = i-1
                break
        print(target_idx, trade_idx)
        
        nums[target_idx], nums[trade_idx] = nums[trade_idx], nums[target_idx]
        nums[target_idx+1:] = sorted(nums[target_idx+1:])