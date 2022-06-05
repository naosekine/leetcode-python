class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x_toplow = min(max(rec1[0], rec1[2]), max(rec2[0], rec2[2]))
        x_bottomhigh = max(min(rec1[0], rec1[2]), min(rec2[0], rec2[2]))
        if x_bottomhigh >= x_toplow:
            return False
        
        y_toplow = min(max(rec1[1], rec1[3]), max(rec2[1], rec2[3]))
        y_bottomhigh = max(min(rec1[1], rec1[3]), min(rec2[1], rec2[3]))
        if y_bottomhigh >= y_toplow:
            return False
        
        return True