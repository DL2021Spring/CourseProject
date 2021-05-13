
__author__ = 'Daniel'


class Solution(object):
    def removeInvalidParentheses(self, s):
        
        rmcnt = self.minrm(s)
        ret = []
        self.dfs(s, "", 0, None, 0, rmcnt, ret)
        return ret

    def minrm(self, s):
        
        rmcnt = 0
        left = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left > 0:
                    left -= 1
                else:
                    rmcnt += 1

        rmcnt += left
        return rmcnt

    def dfs(self, s, cur, left, pi, i, rmcnt, ret):
        
        if left < 0 or rmcnt < 0 or i > len(s):
            return
        if i == len(s):
            if rmcnt == 0 and left == 0:
                ret.append(cur)
            return

        if s[i] not in ("(", ")"):  
            self.dfs(s, cur+s[i], left, None, i+1, rmcnt, ret)
        else:
            if pi == s[i]:  
                while i < len(s) and pi and pi == s[i]: i, rmcnt = i+1, rmcnt-1
                self.dfs(s, cur, left, pi, i, rmcnt, ret)
            else:
                self.dfs(s, cur, left, s[i], i+1, rmcnt-1, ret)
                L = left+1 if s[i] == "(" else left-1  
                self.dfs(s, cur+s[i], L, None, i+1, rmcnt, ret)  


if __name__ == "__main__":
    assert Solution().removeInvalidParentheses("(a)())()") == ['(a())()', '(a)()()']
