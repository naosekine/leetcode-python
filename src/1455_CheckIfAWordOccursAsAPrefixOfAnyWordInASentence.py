class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        count = 1
        for word in sentence.split():
            if word[:len(searchWord)] == searchWord:
                return count
            count += 1
        return -1