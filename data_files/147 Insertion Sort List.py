__author__ = 'Danyang'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def insertionSortList_TLE(self, head):
        
        comparator = lambda x, y: cmp(x.val, y.val)
        
        dummy_head = ListNode(0)
        dummy_head.next = head


        closed_tail = dummy_head.next
        while(closed_tail and closed_tail.next):
            open_head = closed_tail.next
            

            
            ptr_before = dummy_head
            ptr = dummy_head.next 

            
            while(ptr_before):
                if comparator(ptr, open_head)>0:
                    ptr_before.next = open_head
                    closed_tail.next = open_head.next
                    open_head.next = ptr

                    
                    break

                if ptr==open_head:
                    closed_tail = closed_tail.next
                    break

                ptr_before = ptr_before.next
                ptr = ptr.next


        return dummy_head.next


    def insertionSortList(self, head):
        
        comparator = lambda x, y: cmp(x.val, y.val)
        
        
        dummy = ListNode(0)  
        dummy.next = head

        closed_tail = head
        while (closed_tail and closed_tail.next):
            open_head = closed_tail.next
            open_head_next = closed_tail.next.next
            if not comparator(closed_tail, open_head)<=0:  

                pre = dummy
                while comparator(pre.next, open_head)<0:  
                    pre = pre.next

                
                open_head.next = pre.next
                pre.next = open_head

                closed_tail.next = open_head_next

            else:
                closed_tail = closed_tail.next


        return dummy.next

if __name__=="__main__":
    import random
    lst = [ListNode(i) for i in random.sample(xrange(-1000, 1000), 1000)]
    
    
    for i in range(len(lst)):
        try:
            lst[i].next = lst[i+1]
        except IndexError: 
            lst[i].next = None



    head = Solution().insertionSortList(lst[0])
    current = head
    for i in range(len(lst)):
        print current.val
        current = current.next



