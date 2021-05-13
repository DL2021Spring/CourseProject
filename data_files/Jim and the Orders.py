

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        A = cipher
        n = len(A)
        idx = sorted(range(n), key=lambda k: A[k][0] + A[k][1])
        return " ".join(map(lambda x: str(x + 1), idx))


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    
    solution = Solution()
    n = int(f.readline().strip())

    cipher = []
    for i in xrange(n):
        
        t = map(int, f.readline().strip().split(' '))
        cipher.append(tuple(t))

    
    s = "%s\n" % (solution.solve(cipher))
    print s,
