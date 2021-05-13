
__author__ = 'Danyang'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        
        result = []
        q = []
        if root:
            q.append(root)

        while q:
            length = len(q)
            
            for i in range(length):
                cur = q[i]
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            result.append(map(lambda x: x.val, q[:length]))  
            q = q[length:]  
        return result

if __name__=="__main__":
    nodes = [TreeNode(i) for i in range(3)]
    nodes[0].left = nodes[1]
    nodes[1].left = nodes[2]
    print Solution().levelOrder(nodes[0])


