class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nokori = nums,curr =[]):
            if len(curr) == len(nums):
                permutations.append(curr[:])
            
            for i in range(len(nokori)):
                curr.append(nokori[i])
                tmp = nokori[:]
                tmp.pop(i)
                backtrack(tmp, curr)
                
                curr.pop()
        permutations = []
        backtrack()
        return permutations
