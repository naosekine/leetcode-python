class Solution:
    def search(self, nums, target: int) -> int:
        n = len(nums)
        max_n = n
        min_n = 0
        while max_n > min_n:
            mid =  (max_n + min_n) // 2
            if nums[mid] < target:
                min_n = mid+1
            elif nums[mid] > target:
                max_n = mid
            else:
                return mid
        return -1