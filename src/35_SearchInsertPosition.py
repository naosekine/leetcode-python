def searchInsert(self, nums, target: int) -> int:
    top = len(nums)
    bottom = 0
    
    while top >= bottom:
        mid = (top + bottom)//2
        if mid >= len(nums):
            return len(nums)
        if nums[mid] == target:
            return mid
        
        if nums[mid] > target and nums[mid-1] < target:
            return mid
        elif nums[mid] > target:
            top = mid-1
        else:
            bottom = mid+1
    return 0