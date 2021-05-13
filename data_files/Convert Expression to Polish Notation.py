
__author__ = 'Daniel'


class Solution:
    def convertToPN(self, expression):
        
        return self.infix2prefix(expression)

    def infix2prefix(self, lst):
        
        stk = []
        pre = []
        for elt in reversed(lst):
            if elt.isdigit():
                pre.append(elt)
            elif elt == ")":
                stk.append(elt)
            elif elt == "(":
                while stk and stk[-1] != ")":
                    pre.append(stk.pop())
                stk.pop()
            else:
                while stk and self.precedence(elt) < self.precedence(stk[-1]):  
                    pre.append(stk.pop())
                stk.append(elt)

        while stk:
            pre.append(stk.pop())

        pre.reverse()
        return pre

    def precedence(self, x):
        if x in ("(", ")"):
            return 0
        if x in ("+", "-"):
            return 1
        if x in ("*", "/"):
            return 2
        return 3


if __name__ == "__main__":
    assert Solution().infix2prefix(["(", "5", "-", "6", ")", "*", "7"]) == ['*', '-', '5', '6', '7']