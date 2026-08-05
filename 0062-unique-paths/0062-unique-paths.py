class Solution:
    def f(self,row,col,dp):
        if row==0 and col==0:
            return 1
        if row<0 or col<0:
            return 0
        if dp[row][col]!=-1:
            return dp[row][col]
        up= self.f(row-1,col,dp)
        left=self.f(row,col-1,dp)
        dp[row][col]=up+left
        return up+left
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for _ in range(n)] for _ in range(m)]
        return self.f(m-1,n-1,dp)
        