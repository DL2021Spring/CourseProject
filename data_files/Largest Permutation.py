

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, K, lst = cipher
        for i in xrange(len(lst)):
            if K <= 0:
                break
            maxa, idx = -1, 0
            for j in xrange(i, len(lst)):
                if lst[j] > maxa:
                    maxa = lst[j]
                    idx = j
            if idx != i:
                K -= 1
                lst[idx], lst[i] = lst[i], lst[idx]

        return " ".join(map(str, lst))


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    solution = Solution()

    N, K = map(int, f.readline().strip().split(' '))
    lst = map(int, f.readline().strip().split(' '))
    cipher = (N, K, lst)
    
    s = "%s\n" % (solution.solve(cipher))
    print s,
