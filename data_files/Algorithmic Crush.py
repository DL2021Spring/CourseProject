
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, M, queries = cipher

        qry = []
        for query in queries:
            qry.append((query[0], query[2]))
            qry.append((query[1] + 1, -query[2]))

        qry.sort(key=lambda x: (x[0], x[1]))
        

        maxa = -1 << 32
        cur = 0
        for q in qry:
            cur += q[1]
            maxa = max(maxa, cur)

        return maxa


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    N, M = map(int, f.readline().strip().split(' '))

    queries = []
    for t in xrange(M):
        
        queries.append(map(int, f.readline().strip().split(' ')))

    cipher = N, M, queries
    
    s = "%s\n" % (Solution().solve(cipher))
    print s,
