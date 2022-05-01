# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    # dummy
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        top = n
        bottom = 1
        while top >= bottom:
            mid = (top + bottom) // 2
            if not isBadVersion(mid-1) and isBadVersion(mid):
                return mid
            
            if isBadVersion(mid) and isBadVersion(mid):
                top = mid-1
            else:
                bottom = mid+1