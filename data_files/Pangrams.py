
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        bucket = [False for _ in xrange(26)]
        for char in cipher:
            char = char.lower()
            ind = ord(char) - ord('a')
            try:
                bucket[ind] = True
            except IndexError:
                pass

        is_pangram = all(bucket)
        if is_pangram:
            return "pangram"
        else:
            return "not pangram"


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = 1

    for t in xrange(testcases):
        
        cipher = f.readline().strip()

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
