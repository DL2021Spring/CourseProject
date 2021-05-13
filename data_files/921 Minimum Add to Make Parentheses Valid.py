



class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        
        ret = 0
        stk = []
        for s in S:
            if s == "(":
                stk.append(s)
            else:
                if stk:
                    stk.pop()
                else:
                    ret += 1

        ret += len(stk)
        return ret
