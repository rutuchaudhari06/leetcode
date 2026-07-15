class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        q = deque()
        dist = [[0] * m for _ in range(n)]
        vis = [[0] * m for _ in range(n)]

        # Put all 0's into the queue
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    vis[i][j] = 1

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while q:
            row, col, d = q.popleft()
            dist[row][col] = d

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if (
                    0 <= nr < n and
                    0 <= nc < m and
                    not vis[nr][nc]
                ):
                    vis[nr][nc] = 1
                    q.append((nr, nc, d + 1))

        return dist