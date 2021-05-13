
__author__ = 'Danyang'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return repr(self.val)

    def __str__(self):
        return str(self.val)+", "+str(self.next)

class Solution:
    def reverseBetween(self, head, m, n):
        
        
        if not head or m>=n:
            return head

        dummy = ListNode(0)
        dummy.next = head

        cnt = 1  
        pre = dummy

        start_pre = None
        start = None

        cur = pre.next  
        while pre.next:
            
            if cnt==m:
                start_pre = pre
                start = cur

            
            
            
            elif m<cnt<=n:
                
                
                
                

                
                cur.next, pre, cur = pre, cur, cur.next  
                cnt += 1
                continue

            
            elif cnt==n+1:
                end = pre
                start_pre.next = end
                start.next = cur
                break



            pre = pre.next
            cur = cur.next
            cnt += 1

        return dummy.next

if __name__=="__main__":
    length = 3
    lst = [ListNode(i+1) for i in range(length)]
    for i in xrange(length-1):
        lst[i].next = lst[i+1]
    print Solution().reverseBetween(lst[0], 1, 3)