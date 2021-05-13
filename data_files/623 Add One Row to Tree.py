




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        return self.add(root, v, d, 1, "left")

    def add(self, node, v, d, cur_d, child) -> TreeNode:
        
        if cur_d == d:
            new = TreeNode(v)
            setattr(new, child, node)
            return new

        if node:
            node.left = self.add(node.left, v, d, cur_d + 1, "left")
            node.right = self.add(node.right, v, d, cur_d + 1, "right")
            return node


class Solution2:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node

        self.add(self, root, v, d, 1)
        return root

    def add(self, node, v, d, cur_d) -> None:
        if not node:
            return

        if cur_d + 1 == d:
            left = node.left
            right = node.right
            node.left = TreeNode(v)
            node.left.left = left
            node.right = TreeNode(v)
            node.right.right = right

        self.add(node.left, v, d, cur_d + 1)
        self.add(node.right, v, d, cur_d + 1)
