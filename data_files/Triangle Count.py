
__author__ = 'Daniel'


class Solution:
    def triangleCount(self, S):
        
        S.sort()
        cnt = 0
        for h in xrange(len(S)-1, 1, -1):
            s = 0
            e = h-1
            while s<e:
                if S[s]+S[e]>S[h]:
                    cnt += e-s
                    e -= 1
                else:
                    s += 1

        return cnt

if __name__ == "__main__":
    assert Solution().triangleCount([3, 4, 6, 7]) == 3