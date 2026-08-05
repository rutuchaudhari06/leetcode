class Solution:
    def f(self,row,col,dp,mat):
        if row>=0 and col>=0 and mat[row][col]==1:
            return 0
        if row==0 and col==0:
            return 1
        if row<0 or col<0:
            return 0
        if dp[row][col]!=-1:
            return dp[row][col]
        up=self.f(row-1,col,dp,mat)
        left=self.f(row,col-1,dp,mat)
        dp[row][col]=up+left
        return up+left
        
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])

        dp=[[-1 for _ in range(m)] for _ in range(n)]
        return self.f(n-1,m-1,dp,obstacleGrid)