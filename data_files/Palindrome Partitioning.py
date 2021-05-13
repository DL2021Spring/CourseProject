
__author__ = 'Daniel'


class Solution:
    def partition(self, s):
        
        ret = []
        self.backtrack(s, [], ret)
        return ret

    def backtrack(self, s, cur_lvl, ret):
        
        if not s:
            ret.append(list(cur_lvl))

        for i in xrange(1, len(s)+1):
            if self.predicate(s[:i]):
                cur_lvl.append(s[:i])
                self.backtrack(s[i:], cur_lvl, ret)
                cur_lvl.pop()

    def predicate(self, s):
        return s == s[::-1]


if __name__ == "__main__":
    assert Solution().partition("aabbc") == [['a', 'a', 'b', 'b', 'c'], ['a', 'a', 'bb', 'c'], ['aa', 'b', 'b', 'c'], ['aa', 'bb', 'c']]