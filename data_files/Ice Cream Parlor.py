

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        M, N, C = cipher
        hash_map = {}
        for ind, val in enumerate(C):
            if val in hash_map:
                hash_map[val].append(ind)
            else:
                hash_map[val] = [ind]
        for ind, val in enumerate(C):
            target = M - val
            if target in hash_map:
                i = 0
                while i < len(hash_map[target]) and hash_map[target][i] <= ind:
                    i += 1
                if i != len(hash_map[target]):
                    return "%d %d" % (ind + 1, hash_map[target][i] + 1)


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        M = int(f.readline().strip())
        N = int(f.readline().strip())
        C = map(int, f.readline().strip().split(' '))
        cipher = M, N, C
        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
