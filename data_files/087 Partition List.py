
__author__ = 'Danyang'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return repr(self.val)

class Solution:
    def partition(self, head, x):
        
        dummy = ListNode(0)
        dummy.next = head
        dummy_smaller = ListNode(0)
        dummy_larger = ListNode(0)

        pre = dummy
        pre_smaller = dummy_smaller
        pre_larger = dummy_larger
        while pre.next:
            cur = pre.next
            if cur.val<x:
                pre_smaller.next = cur
                pre_smaller = pre_smaller.next
            else:
                pre_larger.next = cur
                pre_larger = pre_larger.next
            pre = pre.next
        
        pre_larger.next = None  
        
        pre_smaller.next = dummy_larger.next
        return dummy_smaller.next

if __name__=="__main__":
    lst = [ListNode(2), ListNode(1)]
    for ind in xrange(len(lst)-1):
        lst[ind].next = lst[ind+1]
    Solution().partition(lst[0], 2)