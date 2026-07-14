class Solution:
    def bfs(self,sr,sc,image,k):
        
        q=deque([(sr,sc)])
        n=len(image)
        m=len(image[0])
        vis=[[0 for _ in range(m)] for _ in range(n)]
        d=[(-1,0),(1,0),(0,-1),(0,1)]

        old = image[sr][sc]
        while q:
            row,col=q.popleft()
            image[row][col]=k
            for i,j in d:
                nr=row+i
                nc=col+j
                if nc>=0 and nr>=0 and nr<n and nc<m and image[nr][nc] == old and not vis[nr][nc]:
                    vis[nr][nc]=1
                    q.append((nr,nc))
        
        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        return self.bfs(sr,sc,image,color)