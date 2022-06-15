class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combies = []
        def backtrack(first = 1, curr = []):            
            if len(curr) == k:
                combies.append(curr[:])
                
            for i in range(first, n + 1):
                curr.append(i) 
                backtrack(i+1, curr) 
                curr.pop()
        backtrack()
        return combies
            