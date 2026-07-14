from collections import deque

class Solution:
    def bfs(self, grid, r, c, vis):
        q = deque([(r, c)])
        vis[r][c] = 1

        n = len(grid)
        m = len(grid[0])

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if (
                    0 <= nr < n and
                    0 <= nc < m and
                    grid[nr][nc] == "1" and
                    not vis[nr][nc]
                ):
                    vis[nr][nc] = 1
                    q.append((nr, nc))

    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])

        vis = [[0]*m for _ in range(n)]
        cnt = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1" and not vis[r][c]:
                    cnt += 1
                    self.bfs(grid, r, c, vis)

        return cnt