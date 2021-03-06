from collections import defaultdict
class HitCounter:

    def __init__(self):
        self.kiroku = defaultdict(int)

    def hit(self, timestamp: int) -> None:
        self.kiroku[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        start = 1
        if timestamp - 299 > 0:
            start = timestamp - 299
        hits = 0
        for i in range(start, timestamp+1):
            hits += self.kiroku[i]
        return hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)