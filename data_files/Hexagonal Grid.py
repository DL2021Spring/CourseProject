

__author__ = 'Danyang'


class Solution(object):
    def __init__(self):
        self.delta = [(0, 1), (1, 0), (1, -1)]  
        

    def solve(self, cipher):
        
        ret = self.rec(cipher)
        if ret:
            return "YES"
        else:
            return "NO"

    def rec(self, grid):
        changed = False
        m = len(grid)
        n = len(grid[0])

        for i in xrange(m):
            for j in xrange(n):
                if not changed:  
                    if grid[i][j] == 0:
                        changed = True
                        grid[i][j] = 1
                        for d in self.delta:
                            i2 = i + d[0]
                            j2 = j + d[1]
                            if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == 0:
                                grid[i2][j2] = 1
                                if self.rec(grid):
                                    return True
                                grid[i2][j2] = 0
                        grid[i][j] = 0
        if not changed:
            return True


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    solution = Solution()
    testcases = int(f.readline().strip())
    for t in xrange(testcases):
        
        int(f.readline().strip())
        cipher = []
        for _ in xrange(2):
            cipher.append(map(int, list(f.readline().strip())))

        
        s = "%s\n" % (solution.solve(cipher))
        print s,
