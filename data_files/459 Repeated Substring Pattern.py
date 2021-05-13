



class Solution:
    def repeatedSubstringPattern(self, s):
        
        return s in (s + s)[1:-1]

    def repeatedSubstringPattern_error(self, s):
        
        if not s:
            return False
        p1 = 0
        e = 1  
        p2 = 1
        while p2 < len(s):
            if s[p1] == s[p2]:
                p1 += 1
                if p1 == e:
                    p1 = 0
            else:
                p1 = 0
                e = p2 + 1

            p2 += 1

        return p2 == len(s) and p1 == 0 and e != len(s)


if __name__ == "__main__":
    assert Solution().repeatedSubstringPattern("abab") == True
    assert Solution().repeatedSubstringPattern("abcd") == False
    assert Solution().repeatedSubstringPattern("abacababacab") == True
