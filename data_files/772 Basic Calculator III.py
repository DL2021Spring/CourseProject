



class Solution:
    def calculate(self, s: str) -> int:
        
        s = s + "\0"  
        ret, _ = self.eval(s, 0, [])
        return ret

    def eval(self, s, i, stk):
        
        operand = 0
        prev_op = "+"
        while i < len(s):
            c = s[i]
            if c == " ":
                pass  
            elif c.isdigit():
                operand = operand * 10 + int(c)
            elif c in ("+", "-", "*", "/", ")", "\0"):   
                if prev_op == "+":
                    stk.append(operand)
                elif prev_op == "-":
                    stk.append(-operand)
                elif prev_op == "*":
                    prev_operand = stk.pop()
                    stk.append(prev_operand * operand)
                elif prev_op == "/":
                    prev_operand = stk.pop()
                    stk.append(int(prev_operand / operand))

                if c in ("+", "-", "*", "/"):
                    operand = 0
                    prev_op = c
                elif c in (")", "\0"):
                    return sum(stk), i
            elif c == "(":  
                operand, i = self.eval(s, i + 1, [])
            else:
                raise

            i += 1


if __name__ == "__main__":
    assert Solution().calculate("(( ( ( 4- 2)+ ( 6+ 10 ) )+ 1) /( ( ( 7 + 9 )* ( 5*8) )- ( 5 + ( 2 * 10 ) ) ) )") == 0
    assert Solution().calculate("(2+6* 3+5- (3*14/7+2)*5)+3") == -12
