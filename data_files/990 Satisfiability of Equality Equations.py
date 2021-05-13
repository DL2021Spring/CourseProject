

from typing import List


class DisjointSet:
    def __init__(self):
        self.pi = {}

    def union(self, x, y):
        self.pi[self.find(x)] = self.find(y)

    def find(self, x):
        if x not in self.pi:
            self.pi[x] = x
        elif self.pi[x] != x:
            self.pi[x] = self.find(self.pi[x])
        return self.pi[x]

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        ds = DisjointSet()
        neqs = []  
        for e in equations:
            a = e[0]
            b = e[-1]
            sign = e[1:-1]
            if sign == "==":
                ds.union(a, b)
            else:
                neqs.append((a, b))

        for a, b in neqs:
            if ds.find(a) == ds.find(b):
                return False

        return True
