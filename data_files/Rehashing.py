
__author__ = 'Danyang'


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return repr(self.val)


class Solution:
    def rehashing(self, hashTable):
        
        cap = len(hashTable)
        cap *= 2
        ht = [None for _ in xrange(cap)]
        for node in hashTable:
            while node:
                self.__rehash(ht, ListNode(node.val))  
                node = node.next
        return ht

    def __rehash(self, ht, node):
        code = self.__hashcode(node.val, len(ht))
        if ht[code] is None:
            ht[code] = node
        else:
            cur = ht[code]
            while cur.next:
                cur = cur.next
            cur.next = node

    def __hashcode(self, key, capacity):
        return key%capacity


if __name__ == "__main__":
    hashTable = [None for _ in xrange(3)]
    n0 = ListNode(29)
    n1 = ListNode(5)
    n0.next = n1
    hashTable[2] = n0

    print Solution().rehashing(hashTable)