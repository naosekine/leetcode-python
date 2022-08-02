from collections import defaultdict
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = wordsDict
        self.memo = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.memo[word].append(i)
            
    def shortest(self, word1: str, word2: str) -> int:
        ans = math.inf
        for i in self.memo[word1]:
            for j in self.memo[word2]:
                ans = min(ans, abs(i-j))
        return ans
                                
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)