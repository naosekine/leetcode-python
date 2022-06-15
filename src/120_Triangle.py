class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(1, len(triangle)):
            for col in range(len(triangle[row])):
                if 0 < col < row:
                    triangle[row][col] += min(triangle[row-1][col], triangle[row-1][col-1])
                elif col == 0:
                    triangle[row][col] += triangle[row-1][col]
                else:
                    triangle[row][col] += triangle[row-1][col-1]
        return min(triangle[-1])
        
        # another solution (self-help)
        # dp = [triangle[0]]
        # for i in range(1, len(triangle)):
        #     tmp = []
        #     for j, ele in enumerate(triangle[i]):
        #         if j != 0 and j != len(triangle[i])-1:
        #             tmp.append(ele + min(dp[i-1][j-1], dp[i-1][j]))
        #         elif j == 0:
        #             tmp.append(ele + dp[i-1][j])
        #         else:
        #             tmp.append(ele + dp[i-1][j-1])
        #     dp.append(tmp)
        # return min(dp[-1])                     