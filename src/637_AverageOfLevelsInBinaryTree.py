# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.ans = []
        self.memo = []
        def dfs(root, n = 0):
            if root:
                print(self.ans)
                if len(self.ans) < n+1:
                    self.ans.append(root.val)
                    self.memo.append(1)
                else:
                    self.ans[n] += root.val
                    self.memo[n] += 1
                bfs(root.left, n+1)
                bfs(root.right, n+1)
        
        bfs(root)
        print(self.ans)
        print(self.memo)
        result = []
        for a, m in zip(self.ans, self.memo):
            result.append(a/m)
        return result