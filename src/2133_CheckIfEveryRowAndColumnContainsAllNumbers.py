from collections import Counter
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:

        numsCounter = Counter(list(range(1, len(matrix)+1))) 
        
        for r in range(len(matrix)):
            r_list = []
            for c in range(len(matrix)):
                r_list.append(matrix[r][c])
            if numsCounter != Counter(r_list):
                return False
            
        for c in range(len(matrix)):
            c_list = [matrix[r][c] for r in range(len(matrix))]
            if numsCounter != Counter(c_list):
                return False
                
        return True