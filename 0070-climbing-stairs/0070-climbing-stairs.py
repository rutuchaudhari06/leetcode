class Solution:
    def f(self, idx,dp):
        if idx == 0:
            return 1
        if idx == 1:
            return 1
        if dp[idx]!=-1:
            return dp[idx]
        dp[idx]=self.f(idx-1,dp) + self.f(idx-2,dp)
        return dp[idx]

    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        return self.f(n,dp)