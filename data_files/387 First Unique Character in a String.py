
__author__ = 'Daniel'


class Solution(object):
    def firstUniqChar(self, s):
        
        if not s:
            return -1

        first = {}
        for i, v in enumerate(list(s)):
            if v not in first:
                first[v] = i
            else:
                first[v] = -1

        lst = filter(lambda x: x != -1, first.values())
        return min(lst) if lst else -1


if __name__ == "__main__":
    assert Solution().firstUniqChar("leetcode") == 0