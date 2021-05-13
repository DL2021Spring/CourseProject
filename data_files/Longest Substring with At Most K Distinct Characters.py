
__author__ = 'Daniel'


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        
        if len(s)<1 or k<1:
            return 0

        cnt = {}
        b = 0
        e = 1
        cnt[s[b]] = 1
        maxa = 1
        while e<len(s):
            
            if s[e] not in cnt:
                cnt[s[e]] = 0
            cnt[s[e]] += 1
            e += 1

            
            while len(cnt)>k:
                cnt[s[b]] -= 1
                if cnt[s[b]]<=0:
                    del cnt[s[b]]
                b += 1

            maxa = max(maxa, e-b)

        return maxa

if __name__=="__main__":
    assert Solution().lengthOfLongestSubstringKDistinct("eceba", 3)==4
