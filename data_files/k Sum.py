
__author__ = 'Danyang'


class Solution(object):
    def kSum(self, A, k, target):
        
        return self.dp(A, k, target)

    def dp(self, A, K, target):
        
        n = len(A)

        f = [[[0 for _ in xrange(target+1)] for _ in xrange(n+1)] for _ in xrange(K+1)]
        for ind, val in enumerate(A):
            if val <= target:
                for j in xrange(ind+1, n+1):  
                    f[1][j][val] = 1

        for i in xrange(2, K+1):
            for j in xrange(i, n+1):
                for v in xrange(1, target+1):
                    f[i][j][v] = 0
                    if v-A[j-1] >= 0:
                        f[i][j][v] += f[i-1][j-1][v-A[j-1]]
                    if j-1 >= i:
                        f[i][j][v] += f[i][j-1][v]

        return f[K][n][target]

    def dfs_TLE(self, A, k, target, cur, ret):
        if len(cur) == k and sum(cur) == target:  
            ret[0] += 1

        if not A or len(cur) >= k:
            return

        
        num = A.pop(0)
        self.dfs_TLE(A, k, target, cur, ret)
        A.push(0, num)

        num = A.pop(0)
        cur.append(num)
        self.dfs_TLE(A, k, target, cur, ret)
        cur.pop()
        A.push(0, num)

    def dfs_TLE_2(self, A, k, target, s, l, la, ret):
        
        if l == k and s == target:
            ret[0] += 1

        if not A or l >= k or la+l < k:
            return

        
        num = A.pop(0)
        self.dfs_TLE_2(A, k, target, s, l, la-1, ret)
        self.dfs_TLE_2(A, k, target, s+num, l+1, la-1, ret)
        A.push(0, num)


if __name__ == "__main__":
    assert Solution().kSum([1, 2, 3, 4], 2, 5) == 2
    assert Solution().kSum(
        [1, 3, 4, 5, 8, 10, 11, 12, 14, 17, 20, 22, 24, 25, 28, 30, 31, 34, 35, 37, 38, 40, 42, 44, 45, 48, 51, 54, 56,
         59, 60, 61, 63, 66], 24, 842) == 453474