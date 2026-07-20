class Solution:
    def f(self,idx,nums,dp):
        if idx==0:
            return nums[0]
        if idx<0:
            return 0
        if dp[idx]!=-1:
            return dp[idx]
        mon=nums[idx]+self.f(idx-2,nums,dp)
        nomon=self.f(idx-1,nums,dp)
        dp[idx]=max(mon,nomon)
        return dp[idx]
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums)
        dp=[-1]*n
        first=self.f(n-2,nums,dp)
        
        prev2 = 0
        prev = nums[1]

        for i in range(2, n):
            pick = nums[i] + prev2
            notPick = prev

            curr = max(pick, notPick)

            prev2 = prev
            prev = curr

        return max(first,prev)
