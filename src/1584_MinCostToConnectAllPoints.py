class UnionFind:
    def __init__(self, size: int):
        self.group = [0] * size
        self.rank = [0] * size
        
        for i in range(size):
            self.group[i] = i
        
    def find(self, node):
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]
    
    def join(self, node1, node2):        
        group1 = self.find(node1)
        group2 = self.find(node2)
        
        if group1 == group2:
            return False
        
        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1
            
        return True
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        all_edges = []
        n = len(points)
        
        for currnode in range(n):
            for nextnode in range(currnode + 1,  n):
                edge_weight = abs(points[currnode][0] - points[nextnode][0]) + abs(points[currnode][1]-points[nextnode][1])
                all_edges.append((edge_weight, currnode, nextnode))
        
        all_edges.sort()
                    
        uf = UnionFind(n)
        mst_cost = 0
        edges_used = 0
        
        for weight, node1, node2 in all_edges:
            if uf.join(node1, node2):
                mst_cost += weight
                edges_used += 1
                if edges_used == n-1:
                    break
        
        return mst_cost
