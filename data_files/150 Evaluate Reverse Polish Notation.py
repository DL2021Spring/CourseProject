__author__ = 'Danyang'


class Solution(object):
    def evalRPN(self, tokens):
        
        ops = ["+", "-", "*", "/"]

        def arith(a, b, op):
            if (op == "+"):
                return a+b
            if (op == "-"):
                return a-b
            if (op == "/"):
                
                return int(float(a)/b)  
            if (op == "*"):
                return a*b

        
        
        
        
        
        
        
        
        
        
        
        

        
        stack = []
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = arith(arg1, arg2, token)
                stack.append(result)
        return stack.pop()


if __name__ == "__main__":
    assert Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22