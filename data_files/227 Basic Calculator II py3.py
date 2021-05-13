



class Solution:
    def calculate(self, s: str) -> int:
        
        operand = 0
        stk = []
        prev_op = "+"
        for i, c in enumerate(s):
            if c.isdigit():
                operand = operand * 10 + int(c)

            
            delimited = c in ("+", "-", "*", "/") or i == len(s) - 1
            if delimited:
                if prev_op == "+":
                    cur = operand
                elif prev_op == "-":
                    cur = -operand
                elif prev_op == "*":
                    cur = stk.pop() * operand
                else:
                    assert prev_op == "/"
                    
                    cur = int(stk.pop() / operand)

                stk.append(cur)
                prev_op = c
                operand = 0

        return sum(stk)

    def calculate_error(self, s: str) -> int:
        
        operand = 0
        stk = []
        prev_op = "+"
        for i, c in enumerate(s):
            if c.isdigit():
                operand = operand * 10 + int(c)

            
            delimited = c in ("+", "-", "*", "/") or i == len(s) - 1
            if delimited:
                cur = {
                    "+": operand,
                    "-": -operand,
                    "*": stk.pop() * operand,
                    "/": int(stk.pop() / operand),  
                }[prev_op]
                stk.append(cur)

                prev_op = c
                operand = 0

        return sum(stk)


if __name__ == "__main__":
    assert Solution().calculate("3+2*2") == 7
