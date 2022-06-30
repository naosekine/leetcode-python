import heapq
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        canEatApples = []
        ans = 0
        i = 0
        while i < len(apples) or canEatApples:
            if i < len(apples):
                heapq.heappush(canEatApples, [i + days[i], apples[i]])
            
            while canEatApples and (canEatApples[0][0] <= i or canEatApples[0][1] == 0):
                heapq.heappop(canEatApples)
            
            if canEatApples:
                if canEatApples[0][1] > 1:
                    canEatApples[0][1] -= 1
                else:
                    heapq.heappop(canEatApples)
                ans += 1
            i += 1
            
        return ans