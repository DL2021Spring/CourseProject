
__author__ = 'Danyang'
class Solution:
    def generateParenthesis(self, n):
        
        result = []
        self.generateParenthesisDfs(result, "", n, n)
        return result

    def generateParenthesisDfs(self, result, cur, left, right):
        
        if left == 0 and right == 0:
            result.append(cur)
            return

        
        if left > 0:
            self.generateParenthesisDfs(result, cur + "(", left - 1, right)
        
        if right > left:
            self.generateParenthesisDfs(result, cur + ")", left, right - 1)


if __name__=="__main__":
    assert Solution().generateParenthesis(3)==['((()))', '(()())', '(())()', '()(())', '()()()']
