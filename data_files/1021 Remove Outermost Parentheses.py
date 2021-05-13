

from collections import deque


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        
        ret = []
        cnt = 0
        for e in S:
            if e == "(":
                cnt += 1
                if cnt > 1:
                    ret.append(e)
            else:
                cnt -= 1
                if cnt > 0:
                    ret.append(e)

        return "".join(ret)


    def removeOuterParentheses_error(self, S: str) -> str:
        
        ret = []
        stk = []
        cur_q = deque()
        for e in S:
            if e == "(":
                stk.append(e)
            else:
                prev = stk.pop()
                if stk:
                    cur_q.appendleft(prev)
                    cur_q.append(e)
                else:
                    ret.extend(cur_q)
                    cur_q = deque()

        return "".join(ret)


if __name__ == "__main__":
    assert Solution().removeOuterParentheses("(()())(())(()(()))") == "()()()()(())"
