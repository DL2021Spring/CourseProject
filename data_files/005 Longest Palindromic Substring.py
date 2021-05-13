
__author__ = 'Danyang'


class Solution(object):
    def longestPalindrome(self, s):
        
        if not s:
            return
        n = len(s)
        if n == 1:
            return s

        ret = s[0]
        for i in xrange(0, n):
            cur = self.get_palindrome_from_center(s, i, i)  
            if len(cur) > len(ret): ret = cur
            cur = self.get_palindrome_from_center(s, i, i+1)
            if len(cur) > len(ret): ret = cur
        return ret

    def longestPalindrome_TLE(self, s):
        
        length = len(s)
        dp = [[False for _ in xrange(length+1)] for _ in xrange(length+1)]
        for i in xrange(length+1):
            dp[i][i] = True

        longest = [0, 0]
        for j in xrange(length+1):
            for i in xrange(j-1, -1, -1):
                if i+1 == j:
                    dp[i][j] = True
                else:
                    dp[i][j] = s[i] == s[j-1] and dp[i+1][j-1]  

                if dp[i][j] == True and longest[1]-longest[0] < j-i:
                    longest[0], longest[1] = i, j

        return s[longest[0]:longest[1]]

    def longestPalindrome_TLE2(self, s):
        
        length = len(s)

        longest = ""
        dp = [[False for _ in xrange(length+1)] for _ in xrange(length+1)]  
        for i in xrange(length+1):
            dp[i][i] = True  
        for i in xrange(length):
            dp[i][i+1] = True  
        for i in xrange(length-1):
            dp[i][i+2] = s[i] == s[i+1]
            if dp[i][i+1]:
                longest = s[i:i+2]

        for l in xrange(3, length+1):  
            for i in xrange(0, length-l):
                if s[i] == s[i+l-1]:
                    dp[i][i+l] = dp[i+1][i+l-1]
                else:
                    dp[i][i+l] = False

                if dp[i][i+l] and len(longest) < l:
                    longest = s[i:i+l]

        return longest

    def get_palindrome_from_center(self, s, begin, end):
        
        while begin >= 0 and end < len(s) and s[begin] == s[end]:
            begin -= 1
            end += 1

        return s[begin+1: end-1+1]


if __name__ == "__main__":
    assert Solution().longestPalindrome("dfaaabbbaaac") == "aaabbbaaa