

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        lst = list(cipher)
        ret = [lst[0]]
        cnt = 0
        for i in xrange(1, len(lst)):
            if lst[i] != ret[-1]:
                ret.append(lst[i])
            else:
                cnt += 1
        return cnt


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = f.readline().strip()

        
        s = "%s\n" % (solution.solve(cipher))
        print s,
