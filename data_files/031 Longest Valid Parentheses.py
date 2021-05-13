
__author__ = 'Danyang'


class Solution(object):
    def longestValidParentheses(self, s):
        
        stk = []  
        maxa = 0
        for idx, val in enumerate(s):
            if val == ")" and stk and s[stk[-1]] == "(":
                stk.pop()
                if not stk:
                    maxa = max(maxa, idx+1)
                else:
                    maxa = max(maxa, idx-stk[-1])
            else:
                stk.append(idx)

        return maxa


if __name__ == "__main__":
    assert Solution().longestValidParentheses("(()()") == 4
    assert Solution().longestValidParentheses("()(()") == 2
    assert Solution().longestValidParentheses("(()") == 2
    assert Solution().longestValidParentheses(")()())") == 4