
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        return len(reduce(lambda x, y: x & y, [set(list(elt)) for elt in cipher]))


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    number = int(f.readline().strip())
    cipher = []
    for t in xrange(number):
        
        cipher.append(f.readline().strip())

    
    s = "%s\n" % (Solution().solve(cipher))
    print s,
