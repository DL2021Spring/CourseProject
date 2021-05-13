
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, K, Q, A, q = cipher

        result = []
        for i in q:
            result.append(A[(i - K) % N])

        return "\n".join(map(str, result))


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    N, K, Q = map(int, f.readline().strip().split(' '))
    A = map(int, f.readline().strip().split(' '))

    q = []
    for i in xrange(Q):
        q.append(int(f.readline().strip()))

    cipher = N, K, Q, A, q


    
    s = "%s\n" % (Solution().solve(cipher))
    print s,
