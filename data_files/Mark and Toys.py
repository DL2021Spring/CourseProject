

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        n, K, A = cipher
        A.sort()
        cnt = 0
        for elt in A:
            K -= elt
            if K >= 0:
                cnt += 1
            else:
                break
        return cnt


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    
    solution = Solution()
    n, K = map(int, f.readline().strip().split(' '))

    
    A = map(int, f.readline().strip().split(' '))

    cipher = n, K, A
    
    s = "%s\n" % (solution.solve(cipher))
    print s,
