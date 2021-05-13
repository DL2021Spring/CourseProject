



class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        
        stk = []
        ret = 0
        for s in S:
            if s == "(":
                stk.append(0)
            else:
                cur = stk.pop()
                score = max(2 * cur, 1)
                if stk:
                    stk[-1] += score
                else:
                    ret += score

        return ret

    def scoreOfParentheses_error(self, S: str) -> int:
        
        ret = 0
        cur_stk = []
        for s in S:
            if s == "(":
                cur_stk.append(0)
                stk.append(s)
            else:
                stk.pop()
                if cur_stk[-1] == 0:
                    cur_stk[-1] = 1
                else:
                    cur_stk[-1] *= 2
            if not stk:
                ret += cur
                cur = 0

        return ret


if __name__ == "__main__":
    assert Solution().scoreOfParentheses("(())") == 2
    assert Solution().scoreOfParentheses("(()(()))") == 6
