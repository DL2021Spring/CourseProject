



class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        return self.make_stk(S) == self.make_stk(T)

    def make_stk(self, S):
        stk = []
        for s in S:
            if s == "#":
                if stk:
                    stk.pop()
            else:
                stk.append(s)

        return stk
