

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        r, c = cipher
        r, c = r - 1, c - 1

        return r / 2 * 10 + r % 2 + c * 2


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    
    solution = Solution()

    cipher = map(int, f.readline().strip().split(' '))

    
    s = "%s\n" % (solution.solve(cipher))
    print s,
