

from typing import List


dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0

        ret = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    ret = max(ret, self.dfs(grid, i, j, visited))

        return ret

    def dfs(self, grid, i, j, visited) -> int:
        visited[i][j] = True
        ret = 1
        m, n = len(grid), len(grid[0])
        for di, dj in dirs:
            I = i + di
            J = j + dj
            if 0 <= I < m and 0 <= J < n and not visited[I][J] and grid[I][J] == 1:
                ret += self.dfs(grid, I, J, visited)

        return ret


if __name__ == "__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    assert Solution().maxAreaOfIsland(grid) == 6
