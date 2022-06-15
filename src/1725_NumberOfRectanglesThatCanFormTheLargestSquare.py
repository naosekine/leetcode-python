class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        dic = defaultdict(int)
        for r, c in rectangles:
            i = min(r, c)
            dic[i] += 1
        return dic[max(dic.keys())]