class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        bottom_max = 0
        bottom = len(heights)-1
        ans = []
        while 0 <= bottom:
            if heights[bottom] > bottom_max:
                ans.append(bottom)
            bottom_max = max(bottom_max, heights[bottom])
            bottom -= 1
            
        return ans[::-1]