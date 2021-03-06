
__author__ = 'Daniel'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        
        n = self.len(head)
        m = n/2
        mid = self.get(head, m)
        if n%2 != 0:
            mid = mid.next

        mid = self.reverse(mid)
        while head and mid:
            if head.val != mid.val:
                return False
            head = head.next
            mid = mid.next

        return True

    def len(self, head):
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next

        return cnt

    def get(self, head, n):
        cnt = 0
        cur = head
        while cnt < n:
            cnt += 1
            cur = cur.next

        return cur

    def reverse(self, head):
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, dummy.next
        while cur:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        if head: head.next = None
        return pre
