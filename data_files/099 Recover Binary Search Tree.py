
__author__ = 'Danyang'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.val)

class Solution:
    def __init__(self):
        self.swapped_pair = []
        self.current = None
        self.pre = None

    def recoverTree(self, root):
        
        self.in_order(root)
        if len(self.swapped_pair)==2:
            self.swapped_pair[0][0].val, self.swapped_pair[1][1].val = self.swapped_pair[1][1].val, self.swapped_pair[0][0].val
        else: 
            self.swapped_pair[0][0].val, self.swapped_pair[0][1].val = self.swapped_pair[0][1].val, self.swapped_pair[0][0].val
        return root

    def in_order(self, current):
        if not current:
            return

        self.in_order(current.left)
        
        self.pre = self.current
        self.current = current
        if self.pre and not self.pre.val<self.current.val:
            if not self.swapped_pair:
                self.swapped_pair.append((self.pre, self.current))  
            else:
                self.swapped_pair.append((self.pre, self.current))  
        self.in_order(current.right)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

if __name__=="__main__":
    node1 = TreeNode(2)
    node2 = TreeNode(1)
    node1.right = node2
    print Solution().recoverTree(node1)