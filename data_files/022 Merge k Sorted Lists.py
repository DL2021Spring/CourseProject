
__author__ = 'Danyang'
import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists_TLE1(self, lists):
        
        lists = filter(lambda x: x is not None, lists)
        if not lists:
            return

        length = len(lists)
        factor = 2
        while length>0:
            i = 0
            while True:
                try:
                    lists[i] = self.mergeTwoLists(lists[i], lists[i+factor/2])
                except IndexError:
                    break
                i += factor

            length /= 2
            factor *= 2

        return lists[0]

    def mergeKLists_TLE2(self, lists):
        
        lists = filter(lambda x: x is not None, lists)
        if not lists:
            return

        result = lists[0]
        for i in xrange(1, len(lists)):
            result = self.mergeTwoLists(result, lists[i])
        return result



    def mergeTwoLists(self, l1, l2):
        
        dummy = ListNode(0)
        dummy.next = l1

        pre = dummy
        the_other = l2
        while pre and pre.next:
            cur = pre.next
            if the_other and cur.val>the_other.val:
                
                temp = the_other.next
                pre.next, the_other.next = the_other, cur

                the_other = temp  
            pre = pre.next


        
        if the_other:
            pre.next = the_other  

        return dummy.next

    def mergeKLists(self, lists):
        
        heap = []
        for head_node in lists:
            if head_node:
                heapq.heappush(heap, (head_node.val, head_node))

        dummy = ListNode(0)

        cur = dummy
        while heap:
            smallest_node = heapq.heappop(heap)[1]
            cur.next = smallest_node
            cur = cur.next
            if smallest_node.next:
                heapq.heappush(heap, (smallest_node.next.val, smallest_node.next))
        return dummy.next

if __name__=="__main__":
    assert  Solution().mergeKLists([None, None])==None
    assert Solution().mergeKLists([ListNode(1), ListNode(0)]).val==0
