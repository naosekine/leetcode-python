class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        n = len(mat2)
        answer = []
        for i in range(m):
            t = []
            for r in range(len(mat2[0])):
                tmp = 0
                for j in range(len(mat1[0])):
                    tmp += mat1[i][j] * mat2[j][r]
                t.append(tmp)
            answer.append(t)
        return answer