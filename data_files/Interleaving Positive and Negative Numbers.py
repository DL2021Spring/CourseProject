
__author__ = 'Daniel'


class Solution(object):
    def rerange(self, A):
        
        n = len(A)
        pos_cnt = len(filter(lambda x: x > 0, A))
        
        pos_expt = True if pos_cnt*2 > n else False

        neg = 0  
        pos = 0  
        for i in xrange(n):
            while neg < n and A[neg] > 0: neg += 1
            while pos < n and A[pos] < 0: pos += 1
            if pos_expt:
                A[i], A[pos] = A[pos], A[i]
            else:
                A[i], A[neg] = A[neg], A[i]

            if i == neg: neg += 1
            if i == pos: pos += 1

            pos_expt = not pos_expt


if __name__ == "__main__":
    A = [-33, -19, 30, 26, 21, -9]
    Solution().rerange(A)
    assert A == [-33, 30, -19, 26, -9, 21]