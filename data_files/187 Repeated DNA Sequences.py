
__author__ = 'Daniel'


class Solution:
    def findRepeatedDnaSequences(self, s):
        
        if len(s) < 10:
            return []

        s = map(self.mapping, list(s))
        h = set()
        
        ret = set()
        cur = 0
        for i in xrange(10):
            cur <<= 2
            cur &= 0xFFFFF
            cur += s[i]
        h.add(cur)

        for i in xrange(10, len(s)):
            cur <<= 2
            cur &= 0xFFFFF  
            cur += s[i]
            if cur in h and cur not in ret:
                ret.add(cur)
            else:
                h.add(cur)

        return map(self.decode, ret)

    def decode(self, s):
        dic = {
            0: "A",
            1: "C",
            2: "G",
            3: "T"
        }
        ret = []
        for i in xrange(10):
            ret.append(dic[s%4])
            s >>= 2

        return "".join(reversed(ret))

    def mapping(self, a):
        dic = {
            "A": 0,
            "C": 1,
            "G": 2,
            "T": 3,
            }

        return dic[a]

if __name__ == "__main__":
    assert Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") == ['CCCCCAAAAA', 'AAAAACCCCC']
