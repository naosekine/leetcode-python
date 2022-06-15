class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        def remove_point(a, b):
            points.discard((a, b))
            for bi in points_x[a]:
                if (a, bi) in points:
                    remove_point(a, bi)
            for ai in points_y[b]:
                if (ai, b) in points:
                    remove_point(ai, b)
            
        points = set()
        points_x = defaultdict(list)
        points_y = defaultdict(list)

        for a, b in stones:
            points.add((a,b))
            points_x[a].append(b)
            points_y[b].append(a)
        cnt = 0
        for a, b in stones:
            if (a, b) in points:
                remove_point(a, b)
                cnt += 1
        
        return len(stones) - cnt