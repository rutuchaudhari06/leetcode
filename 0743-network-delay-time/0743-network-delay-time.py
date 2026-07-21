class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=[[] for _ in range(n+1)]

        for u,v,w in times:
            graph[u].append((v,w))
        
        if not graph[k]:
            return -1
        
        dist=[float('inf')]*(n+1)
        dist[k]=0
        pq=[]
        heapq.heappush(pq,(0,k))
        while pq:
            time,node=heapq.heappop(pq)
            
            for v,t in graph[node]:
                if dist[v]>t+time:
                    dist[v]=t+time
                    heapq.heappush(pq,(dist[v],v))
        
        ans = 0

        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                return -1
            ans = max(ans, dist[i])

        return ans
