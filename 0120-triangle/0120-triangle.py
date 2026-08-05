class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[-1] * len(row) for row in triangle]
        n=len(triangle)
        for i in range(n):
            dp[n-1][i]=triangle[n-1][i]

        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                d=triangle[i][j]+dp[i+1][j]
                dg=triangle[i][j] + dp[i+1][j+1]
                dp[i][j]=min(d,dg)

        return dp[0][0]