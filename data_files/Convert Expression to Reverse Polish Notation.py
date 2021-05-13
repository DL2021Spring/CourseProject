
__author__ = 'Daniel'


class Solution(object):
    def convertToRPN(self, expression):
        
        return self.infix2postfix(expression)

    def infix2postfix(self, lst):
        
        stk = []
        ret = []  
        for elt in lst:
            if elt.isdigit():
                ret.append(elt)
            elif elt == "(":
                stk.append(elt)
            elif elt == ")":
                while stk and stk[-1] != "(":
                    ret.append(stk.pop())
                stk.pop()  
            else:
                while stk and self.precedence(elt) <= self.precedence(stk[-1]):
                    ret.append(stk.pop())
                stk.append(elt)

        while stk:  
            ret.append(stk.pop())

        return ret

    def precedence(self, x):
        if x in ("(", ")"):
            return 0
        if x in ("+", "-"):
            return 1
        if x in ("*", "/"):
            return 2
        return 3

if __name__ == "__main__":
    print Solution().infix2postfix(["3", "-", "4", "+", "5"])