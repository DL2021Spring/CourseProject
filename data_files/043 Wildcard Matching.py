
__author__ = 'Danyang'
class Solution:
    def isMatch_MLE(self, s, p):
        
        tape = s
        pattern = p

        m = len(tape)
        n = len(pattern)
        dp = [[False for _ in xrange(n+1)] for _ in xrange(m+1)]
        
        dp[m][n] = True
        for j in xrange(n-1, -1 , -1):
            if pattern[j]=="*":
                dp[m][j] = dp[m][j+1]

        
        for i in xrange(m-1, -1, -1):
            for j in xrange(n-1, -1, -1):
                if tape[i]==pattern[j] or pattern[j]=="?":
                    dp[i][j] = dp[i+1][j+1]
                elif pattern[j]=="*":
                    dp[i][j] = dp[i][j+1] or dp[i+1][j]  
                else:
                    dp[i][j] = False


        return dp[0][0]

    def isMatch_forward(self, s, p):
        
        tape = s
        pattern = p

        m = len(tape)
        n = len(pattern)

        if n - list(pattern).count("*") > m:
            return False

        dp = [False for _ in xrange(m+1)]
        dp[0] = True  
        for j in xrange(1, n+1):
            if pattern[j-1]=="*":
                
                
                k = 0
                while k<m+1 and dp[k]!=True: k+= 1
                for i in xrange(k, m+1):
                    dp[i] = True
            else:
                for i in xrange(m, 0, -1):
                    dp[i] = dp[i-1] and (tape[i-1]==pattern[j-1] or pattern[j-1]=="?")

            dp[0] = dp[0] and pattern[j-1]=="*"  


        return dp[m]

if __name__=="__main__":
    assert Solution().isMatch("aab", "c*a*b")==False
    assert Solution().isMatch("aa","a")==False
    assert Solution().isMatch("aa", "aa")==True
    assert Solution().isMatch("aaa", "aa")==False
    assert Solution().isMatch("aaa", "*")==True
    assert Solution().isMatch("aa", "a*")==True
    assert Solution().isMatch("ab", "?*")==True
