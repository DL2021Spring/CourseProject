

from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        counter = defaultdict(int)
        s1_set = set(s1)
        for c in s1:
            counter[c] += 1

        i = 0
        j = 0
        while j < len(s2):
            if counter[s2[j]] > 0:
                counter[s2[j]] -= 1
                if j - i + 1 == len(s1):
                    return True
                j += 1
            else:
                if s2[i] in s1_set:
                    
                    counter[s2[i]] += 1
                i += 1
                if j < i:
                    j = i

        return False


if __name__ == "__main__":
    assert Solution().checkInclusion("ab", "eidbaooo") == True
    assert Solution().checkInclusion("ab", "eidboaoo") == False
