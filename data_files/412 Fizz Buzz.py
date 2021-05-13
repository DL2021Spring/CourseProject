
__author__ = 'Daniel'


class Solution(object):
    def fizzBuzz(self, n):
        
        ret = []
        for i in xrange(1, n+1):
            cur = ""
            if i % 3 == 0:
                cur += "Fizz"
            if i % 5 == 0:
                cur += "Buzz"
            if not cur:
                cur = str(i)

            ret.append(cur)

        return ret