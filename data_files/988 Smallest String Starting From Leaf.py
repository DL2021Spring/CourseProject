




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import Tuple
from collections import deque


class Solution:
    def __init__(self):
        self.mn: Tuple[int] = None

    def smallestFromLeaf(self, root: TreeNode) -> str:
        
        self.dfs(root, deque())
        if not self.mn:
            return ""
        return "".join(
            chr(e + ord("a"))
            for e in self.mn
        )

    def dfs(self, node, cur_deque):
        if not node:
            return

        cur_deque.appendleft(node.val)
        if not node.left and not node.right:
            t = tuple(cur_deque)
            if not self.mn or t < self.mn:
                self.mn = t
        else:
            self.dfs(node.left, cur_deque)
            self.dfs(node.right, cur_deque)
        
        cur_deque.popleft()
