

import string
import operator


class Solution:
    def characterReplacement(self, s, k):
        
        counter = {
            alphabet: 0
            for alphabet in string.ascii_uppercase
        }
        lo = 0
        ret = 0
        assert k > 0
        for hi in range(len(s)):
            counter[s[hi]] += 1
            while True:
                most = max(counter.values())  
                l = hi - lo + 1
                if l - most > k:
                    counter[s[lo]] -= 1
                    lo += 1
                else:
                    ret = max(ret, l)
                    break

        return ret


if __name__ == "__main__":
    assert Solution().characterReplacement("AABABBA", 1) == 4
    assert Solution().characterReplacement("ABAB", 2) == 4
