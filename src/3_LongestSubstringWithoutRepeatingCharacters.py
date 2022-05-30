class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        visited = {}
        i = j = 0
        while i < len(s) and j < len(s):
            if not visited.get(s[j]):
                visited[s[j]] = True
                maxLen = max(maxLen, j-i+1)
                j += 1
            else:
                visited[s[i]] = False
                i += 1
        return maxLen