

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        A = sorted(cipher)
        cur = -5
        cnt = 0
        for a in A:
            if cur + 4 < a:
                cur = a
                cnt += 1
        return cnt


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    
    solution = Solution()
    n = int(f.readline().strip())


    
    cipher = map(int, f.readline().strip().split(' '))

    
    s = "%s\n" % (solution.solve(cipher))
    print s,
