

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        return sum(cipher) / 2.0


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    
    solution = Solution()
    N = int(f.readline().strip())

    cipher = []
    for _ in xrange(N):
        
        cipher.append(int(f.readline().strip()))

    
    s = "%s\n" % (solution.solve(cipher))
    print s,
