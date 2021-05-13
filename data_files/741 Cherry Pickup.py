

from typing import List


class Solution:
    def __init__(self):
        self.cache = {}

    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        return max(0, self.F(grid, 0, 0, 0))

    def F(self, grid, r1, c1, r2):
        n = len(grid)
        if (r1, c1, r2) not in self.cache:
            ret = float("-inf")
            c2 = r1 + c1 - r2   
            if 0 <= r1 < n and 0 <= c1 < n and 0 <= r2 < n and 0 <= c2 < n:
                if grid[r1][c1] != -1 and grid[r2][c2] != -1:
                    ret = 0
                    ret += grid[r1][c1]
                    if r1 != r2:
                        ret += grid[r2][c2]

                    if r1 == n - 1 and c1 == n - 1:
                        pass  
                    else:
                        ret += max(
                            self.F(grid, r1+1, c1, r2+1),   
                            self.F(grid, r1+1, c1, r2),  
                            self.F(grid, r1, c1+1, r2+1),  
                            self.F(grid, r1, c1+1, r2),  
                        )

            self.cache[r1, c1, r2] = ret

        return self.cache[r1, c1, r2]


if __name__ == "__main__":
    assert Solution().cherryPickup(
        [[0, 1, -1],
         [1, 0, -1],
         [1, 1,  1]]
    ) == 5

    assert Solution().cherryPickup(
        [[1, 1, -1],
         [1, -1, 1],
         [-1, 1, 1]]
    ) == 0
