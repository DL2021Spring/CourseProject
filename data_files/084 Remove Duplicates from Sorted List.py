
__author__ = 'Danyang'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        
        
        if not head:
            return head
        
        closed_ptr = head
        open_ptr = head.next
        while open_ptr:
            
            while open_ptr and closed_ptr.val==open_ptr.val:
                open_ptr = open_ptr.next

            closed_ptr.next = open_ptr
            closed_ptr = closed_ptr.next
            open_ptr = open_ptr.next if open_ptr else None

        return head

if __name__=="__main__":
    nodes = [ListNode(1) for _ in range(2)]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]

    Solution().deleteDuplicates(nodes[0])