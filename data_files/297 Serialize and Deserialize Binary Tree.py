
from collections import deque

__author__ = 'Daniel'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        
        if not root:
            return "null"

        ret = []
        q = []
        q.append(root)
        ret.append(str(root.val))  
        while q:
            l = len(q)
            for i in xrange(l):
                cur = q[i]
                if cur.left: q.append(cur.left)
                ret.append(self.encode(cur.left))
                if cur.right: q.append(cur.right)
                ret.append(self.encode(cur.right))

            q = q[l:]

        return ",".join(ret)

    def deserialize(self, data):
        
        lst = data.split(",")
        root = self.decode(lst[0])

        q = deque([root])
        i = 1
        while q:
            cur = q.popleft()
            if i < len(lst):
                cur.left = self.decode(lst[i])
                i += 1
                if cur.left: q.append(cur.left)
            if i < len(lst):
                cur.right = self.decode(lst[i])
                i += 1
                if cur.right: q.append(cur.right)

        return root

    def decode(self, s):
        if s == "null":
            return None
        else:
            return TreeNode(int(s))

    def encode(self, node):
        if not node:
            return "null"
        else:
            return str(node.val)
