




class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if not root:
            return 0

        max_child_depth = max([
            self.maxDepth(child)
            for child in root.children
        ] or [0])
        
        return max_child_depth + 1
