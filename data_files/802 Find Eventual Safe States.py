

from typing import List, Set


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        visit: List[int] = [0 for _ in graph]  
        acyclic: Set[int] = set()
        for u in range(len(graph)):
            if visit[u] == 0:
                self.dfs(graph, u, visit, acyclic)

        return [
            u
            for u in range(len(graph))
            if u in acyclic
        ]

    def dfs(self, graph, cur, visit, acyclic):
        visit[cur] = 1
        for nbr in graph[cur]:
            if visit[nbr] == 2:
                if nbr in acyclic:
                    continue
                else:
                    break
            if visit[nbr] == 1:
                break
            if visit[nbr] == 0 and not self.dfs(graph, nbr, visit, acyclic):
                break
        else:
            acyclic.add(cur)
            visit[cur] = 2
            return True

        visit[cur] = 2
        return False


if __name__ == "__main__":
    assert Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]) == [2,4,5,6]
