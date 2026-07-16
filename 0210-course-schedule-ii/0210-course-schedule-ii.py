class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]
        for a,b in prerequisites:
            graph[b].append(a)
        n=numCourses
        indeg=[0]*n

        for i in range(n):
            for it in graph[i]:
                indeg[it]+=1
        
        q=deque()
        ans=[]
        for i in range(n):
            if indeg[i]==0:
                q.append(i)
        
        while q:
            node =q.popleft()
            ans.append(node)
            for it in graph[node]:
                indeg[it]-=1
                if indeg[it]==0:
                    q.append(it)
        if len(ans) != numCourses:
            return []
        return ans
            

                    
        
        