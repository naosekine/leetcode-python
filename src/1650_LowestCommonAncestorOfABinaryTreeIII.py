"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

from collections import deque
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_parents = deque()
        q_parents = deque()
        while p is not None:
            p_parents.append(p)
            p = p.parent
        while q is not None:
            q_parents.append(q)
            q = q.parent
        
        p_node = p_parents.pop()  
        q_node = q_parents.pop()
        last_pq = p_node
        while p_node == q_node and p_parents and q_parents:
            last_pq = p_node
            p_node = p_parents.pop()  
            q_node = q_parents.pop()
        
        if p_node == q_node and (not p_parents or not q_parents):
            return p_node
        else:
            return last_pq
            