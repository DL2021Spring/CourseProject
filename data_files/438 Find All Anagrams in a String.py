

from collections import Counter


class Solution:
    def findAnagrams(self, s, target):
        
        ret = []
        counter_target = Counter(target)
        counter_cur = Counter(s[:len(target)])
        if counter_cur == counter_target:
            ret.append(0)

        for idx in range(len(target), len(s)):
            head = s[idx - len(target)]
            tail = s[idx]
            counter_cur[tail] += 1
            counter_cur[head] -= 1
            if counter_cur[head] == 0:
                del counter_cur[head]  
            if counter_cur == counter_target:
                
                ret.append(idx - len(target) + 1)

        return ret


if __name__ == "__main__":
    assert Solution().findAnagrams("cbaebabacd", "abc") == [0, 6]
