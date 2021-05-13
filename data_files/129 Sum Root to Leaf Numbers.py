
__author__ = 'Danyang'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        
        result = []
        self.dfs(root, "", result)
        result = [int(element) for element in result]
        return sum(result)

    def dfs(self, root, cur, result):
        
        if not root:
            return
        cur = cur+str(root.val)
        if not root.left and not root.right:
            result.append(cur)
            return

        if root.left:
            self.dfs(root.left, cur, result)
        if root.right:
            self.dfs(root.right, cur, result)


    def dfs_error(self, root, cur, result):
        
        if not root:
            return

        cur.append(root.val)

        if not root.left and not root.right:
            result.append(cur)
            return

        if root.left:
            self.dfs_error(root.left, cur, result)  
        if root.right:
            self.dfs_error(root.right, cur, result)


if __name__=="__main__":
    nodes = [TreeNode(0), TreeNode(1), TreeNode(3)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    Solution().sumNumbers(nodes[0])