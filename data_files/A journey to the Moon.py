
__author__ = 'Danyang'


class DisjointSet(object):
    def __init__(self, n):
        self.rank = [1 for _ in xrange(n)]
        self.parent = [i for i in xrange(n)]
        self.n = n

    def find(self, i):
        if i == self.parent[i]:
            return i
        else:
            self.parent[i] = self.find(self.parent[i])  
            return self.parent[i]

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)

        if x == y: return
        self.parent[x] = y
        self.rank[y] += self.rank[x]

    def card(self):
        card = 0
        for i in xrange(self.n):
            if self.parent[i] == i:
                card += 1
        return card


class Solution(object):
    def solve(self, cipher):
        
        N, pairs = cipher
        djs = DisjointSet(N)
        for a, b in pairs:
            djs.union(a, b)

        result = 0
        for i in xrange(N):
            if djs.find(i) == i:  
                
                result += (djs.rank[i]) * (N - djs.rank[i])
        return result / 2


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    solution = Solution()

    N, I = map(int, f.readline().strip().split(' '))

    pairs = []
    for i in xrange(I):
        pairs.append(map(int, f.readline().strip().split(' ')))

    cipher = N, pairs
    
    s = "%s\n" % (solution.solve(cipher))
    print s,
