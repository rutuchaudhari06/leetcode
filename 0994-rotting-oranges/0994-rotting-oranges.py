class Solution:
        
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        n=len(grid)
        m=len(grid[0])
        vis=[[0 for _ in range(m)] for _ in range(n)]
        d=[(-1,0),(1,0),(0,-1),(0,1)]
        cnt=0
        fresh=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j,0))
                    vis[i][j]=2
                elif grid[i][j]==1:
                    fresh+=1
        
        while q:
            row,col,t=q.popleft()
            cnt=max(cnt,t)
            for i,j in d:
                nr=row+i
                nc=col+j
                if nc>=0 and nr>=0 and nr<n and nc<m and grid[nr][nc] == 1 and not vis[nr][nc]:
                    vis[nr][nc]=1
                    fresh-=1
                    q.append((nr,nc,t+1))
        
        if fresh>0:
            return -1
        return cnt