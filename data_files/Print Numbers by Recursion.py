
__author__ = 'Daniel'


class Solution(object):
    def numbersByRecursion(self, n):
        return self.rec(n)

    def rec(self, n):
        if n == 0:
            return []
        if n == 1:
            return [i+1 for i in xrange(9)]
        else:
            lst = self.rec(n-1)
            l = len(lst)
            cur = []
            prev = lst[-1]+1
            for i in xrange(prev-prev/10):
                for j in xrange(10):
                   cur.append(lst[prev/10-1+i]*10+j)

            lst.extend(cur)
            return lst

if __name__ == "__main__":
    print Solution().numbersByRecursion(2)
    assert Solution().numbersByRecursion(2) == [i+1 for i in xrange(99)]