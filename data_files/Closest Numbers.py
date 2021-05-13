
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, A = cipher
        A.sort()

        diff = 1 << 31
        lst = []
        for i in xrange(N - 1):
            b = A[i + 1]
            a = A[i]
            if abs(a - b) < diff:
                diff = abs(a - b)
                lst = [a, b]
            elif abs(a - b) == diff:
                lst.append(a)
                lst.append(b)

        return " ".join(map(str, lst))


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    solution = Solution()
    N = int(f.readline().strip())
    A = map(int, f.readline().strip().split(' '))
    cipher = N, A

    
    s = "%s\n" % (solution.solve(cipher))
    print s,
