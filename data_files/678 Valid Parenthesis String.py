



class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stk_left = []
        stk_star = []
        for i, c in enumerate(s):
            if c == "(":
                stk_left.append(i)
            elif c == "*":
                stk_star.append(i)
            else:
                if stk_left:
                    stk_left.pop()
                elif stk_star:
                    stk_star.pop()
                else:
                    return False

        while stk_left and stk_star and stk_star[-1] > stk_left[-1]:
            stk_star.pop()
            stk_left.pop()

        return not stk_left


if __name__ == "__main__":
    assert Solution().checkValidString("(*))") == True
    assert Solution().checkValidString("*(") == False
    assert Solution().checkValidString("(*)") == True
