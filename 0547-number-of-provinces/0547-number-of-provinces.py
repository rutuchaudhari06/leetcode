class Solution:
    def dfs(self, graph, node, vis):
        vis[node] = 1

        for i in range(len(graph)):
            if graph[node][i] == 1 and not vis[i]:
                self.dfs(graph, i, vis)
        

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        vis=[0]*len(isConnected)
        cnt=0
        for i in range(len(vis)):
            if not vis[i]:
                cnt += 1
                self.dfs(isConnected, i, vis)
        return cnt