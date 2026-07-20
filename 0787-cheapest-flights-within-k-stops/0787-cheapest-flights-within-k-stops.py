class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph=[[] for _ in range(n)]
        for s,e,p in flights:
            graph[s].append((e,p))
        pq=[]
        heapq.heappush(pq, (0, 0, src))

        prices=[float('inf')]*n
        prices[src]=0

        while pq:
            cnt,prc,node=heapq.heappop(pq)
            if cnt>k:
                continue
            for curr,currprice in graph[node]:
                if currprice+prc<prices[curr] and cnt<=k:
                    prices[curr]=currprice+prc
                    heapq.heappush(pq,(cnt+1,prices[curr],curr))

        if prices[dst]==float('inf'):
            return -1
        return prices[dst]

        