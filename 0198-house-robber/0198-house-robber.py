class Solution:
    def f(self,idx,nums,dp):
        if idx < 0:
            return 0
        if idx == 0:
            return nums[0]
        if dp[idx]!=-1:
            return dp[idx]

        mon=self.f(idx-2,nums,dp)+nums[idx]
        nomon=self.f(idx-1,nums,dp)
        dp[idx]=max(mon,nomon)
        return dp[idx]

    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        return self.f(n-1,nums,dp)
        