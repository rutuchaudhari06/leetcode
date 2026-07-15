class Solution:
    def bfs(self, board, r,c,vis):
        n=len(board)
        m=len(board[0])
        vis[r][c]=1
        q=deque([(r,c)])
        d = [(-1,0), (1,0), (0,-1), (0,1)]
        while q:
            row,col=q.popleft()
            for i,j in d:
                nr=row+i
                nc=col+j
                if (0 <= nr < n and
                    0 <= nc < m and
                    not vis[nr][nc] and board[nr][nc]==1):
                    q.append((nr,nc))
                    vis[nr][nc]=1
    def numEnclaves(self, board: List[List[int]]) -> int:
        n=len(board)
        m=len(board[0])

        vis=[[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i+1==n or j+1==m or i-1<0 or j-1<0:
                    if board[i][j]==1:
                        self.bfs(board,i,j,vis)
        cnt=0
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and board[i][j]==1:
                    cnt+=1
        return cnt
