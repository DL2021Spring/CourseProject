



class Solution:
    def findContentChildren(self, g, s):
        
        g.sort()
        s.sort()
        ret = 0
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                ret += 1
                i += 1
                j += 1
            else:
                j += 1

        return ret


if __name__ == "__main__":
    assert Solution().findContentChildren([10,9,8,7], [5,6,7,8]) == 2
