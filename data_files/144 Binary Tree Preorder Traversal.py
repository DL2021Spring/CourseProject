
__author__ = 'Danyang'



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        
        ret = []
        cur = root
        while cur:
            if not cur.left:
                ret.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right

                if not pre.right:
                    pre.right = cur
                    ret.append(cur.val)
                    cur = cur.left
                else:
                    pre.right = None
                    cur = cur.right

        return ret

    def preorderTraversal_memory(self, root):
        
        lst = []
        self.preTraverse_itr(root, lst)
        return lst


    def preTraverse(self, node, lst):
        if not node:
            return
        lst.append(node.val)

        self.preTraverse(node.left, lst)
        self.preTraverse(node.right, lst)

    def preTraverse_itr(self, root, lst):
        
        if not root:
            return
        stk = [root]
        while stk:
            node = stk.pop()
            lst.append(node.val)
            if node.right:  
                stk.append(node.right)

            if node.left:
                stk.append(node.left)



if __name__=="__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    print Solution().preorderTraversal(t1)