



class Solution:
    def countSegments(self, s):
        
        ret = 0
        if not s:
            return ret

        
        if s[0] != " ":
            ret = 1
        prev = s[0]
        for c in s[1:]:
            if c != " " and prev == " ":
                ret += 1
            prev = c
        return ret


if __name__ == "__main__":
    assert Solution().countSegments("Hello, my name is John") == 5
