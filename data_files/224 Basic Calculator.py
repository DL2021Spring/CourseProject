
__author__ = 'Daniel'


class Solution:
    def calculate(self, s):
        
        lst = self.to_list(s)
        postfix = self.infix2postfix(lst)
        return self.eval_postfix(postfix)

    def to_list(self, s):
        i = 0
        ret = []
        while i < len(s):
            if s[i] == " ":
                i += 1

            elif s[i] in ("(", ")", "+", "-"):
                ret.append(s[i])
                i += 1

            else:
                b = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                ret.append(s[b:i])

        return ret

    def infix2postfix(self, lst):
        stk = []  
        ret = []
        for elt in lst:
            if elt.isdigit():
                ret.append(elt)
            elif elt == "(":
                stk.append(elt)
            elif elt == ")":
                while stk[-1] != "(":
                    ret.append(stk.pop())
                stk.pop()
            else:  
                while stk and self.precendece(elt) <= self.precendece(stk[-1]):
                    ret.append(stk.pop())

                stk.append(elt)

        while stk:
            ret.append(stk.pop())

        return ret

    def precendece(self, op):
        if op in ("(", ")"):
            return 0
        if op in ("+", "-"):
            return 1

    def eval_postfix(self, post):
        stk = []
        for elt in post:
            if elt in ("+", "-"):
                b = int(stk.pop())
                a = int(stk.pop())
                if elt == "+":
                    stk.append(a+b)
                else:
                    stk.append(a-b)
            else:
                stk.append(elt)

        assert len(stk) == 1
        return int(stk[-1])


if __name__ == "__main__":
    assert Solution().calculate(" 2-1 + 2 ") == 3
    assert Solution().calculate("(1+(4+5+2)-3)+(6+8)") == 23