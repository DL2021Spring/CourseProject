

MOD = 10 ** 9 + 7
dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))


class Solution:
    def findPaths(self, m: int, n: int, N: int, r: int, c: int) -> int:
        
        ret = 0
        F = [[0 for _ in range(n)] for _ in range(m)]
        F[r][c] = 1
        for _ in range(N):  
            F_new = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    for di, dj in dirs:
                        I = i + di
                        J = j + dj
                        if 0 <= I < m and 0 <= J < n:
                            F_new[I][J] = (F_new[I][J] + F[i][j]) % MOD
                        else:
                            ret = (ret + F[i][j]) % MOD

            F = F_new

        return ret


if __name__ == "__main__":
    assert Solution().findPaths(2, 2, 2, 0, 0) == 6
    assert Solution().findPaths(1, 3, 3, 0, 1) == 12
