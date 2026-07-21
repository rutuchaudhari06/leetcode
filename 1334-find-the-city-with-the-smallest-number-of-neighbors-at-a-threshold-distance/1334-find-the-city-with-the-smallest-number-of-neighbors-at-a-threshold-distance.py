class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], th: int) -> int:
        mat=[[float('inf') for _ in range(n)] for _ in range(n)]

        for u,v,w in edges:
            mat[u][v]=w
            mat[v][u]=w

        for i in range(n):
            mat[i][i]=0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if mat[i][k] == float('inf') or mat[k][i] == float('inf'):
                        continue
                    mat[i][j]=min(mat[i][j], mat[i][k]+mat[k][j])

        cntmax=n
        city=-1

        for i in range(n):
            cnt=0
            for j in range(n):
                if mat[i][j]<=th:
                    cnt+=1
            if cntmax>=cnt:
                cntmax=cnt
                city=i

        return city
