
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        tasks = cipher
        tasks.sort(key=lambda t: t[0])

        overshot = -1
        timer = 0
        for task in tasks:
            timer += task[1]
            overshot = max(overshot, timer - task[0])

        return overshot


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())
    cipher = []
    for t in xrange(testcases):
        
        cipher.append(map(lambda x: int(x), f.readline().strip().split(' ')))

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
