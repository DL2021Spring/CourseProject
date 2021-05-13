
__author__ = 'Danyang'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        
        if not root:
            return []
        result = []
        next_level = [root]
        while next_level:
            current_level = next_level
            result.insert(0, map(lambda x: x.val, current_level))  

            next_level = []
            for element in current_level:
                if element.left:
                    next_level.append(element.left)
                if element.right:
                    next_level.append(element.right)
        return result

if __name__=="__main__":
    Solution().levelOrderBottom(TreeNode(1))










