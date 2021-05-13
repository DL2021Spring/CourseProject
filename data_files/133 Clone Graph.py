
__author__ = 'Danyang'

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
    def __repr__(self):
        return repr(self.label)

class Solution:
    def cloneGraph_TLE(self, node):
        
        return self.clone_graph_visited(node, set())

    def clone_graph_visited(self, node, visited_set):
        
        if not node:
            return
        visited_set.add(node)
        neighbors_cloned = [self.clone_graph_visited(neighbor, set(visited_set)) for neighbor in node.neighbors if neighbor not in visited_set]
        node_cloned = UndirectedGraphNode(node.label)
        for neighbor_cloned in neighbors_cloned:
            if neighbor_cloned not in visited_set:
                neighbor_cloned.neighbors.append(node_cloned)
        node_cloned.neighbors = neighbors_cloned
        return node_cloned

    def cloneGraph(self, node):
        
        if not node:
            return

        original2copy = {} 
        q = [node]  

        clone = UndirectedGraphNode(node.label)
        original2copy[node] = clone
        while q:
            cur = q.pop()
            for neighbor in cur.neighbors:
                if neighbor in original2copy:  
                    original2copy[cur].neighbors.append(original2copy[neighbor])
                else:
                    q.append(neighbor)
                    clone_neighbor = UndirectedGraphNode(neighbor.label)
                    original2copy[neighbor] = clone_neighbor
                    original2copy[cur].neighbors.append(original2copy[neighbor])

        return original2copy[node]


if __name__=="__main__":
    lst = [UndirectedGraphNode(i+1) for i in range(3)]
    for item in lst:
        item.neighbors = list(lst)
        item.neighbors.remove(item)
    cloned = Solution().cloneGraph(lst[0])
    assert cloned.neighbors[0].label in (2, 3)
    assert cloned.neighbors[1].label in (2, 3)


