
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        
        st = 0  
        counter = defaultdict(int)
        maxa = 0
        for idx, val in enumerate(s):
            if counter[val] == 0:
                k -= 1

            counter[val] += 1
            while k < 0:
                counter[s[st]] -= 1
                if counter[s[st]] == 0:
                    k += 1
                st += 1

            maxa = max(maxa, idx - st + 1)

        return maxa


if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstringKDistinct("eceba", 2) == 3
