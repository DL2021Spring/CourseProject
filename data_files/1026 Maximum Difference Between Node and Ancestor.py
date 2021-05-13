




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ret = 0

    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        self.dfs(root)
        return self.ret

    def dfs(self, node):
        if not node:
            return float("inf"), -float("inf")

        lmin, lmax = self.dfs(node.left)
        rmin, rmax = self.dfs(node.right)
        mini = min(lmin, rmin)
        maxa = max(lmax, rmax)
        if mini != float("inf"):
            self.ret = max(self.ret, abs(mini - node.val))
        if maxa != -float("inf"):
            self.ret = max(self.ret, abs(maxa - node.val))

        return min(mini, node.val), max(maxa, node.val)
