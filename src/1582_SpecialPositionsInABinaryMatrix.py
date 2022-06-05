class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                flag = False
                if mat[i][j] == 1:
                    if mat[i].count(1) == 1:
                        flag = True                 
                        for l in range(len(mat)):
                            if l != i:
                                if mat[l][j] == 1:
                                    flag = False
                        if flag:
                            count += 1
        return count
                                