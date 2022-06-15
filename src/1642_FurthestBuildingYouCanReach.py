import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_allocations = []
        
        for i in range(len(heights)-1):
            climb = heights[i+1] - heights[i]
            if climb <= 0:
                continue
            
            heapq.heappush(ladder_allocations, climb)
            
            if len(ladder_allocations) <= ladders:
                continue
            
            bricks -= heapq.heappop(ladder_allocations)
            
            if bricks < 0:
                return i
            
        return len(heights) - 1

# help-self solution
#         used_ladders = []
#         ans = 0
#         for i in range(1, len(heights)):
#             ans += 1
#             if heights[i-1] < heights[i]:
#                 # print(used_ladders)
#                 if ladders > 0:
#                     ladders -= 1
#                     heapq.heappush(used_ladders, heights[i] - heights[i-1])
#                 else:
#                     if bricks > 0 and len(used_ladders) > 0:
#                         min_used_ladder = heapq.heappop(used_ladders)
#                         if min_used_ladder < heights[i] - heights[i-1] and bricks >= min_used_ladder:
#                             heapq.heappush(used_ladders, heights[i] - heights[i-1])
#                             bricks -= min_used_ladder
#                         elif min_used_ladder >= heights[i] - heights[i-1] and bricks >= heights[i] - heights[i-1]:
#                             heapq.heappush(used_ladders, min_used_ladder)
#                             bricks -= heights[i] - heights[i-1]
#                         else:
#                             ans -= 1
#                             break
#                     elif bricks > 0 and len(used_ladders) == 0:
#                         if bricks >= heights[i] - heights[i-1]:
#                             bricks -= heights[i] - heights[i-1]
#                         else:
#                             ans -= 1
#                             break
#                     else:
#                         ans -= 1
#                         break

#         return ans
        