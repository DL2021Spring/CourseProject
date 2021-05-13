
__author__ = 'Danyang'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        
        lst = []
        self.postTraverse_itr(root, lst)
        return lst



    def postTraverse(self, node, lst):
        if not node:
            return
        self.postTraverse(node.left, lst)
        self.postTraverse(node.right, lst)

        lst.append(node.val)

    def postTraverse_itr(self, root, lst):
        
        if not root:
            return
        stk = [root]
        while stk:
            cur = stk.pop()
            lst.insert(0, cur.val)  
            if cur.left:
                stk.append(cur.left)

            if cur.right:
                stk.append(cur.right)






if __name__=="__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    print Solution().postorderTraversal(t1)