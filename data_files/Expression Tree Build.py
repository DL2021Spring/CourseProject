
__author__ = 'Daniel'


class ExpressionTreeNode:
    def __init__(self, symbol):
        self.symbol = symbol
        self.left, self.right = None, None


class Solution:
    def build(self, expression):
        
        post = self.infix2postfix(expression)
        tree_node = self.postfix2tree(post)
        return tree_node

    def infix2postfix(self, expression):
        
        post = []
        op_stk = []
        for elt in expression:
            if elt.isdigit():
                post.append(elt)
            elif elt == "(":
                op_stk.append(elt)
            elif elt == ")":
                while op_stk and op_stk[-1] != "(":
                    post.append(op_stk.pop())
                op_stk.pop()
            else:
                while op_stk and self.precedence(op_stk[-1]) >= self.precedence(
                        elt):  
                    post.append(op_stk.pop())
                op_stk.append(elt)

        while op_stk:
            post.append(op_stk.pop())

        return post

    def postfix2tree(self, post):
        tree_stk = []
        for elt in post:
            if elt.isdigit():
                tree_stk.append(ExpressionTreeNode(elt))
            else:
                pi = ExpressionTreeNode(elt)
                pi.right = tree_stk.pop()
                pi.left = tree_stk.pop()
                tree_stk.append(pi)

        try:
            return tree_stk.pop()
        except IndexError:
            return None

    def precedence(self, elt):
        if elt in ("(", ")"):
            return 0
        if elt in ("+", "-"):
            return 1
        if elt in ("*", "/"):
            return 2
        return 3


if __name__ == "__main__":
    tree_ndoe = Solution().build(["2", "*", "6", "-", "(", "23", "+", "7", ")", "/", "(", "1", "+", "2", ")"])
    assert tree_ndoe.symbol == "-