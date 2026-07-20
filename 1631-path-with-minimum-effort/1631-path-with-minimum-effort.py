class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n=len(heights)
        m=len(heights[0])

        dist=[[float('inf') for _ in range(m)] for _ in range(n)]
        dist[0][0]=0
        pq=[]
        heapq.heappush(pq,(0,0,0))
        d=[(-1,0),(1,0),(0,-1),(0,1)]
        while pq:
            effort,row,col=heapq.heappop(pq)
            
            for i,j in d:
                nr=row+i
                nc=col+j
                if 0<=nr<n and 0<=nc<m:
                    eff=abs(heights[row][col]-heights[nr][nc])
                    neweff=max(effort,eff)
                    if neweff<dist[nr][nc]:
                        dist[nr][nc]=neweff
                        heapq.heappush(pq,(neweff,nr,nc))
                        
        return dist[n-1][m-1]

