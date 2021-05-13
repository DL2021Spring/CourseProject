
__author__ = 'Danyang'


class Solution:
    def isMatch_error(self, s, p):
        
        
        tape = s
        regex = p

        index = 0
        state = 0
        while index < len(tape) and state < len(regex):
            char = tape[index]
            if state+1 < len(regex) and regex[state+1] == "*":
                if regex[state] != ".":
                    if char == regex[state]:  
                        while index < len(tape) and tape[index] == char: index += 1
                        state += 2
                    else:
                        state += 2
                else:  
                    state += 2
                    if state < len(regex):
                        if regex[state] != ".":  
                            while index < len(tape) and tape[index] != regex[state]: index += 1
                        else:  
                            count = 1

                    else:
                        return True
            else:  
                if char == regex[state] or regex[state] == ".":
                    index += 1
                    state += 1
                else:
                    break

        if index == len(tape) and state == len(regex):
            return True
        return False


    def isMatch_TLE(self, s, p):
        
        
        tape = s
        regex = p

        index = 0
        state = 0

        
        if not tape and not regex:
            return True
        
        if tape and not regex:  
            return False

        if not tape and regex:
            if state+1 < len(regex) and regex[state+1] == "*":
                return self.isMatch(tape, regex[state+2:])
            else:
                return False

        if state+1 < len(regex) and regex[state+1] == "*":
            if tape[index] == regex[state] or regex[state] == ".":  
                return self.isMatch(tape[index+1:], regex[state:]) or \
                       self.isMatch(tape[index+1:], regex[state+2:]) or \
                       self.isMatch(tape[index:], regex[state+2:])
            else:
                return self.isMatch(tape[index:], regex[state+2:])
        else:  
            if tape[index] == regex[state] or regex[state] == ".":
                return self.isMatch(tape[index+1:], regex[state+1:])
            else:
                return False

    def isMatch(self, s, p):
        
        
        tape = s
        regex = p

        m = len(tape)
        n = len(regex)

        dp = [[False for _ in xrange(n+1)] for _ in xrange(m+1)]

        
        dp[m][n] = True
        for j in xrange(n-1, -1, -1):
            if regex[j] == "*":
                dp[m][j] = dp[m][j+1]
            elif j+1 < n and regex[j+1] == "*":
                dp[m][j] = dp[m][j+1]
            else:
                dp[m][j] = False

        
        for i in xrange(m-1, -1, -1):
            for j in xrange(n-1, -1, -1):
                if regex[j] == "*":
                    if j-1 >= 0 and regex[j-1] != "*":
                        dp[i][j] = dp[i][j+1]  
                    else:
                        return False  
                elif j+1 < n and regex[j+1] == "*":
                    if tape[i] == regex[j] or regex[j] == ".":
                        dp[i][j] = dp[i][j+2] or dp[i+1][j] or dp[i+1][j+2]  
                    else:
                        dp[i][j] = dp[i][j+2]
                else:
                    if tape[i] == regex[j] or regex[j] == ".":
                        dp[i][j] = dp[i+1][j+1]
                    else:
                        dp[i][j] = False

        

        return dp[0][0]


if __name__ == "__main__":
    assert Solution().isMatch("aa", "a") == False
    assert Solution().isMatch("aa", "aa") == True
    assert Solution().isMatch("aaa", "aa") == False
    assert Solution().isMatch("aa", "a*") == True
    assert Solution().isMatch("ab", ".*") == True
    assert Solution().isMatch("aab", "c*a*b") == True
    assert Solution().isMatch("aaa", "a*a") == True
    assert Solution().isMatch("bbbba", ".*a*a") == True
    assert Solution().isMatch("a", "aa*") == True