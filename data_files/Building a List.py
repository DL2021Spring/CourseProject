
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        s = cipher
        s = "".join(sorted(list(s)))
        result = []
        self.dfs(s, "", result)
        return "\n".join(result[1:])

    def dfs(self, seq, cur, result):
        result.append(cur)
        if seq:
            for i in xrange(len(seq)):
                self.dfs(seq[i + 1:], cur + seq[i], result)


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        N = int(f.readline().strip())
        cipher = f.readline().strip()

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
