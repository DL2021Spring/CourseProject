
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, K, lst = cipher

        hm = {}
        for val in lst:
            if val in hm:
                hm[val] += 1
            else:
                hm[val] = 1

        cnt = 0
        for val in lst:
            target = val + K
            if target in hm:
                cnt += hm[target]
        return cnt


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    N, K = map(int, f.readline().strip().split(' '))
    lst = map(int, f.readline().strip().split(' '))
    cipher = N, K, lst
    
    s = "%s\n" % (Solution().solve(cipher))
    print s,
