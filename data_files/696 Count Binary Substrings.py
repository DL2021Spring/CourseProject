



class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        cur = 1  
        prev = 0
        ret = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                prev = cur
                cur = 1
            if prev >= cur:
                ret += 1

        return ret

    def countBinarySubstrings_error(self, s: str) -> int:
        
        counter = {"0": 0, "1": 0}
        ret = 0
        if not s:
            return ret
        counter[s[0]] += 1
        for i in range(1, len(s)):
            if s[i] != s[i-1] and counter[s[i]] != 0:
                counter[s[i]] = 0

            counter[s[i]] += 1
            if min(counter["0"], counter["1"]) > 0:
                ret += 1

        return ret


if __name__ == "__main__":
    assert Solution().countBinarySubstrings("00110011") == 6
    assert Solution().countBinarySubstrings("00110") == 3
