class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph=[[] for _ in range(n)]
        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))

        dist=[float('inf')]*n
        dist[0]=0

        ways=[0]*n
        ways[0]=1

        pq=[]
        heapq.heappush(pq,(0,0))
        MOD = 10**9 + 7

        while pq:
            time,node=heapq.heappop(pq)
            if time > dist[node]:
                continue
            
            for v,w in graph[node]:
                if w+time<dist[v]:
                    dist[v]=w+time
                    ways[v]=ways[node]
                    heapq.heappush(pq,(dist[v],v))
                elif w+time==dist[v]:
                    ways[v]=(ways[node]+ways[v])%MOD

        return ways[n-1]%MOD
        