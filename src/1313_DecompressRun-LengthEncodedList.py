class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans=[]
        a = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                a = nums[i]
            else:
                for _ in range(a):
                    ans.append(nums[i])
            print(a)
        return ans