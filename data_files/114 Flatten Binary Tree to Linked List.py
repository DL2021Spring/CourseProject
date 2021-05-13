
__author__ = 'Danyang'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return repr(self.val)

class Solution:
    def flatten_data_structure(self, root):
        
        
        if not root:
            return

        lst = []
        self.dfs_traverse(root, lst)
        lst = lst[1:] 

        root.left = None
        cur = root
        for node in lst:
            node.left = None
            node.right = None
            cur.right = node
            cur = cur.right


    def dfs_traverse(self, root, lst):
        
        if not root:
            return
        lst.append(root)
        self.dfs_traverse(root.left, lst)
        self.dfs_traverse(root.right, lst)

    def flatten(self, root):
        
        if not root:
            return None


        left_last = self.get_last(root.left)

        left = self.flatten(root.left)
        right = self.flatten(root.right)

        
        
        

        root.left = None
        if left:
            root.right = left
            left_last.right = right
        else:
            root.right = right
        return root

    def get_last(self, root):
        
        if not root:
            return None
        if not root.left and not root.right:
            return root
        if root.right:
            return self.get_last(root.right)
        else:
            return self.get_last(root.left)

if __name__=="__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node1.left = node2
    Solution().flatten(node1)

