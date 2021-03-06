
__author__ = 'Danyang'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    
    def __init__(self):
        self.current_node = None  

    def sortedListToBST(self, head):
        
        if not head:
            return head

        self.current_node = head
        length = self.getLength(head)
        return self.sortedListToBST_dfs(0, length-1)

    def sortedListToBST_dfs(self, start, end):
        if start>end:
            return
        mid = (start+end)/2
        left_subtree = self.sortedListToBST_dfs(start, mid-1)
        root = TreeNode(self.current_node.val)
        self.current_node = self.current_node.next
        right_subtree = self.sortedListToBST_dfs(mid+1, end)

        root.left = left_subtree
        root.right = right_subtree
        return root

    def getLength(self, head):
        count = 0
        while head:
            head = head.next
            count += 1
        return count