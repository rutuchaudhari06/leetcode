class Solution:
    def f(self,i,j,mat,dp):
        if i==0 and j==0:
            return mat[0][0]
        if i<0 or j<0:
            return float('inf')
        if dp[i][j]!=-1:
            return dp[i][j]
        up=mat[i][j]+ self.f(i-1,j,mat,dp)
        left=mat[i][j]+self.f(i,j-1,mat,dp)

        dp[i][j]=min(up,left)
        return min(up,left)


    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[-1 for _ in range(m)] for _ in range(n)]

        return self.f(n-1,m-1,grid,dp)