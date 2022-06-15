class Solution(object):
    def numMatchingSubseq(self, S, words):
        ans = 0
        heads = [[] for _ in range(26)]
        
        for word in words:
            it = iter(word)
            heads[ord(next(it)) - ord('a')].append(it)
        
        for letter in S:
            letter_idx = ord(letter) - ord('a')
            old_buckets = heads[letter_idx]
            heads[letter_idx] = []
            
            while old_buckets:
                it = old_buckets.pop()
                nxt = next(it, None)
                if nxt:
                    heads[ord(nxt) - ord('a')].append(it)
                    print(type(nxt))
                else:
                    ans += 1
        return ans
            
