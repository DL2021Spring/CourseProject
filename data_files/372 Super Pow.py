
__author__ = 'Daniel'

C = 1337


class Solution(object):
    def superPow(self, a, b):
        
        if not b:
            return 1
        s = 1
        lsd = b.pop()  
        s *= (a % C) ** lsd
        s %= C
        rest = self.superPow(a, b)
        s *= rest ** 10
        s %= C
        return s

if __name__ == "__main__":
    print Solution().superPow(2, [1, 0])




