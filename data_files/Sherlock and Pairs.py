
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        hm = {}
        cnt = 0
        for ind, val in enumerate(cipher):
            if val in hm:
                cnt += 2 * len(hm[val])
                hm[val].append(ind)
            else:
                hm[val] = [ind]
        return cnt


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        N = f.readline().strip()
        cipher = map(int, f.readline().strip().split(' '))

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
