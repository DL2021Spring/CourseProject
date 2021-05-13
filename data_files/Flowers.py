
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, K, C = cipher

        C.sort(reverse=True)

        group_cnt = N / K + 1  
        total_cost = 0
        for i in xrange(group_cnt):
            unit_cost = i + 1
            total_cost += unit_cost * sum(C[i * K:(i + 1) * K])
        return total_cost


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    N, K = map(int, f.readline().strip().split(' '))
    C = map(int, f.readline().strip().split(' '))
    cipher = N, K, C
    
    s = "%s\n" % (Solution().solve(cipher))
    print s,
