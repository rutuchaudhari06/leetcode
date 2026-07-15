class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        vis=[-1]*n
        t=0
        for start in range(n):
            if vis[start] != -1:
                continue
            q=deque([start])
            vis[start]=t

            while q:
                node=q.popleft()
                for it in graph[node]:
                    if vis[it]==-1:
                        q.append(it)
                        vis[it]=1-vis[node]
                    elif vis[node]==vis[it]:
                        return False
        return True


