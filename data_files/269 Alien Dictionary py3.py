
from typing import List
from collections import defaultdict, deque


class Solution(object):
    def alienOrder(self, words: List[str]) -> str:
        G = self.construct_graph(words)
        visited = defaultdict(int)  
        ret = deque()
        for u in G.keys():
            if visited[u] == 0:
                if not self.topo_dfs(G, u, visited, ret):
                    return ""

        return "".join(ret)

    def construct_graph(self, words):
        G = defaultdict(list)
        
        for w in words:  
            for c in w:
                G[c]

        for i in range(len(words) - 1):  
            for c1, c2 in zip(words[i], words[i+1]):
                if c1 != c2:  
                    G[c1].append(c2)
                    break  

        return G

    def topo_dfs(self, G, u, visited, ret):
        
        visited[u] = 1
        for nbr in G[u]:
            if visited[nbr] == 1:
                return False
            if visited[nbr] == 0:
                if not self.topo_dfs(G, nbr, visited, ret):
                    return False

        visited[u] = 2
        ret.appendleft(u)  
        return True


if __name__ == "__main__":
    lst = ["ze", "yf", "xd", "wd", "vd", "ua", "tt", "sz", "rd", "qd", "pz", "op", "nw", "mt", "ln", "ko", "jm", "il",
           "ho", "gk", "fa", "ed", "dg", "ct", "bb", "ba"]
    assert Solution().alienOrder(lst) == "zyxwvutsrqponmlkjihgfedcba"
