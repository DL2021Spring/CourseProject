
__author__ = 'Daniel'


class Solution:
    def findOrder(self, numCourses, prerequisites):
        
        V = {}
        for i in xrange(numCourses):
            V[i] = []

        for edge in prerequisites:
            V[edge[1]].append(edge[0])

        return self.topological_sort(V)

    def topological_sort(self, V):
        visited = set()
        marked = set()
        ret = []

        for k in V.keys():
            if k not in visited:
                if not self.dfs(V, k, visited, marked, ret):
                    return []

        ret.reverse()
        return ret

    def dfs(self, V, k, visited, marked, ret):
        
        if k in marked:
            return False

        marked.add(k)
        for neighbor in V[k]:
            if neighbor not in visited:
                if not self.dfs(V, neighbor, visited, marked, ret):
                    return False

        marked.remove(k)
        visited.add(k)
        ret.append(k)
        return True


if __name__ == "__main__":
    assert Solution().findOrder(2, [[0, 1], [1, 0]]) == []