class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        front = nums[:-k]
        back = nums[-k:]
        n = len(front)
        m = len(back)
        for i in range(m):
            nums[i]  = back[i]
        for i in range(n):
            nums[i+m] = front[i]