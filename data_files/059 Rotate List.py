
__author__ = 'Danyang'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return repr(self.val)

class Solution:
    def rotateRight(self, head, k):
        
        if not head:
            return None


        dummy = ListNode(0)
        dummy.next = head

        
        length = 0
        pre = dummy
        while pre.next:
            length += 1
            pre = pre.next
        
        last = pre

        
        k = k%length  

        
        count = 0
        pre = dummy
        while count<length-k:  
            count += 1
            pre = pre.next

        
        if k!=0: 
            pre.next, dummy.next, last.next = None, pre.next, dummy.next

        return dummy.next

if __name__=="__main__":
    length = 1
    lst = [ListNode(i+1) for i in xrange(length)]
    for i in range(length-1):
        lst[i].next = lst[i+1]
    Solution().rotateRight(lst[0], 1)
