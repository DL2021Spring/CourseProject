
__author__ = 'Daniel'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        
        if not root:
            return []

        ret = []
        self.dfs(root, [], ret)
        return ret

    def dfs(self, cur, path, ret):
        
        path.append(cur)
        if not cur.left and not cur.right:
            ret.append("->".join(map(lambda x: str(x.val), path)))
            return

        if cur.left:
            self.dfs(cur.left, path, ret)
            path.pop()  

        if cur.right:
            self.dfs(cur.right, path, ret)
            path.pop()  

    def dfs_path(self, cur, path, ret):
        if not cur:
            return

        path.append(cur)
        if not cur.left and not cur.right:
            ret.append("->".join(map(lambda x: str(x.val), path)))

        self.dfs_path(cur.left, path, ret)
        self.dfs_path(cur.right, path, ret)
        path.pop()
