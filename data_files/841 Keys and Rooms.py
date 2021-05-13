

from typing import List


class Solution:
    def canVisitAllRooms(self, G: List[List[int]]) -> bool:
        
        n = len(G)
        visited = [0 for _ in range(n)]  
        self.dfs(G, 0, visited)
        return all(e == 1 for e in visited)

    def dfs(self, G, u, visited):
        visited[u] = 1
        for nbr in G[u]:
            if not visited[nbr]:
                self.dfs(G, nbr, visited)


if __name__ == "__main__":
    assert Solution().canVisitAllRooms([[1],[2],[3],[]]) == True
    assert Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]]) == False
