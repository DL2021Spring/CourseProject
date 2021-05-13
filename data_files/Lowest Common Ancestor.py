
__author__ = 'Danyang'


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return repr(self.val)


class Solution:
    def lowestCommonAncestor(self, root, A, B):
        
        p1 = self.path(root, A)
        p2 = self.path(root, B)
        p1.append(TreeNode(0))  
        p2.append(TreeNode(0))  
        for ind, val in enumerate(p1):
            if val != p2[ind]:
                return p1[ind-1]

    def path(self, root, target):
        
        ans = []
        self.get_path(root, target, [], ans)
        return ans

    def get_path(self, cur, target, path, ans):
        
        if not cur:
            return False

        path.append(cur)

        if cur == target:  
            
            ans.extend(path)  
            return True

        if cur.left and self.get_path(cur.left, target, path, ans):
            return True

        if cur.right and self.get_path(cur.right, target, path, ans):
            return True

        path.pop()
        return False


if __name__ == "__main__":
    node = TreeNode(1)
    print Solution().lowestCommonAncestor(node, node, node)

    nodes = dict(zip(range(3, 8), [TreeNode(i) for i in range(3, 8)]))
    nodes[4].left = nodes[3]
    nodes[4].right = nodes[7]
    nodes[7].left = nodes[5]
    nodes[7].right = nodes[6]
    print Solution().lowestCommonAncestor(nodes[4], nodes[3], nodes[5])
