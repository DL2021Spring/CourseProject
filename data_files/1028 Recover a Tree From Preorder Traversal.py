




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import OrderedDict


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        
        depth = 0
        
        n = len(S)
        i = 0
        root = None
        stk = []
        while i < n:
            if S[i] == "-":
                depth += 1
                i += 1
            else:
                j = i
                while j < n and S[j] != "-":
                    j += 1

                val = int(S[i:j])

                
                cur = TreeNode(val)
                if depth == 0:
                    root = cur
                    stk = [(depth, root)]
                else:
                    assert stk
                    while stk[-1][0] != depth - 1:
                        stk.pop()

                    _, pi = stk[-1]
                    if not pi.left:
                        pi.left = cur
                    elif not pi.right:
                        pi.right = cur
                        stk.pop()
                    else:
                        raise
                    stk.append((depth, cur))

                depth = 0
                i = j

        return root

    def recoverFromPreorder_error(self, S: str) -> TreeNode:
        
        depth = 0
        depths = OrderedDict()
        
        n = len(S)
        i = 0
        while i < n:
            if S[i] == "-":
                depth += 1
                i += 1
            else:
                j = i
                while j < n and S[j] != "-":
                    j += 1

                val = int(S[i:j])
                depths[val] = depth
                depth = 0
                i = j

        
        stk = []
        root = None
        for k, v in depths.items():
            cur = TreeNode(k)
            if v == 0:
                root = cur
                stk = [root]
            else:
                assert stk
                while depths[stk[-1].val] != v - 1:
                    stk.pop()

                if not stk[-1].left:
                    stk[-1].left = cur
                elif not stk[-1].right:
                    stk[-1].right = cur
                    stk.pop()
                else:
                    raise
                stk.append(cur)

        return root


if __name__ == "__main__":
    assert Solution().recoverFromPreorder("5-4--4")
    assert Solution().recoverFromPreorder("1-2--3--4-5--6--7")
