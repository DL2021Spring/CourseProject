
__author__ = 'Daniel'


class Solution:
    def evalRPN(self, tokens):
        
        return self.eval_postfix(tokens)

    def eval_postfix(self, post):
        stk = []
        for elt in post:
            if elt.strip("-").isdigit():
                stk.append(int(elt))
            else:
                b = stk.pop()
                a = stk.pop()
                if elt == "+":
                    stk.append(a+b)
                elif elt == "-":
                    stk.append(a-b)
                elif elt == "*":
                    stk.append(a*b)
                else:
                    stk.append(self.__div(a, b))  

        if stk:
            return stk[-1]
        return 0


    def __div(self, a, b):
        sign = 1
        if a*b < 0:
            sign = -1

        return abs(a)/abs(b)*sign