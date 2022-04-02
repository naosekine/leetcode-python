class Solution:
    def removeElement(self, nums, val) -> int:
        cur_idx = 0
        for idx in range(len(nums)):
            if val != nums[idx]:
                nums[cur_idx] = nums[idx]
                cur_idx += 1
        return cur_idx
    
if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3,2,2,3], 3))
    print(s.removeElement([0,1,2,2,3,0,4,2], 2))