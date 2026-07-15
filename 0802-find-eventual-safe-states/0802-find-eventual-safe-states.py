class Solution:
    def dfs(self,nums,node,vis,vispath,safe):
        vis[node]=1
        vispath[node]=1
        for it in nums[node]:
            if not vis[it]:
                if self.dfs(nums, it, vis, vispath,safe):
                    return True    
            elif vispath[it]:
                return True
        vispath[node]=0
        safe[node]=1
        return False
    def eventualSafeNodes(self, nums: List[List[int]]) -> List[int]:
        n=len(nums)
        
        vis=[0]*n
        vispath=[0]*n
        safe=[0]*n

        for i in range(n):
            if not vis[i]:
                self.dfs(nums,i,vis,vispath,safe)
        ans = []

        for i in range(n):
            if safe[i]:
                ans.append(i)

        return ans