class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(adjList, visited, startNode):
            
            visited[startNode] = 1
            for i in range(len(adjList[startNode])):
                if visited[adjList[startNode][i]] == 0:
                    dfs(adjList, visited, adjList[startNode][i])
                    
        components = 0
        visited = [0] * n
        adjList = [[] for _ in range(n)]
        print(adjList)
        
        for i in range(len(edges)):
            adjList[edges[i][0]].append(edges[i][1])
            adjList[edges[i][1]].append(edges[i][0])
        print(adjList)
        print(visited)
        for i in range(n):
            print(visited)
            if visited[i] == 0:
                components += 1
                dfs(adjList, visited, i)
        
        return components