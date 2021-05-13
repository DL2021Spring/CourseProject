



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""

        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        ret = [str(t.val)]
        if left or right:
            ret.append("(" + left + ")")
        if right:
            ret.append("(" + right + ")")

        return "".join(ret)
