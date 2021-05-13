
__author__ = 'Daniel'


class Solution:
    def convertToTitle(self, n):
        
        sb = []  
        while n:
            n -= 1  
            sb.append(chr(ord("A")+n%26))
            n /= 26

        return "".join(reversed(sb))

