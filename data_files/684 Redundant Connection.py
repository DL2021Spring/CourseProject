

from typing import List
from collections import defaultdict


class DisjointSet():
    def __init__(self):
        self.sz = {}  
        self.pi = {}  

    def add(self, x):
        if x not in self.pi:  
            self.sz[x] = 1
            self.pi[x] = x

    def unionize(self, x, y):
        p1 = self.root(x)
        p2 = self.root(y)
        if p1 != p2:
            sz1 = self.sz[p1]
            sz2 = self.sz[p2]
            if sz1 > sz2:
                p1, p2 = p2, p1

            self.pi[p1] = p2
            self.sz[p2] += self.sz[p1]
            del self.sz[p1]

    def root(self, x):
        p = self.pi[x]
        if p != x:
            self.pi[x] = self.root(p)

        return self.pi[x]

    def is_union(self, x, y):
        if x in self.pi and y in self.pi:
            return self.root(x) == self.root(y)

        return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        ds = DisjointSet()
        for p, q in edges:
            ds.add(p)
            ds.add(q)
            if ds.is_union(p, q):
                return [p, q]

            ds.unionize(p, q)

        raise

class Solution_dfs:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        G = defaultdict(set)
        for p, q in edges:
            G[p].add(q)
            G[q].add(p)

        visited = set()
        for k in G.keys():
            if k not in visited:
                circle = self.dfs(G, k, None, set([k]), [k], visited)
                if circle:
                    for p, q in reversed(edges):
                        if p in circle and q in circle:
                            return [p, q]

        raise

    def dfs(self, G, cur, pi, path, path_list, visited):
        visited.add(cur)

        for nbr in G[cur]:
            if nbr != pi:
                if nbr in path:
                    
                    circle = set()
                    in_circle = False
                    for e in path_list:
                        if e == nbr:
                            in_circle = True
                        if in_circle:
                            circle.add(e)
                    return circle

                path.add(nbr)
                path_list.append(nbr)
                circle = self.dfs(G, nbr, cur, path, path_list, visited)
                if circle:
                    return circle
                path.remove(nbr)
                path_list.pop()

        return None


if __name__ == "__main__":
    assert Solution().findRedundantConnection([[1,2], [1,3], [2,3]]) == [2, 3]
    assert Solution().findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]) == [1, 4]
    assert Solution().findRedundantConnection([[30,44],[34,47],[22,32],[35,44],[26,36],[2,15],[38,41],[28,35],[24,37],[14,49],[44,45],[11,50],[20,39],[7,39],[19,22],[3,17],[15,25],[1,39],[26,40],[5,14],[6,23],[5,6],[31,48],[13,22],[41,44],[10,19],[12,41],[1,12],[3,14],[40,50],[19,37],[16,26],[7,25],[22,33],[21,27],[9,50],[24,42],[43,46],[21,47],[29,40],[31,34],[9,31],[14,31],[5,48],[3,18],[4,19],[8,17],[38,46],[35,37],[17,43]]) == [5,48]
