




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_depth = -float("inf")
        self.expecting_partial = False

    def isCompleteTree(self, root: TreeNode) -> bool:
        
        return self.dfs(root, 0)

    def dfs(self, node, d):
        if not node:
            
            if self.max_depth == -float("inf"):  
                self.max_depth = d - 1
                return True
            elif self.expecting_partial:
                return d == self.max_depth
            else:
                if d == self.max_depth + 1:
                    return True
                if d == self.max_depth:
                    self.expecting_partial = True
                    return True
                return False

        return self.dfs(node.left, d + 1) and self.dfs(node.right, d + 1)
