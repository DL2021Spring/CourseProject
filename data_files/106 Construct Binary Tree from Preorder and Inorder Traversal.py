
__author__ = 'Danyang'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree_MLE(self, preorder, inorder):
        
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        root_index = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:root_index+1], inorder[0:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])

        return root
        
    def buildTree(self, preorder, inorder):
        
        self.preorder = preorder
        self.inorder = inorder
        return self._buildTree(0, len(preorder), 0, len(inorder))

    def _buildTree(self, pre_start, pre_end, in_start, in_end):
        if pre_start >= pre_end:
            return None
        root = TreeNode(self.preorder[pre_start])
        offset = self.inorder[in_start:in_end + 1].index(root.val)
        root.left = self._buildTree(pre_start + 1, pre_start + offset + 1, in_start, in_start + offset)
        root.right = self._buildTree(pre_start + offset + 1, pre_end, in_start + offset + 1, in_end)
        return root
