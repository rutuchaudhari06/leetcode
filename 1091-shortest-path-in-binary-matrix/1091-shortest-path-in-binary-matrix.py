import heapq

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0]==1:
            return -1
        if grid[n-1][n-1]==1:
            return -1
        pq=[]
        heapq.heappush(pq,(1,0,0))

        dist=[[float('inf') for _ in range(n)] for _ in range(n)]
        dist[0][0]=1

        while pq:
            wt,row,col=heapq.heappop(pq)
            
            for r in -1,0,1:
                for c in -1,0,1:
                    nr=row+r
                    nc=col+c
                    if 0<=nr<n and 0<=nc<n and grid[nr][nc]==0 and dist[nr][nc]>wt+1:
                        dist[nr][nc]=wt+1
                        heapq.heappush(pq,(dist[nr][nc],nr,nc))
        
        return -1 if dist[n-1][n-1] == float('inf') else dist[n-1][n-1]