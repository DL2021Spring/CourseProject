
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        A, B, N = cipher

        a, b = A, B
        cnt = 1
        while cnt < N:
            cnt += 1
            a, b = b, b * b + a

        return a


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    solution = Solution()

    cipher = map(int, f.readline().strip().split(' '))

    
    s = "%s\n" % (solution.solve(cipher))
    print s,
