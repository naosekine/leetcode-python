class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        ans = []
        tmp = []
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                print(tmp)
                if len(tmp) < c:
                    tmp.append(mat[x][y])
                elif len(tmp) == c:
                    ans.append(tmp)
                    tmp = []
                    if 0<=x<=len(mat) and 0<=y<=len(mat[0]):
                        tmp.append(mat[x][y])
        ans.append(tmp)
        return ans