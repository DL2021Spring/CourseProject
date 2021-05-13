
__author__ = 'Daniel'


class Solution:
    def woodCut(self, L, k):
        
        if not L:
            return 0
        maxa = max(L)
        lo = 0
        hi = maxa+1
        while lo < hi:
            m = (lo+hi)/2
            if m == 0:
                return m
            cnt = 0
            for l in L:
                cnt += l/m
            if cnt >= k:
                lo = m+1
            else:
                hi = m

        return lo-1


if __name__ == "__main__":
    assert Solution().woodCut([2147483644, 2147483645, 2147483646, 2147483647], 4) == 2147483644