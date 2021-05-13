

from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def alienOrder(self, words):
        
        V = self.construct_graph(words)
        visited = set()
        pathset = set()
        ret = []
        for v in V.keys():
            if v not in visited:
                if not self.topo_dfs(V, v, visited, pathset, ret):
                    return ""

        return "".join(reversed(ret))

    def construct_graph(self, words):
        V = defaultdict(list)
        
        for w in words:  
            for c in w:
                V[c]
        for i in xrange(len(words) - 1):  
            for j in xrange(min(len(words[i]), len(words[i+1]))):
                if words[i][j] != words[i+1][j]:
                    V[words[i][j]].append(words[i+1][j])
                    break  

        return V

    def topo_dfs(self, V, v, visited, pathset, ret):
        
        if v in pathset:
            return False

        pathset.add(v)
        for nbr in V[v]:
            if nbr not in visited:
                if not self.topo_dfs(V, nbr, visited, pathset, ret):
                    return False

        pathset.remove(v)
        visited.add(v)  
        ret.append(v)  
        return True

    def construct_graph_tedious(self, words, up, down, ptr, V):
        
        i = up
        while i < down:
            if ptr >= len(words[i]):
                i += 1
            else:
                if words[i][ptr] not in V:
                    V[words[i][ptr]] = []

                j = i+1
                while j < down and ptr < len(words[j]) and words[j][ptr] == words[i][ptr]:
                    j += 1

                self.construct_graph_tedious(words, i, j, ptr+1, V)
                if j < down and ptr < len(words[j]):
                    V[words[i][ptr]].append(words[j][ptr])

                i = j


if __name__ == "__main__":
    lst = ["ze", "yf", "xd", "wd", "vd", "ua", "tt", "sz", "rd", "qd", "pz", "op", "nw", "mt", "ln", "ko", "jm", "il",
           "ho", "gk", "fa", "ed", "dg", "ct", "bb", "ba"]
    assert Solution().alienOrder(lst) == "zyxwvutsrqponmlkjihgfedcba"
