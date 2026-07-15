class Solution:
    def dfs(self,nums,node,vis,vispath):
        vis[node]=1
        vispath[node]=1
        for it in nums[node]:
            if not vis[it]:
                if self.dfs(nums, it, vis, vispath):
                    return True    
            elif vispath[it]:
                return True
        vispath[node]=0
        return False
    def canFinish(self, numCourses: int, numslist: List[List[int]]) -> bool:
        nums = [[] for _ in range(numCourses)]

        for a, b in numslist:
            nums[b].append(a)
        n=len(nums)
        
        vis=[0]*n
        vispath=[0]*n

        for i in range(n):
            if not vis[i]:
                if self.dfs(nums,i,vis,vispath):
                    return False
        return True
