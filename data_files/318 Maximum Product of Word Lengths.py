
__author__ = 'Daniel'


class Solution(object):
    def maxProduct(self, words):
        
        l = map(len, words)
        codes = map(self.encode, words)
        maxa = 0
        for i in xrange(len(codes)):
            for j in xrange(i+1, len(codes)):
                if codes[i] & codes[j] == 0:
                    maxa = max(maxa, l[i]*l[j])

        return maxa

    def encode(self, x):
        ret = 0
        for c in x:
            ret |= 1 << (ord(c)-ord('a'))
        return ret


if __name__ == "__main__":
    assert Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) == 16