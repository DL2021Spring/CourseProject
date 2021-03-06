

from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        
        ret, _ = self.eval(s + "\0", 0, [])
        return ret

    def eval(self, s: str, start: int, stk: List[int]) -> int:
        prev_op = "+"
        operand = 0
        i = start
        while i < len(s):  
            if s[i] == " ":
                pass
            elif s[i].isdigit():
                operand = operand * 10 + int(s[i])
            elif s[i] in ("+", "-", ")", "\0"):  
                if prev_op == "+":
                    stk.append(operand)
                elif prev_op == "-":
                    stk.append(-operand)
        
                if s[i] in ("+", "-"):
                    operand = 0
                    prev_op = s[i]
                elif s[i] in (")", "\0"):
                    return sum(stk), i
            elif s[i] == "(":
                
                operand, i = self.eval(s, i + 1, [])
            else:
                raise

            i += 1


if __name__ == "__main__":
    assert Solution().calculate("(1+(4+5+2)-3)+(6+8)") == 23
