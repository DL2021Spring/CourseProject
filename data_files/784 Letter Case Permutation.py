

from typing import List


class Solution:
    def __init__(self):
        self.ret = []

    def letterCasePermutation(self, S: str) -> List[str]:
        
        
        S_lst = list(S)
        self.dfs([], S_lst, 0)
        return [
            "".join(e)
            for e in self.ret
        ]

    def dfs(self, lst, S_lst, i):
        if len(lst) == len(S_lst):
            self.ret.append(list(lst))
            return

        if S_lst[i].isdigit():
            lst.append(S_lst[i])
            self.dfs(lst, S_lst, i + 1)
            lst.pop()
        else:
            lst.append(S_lst[i].lower())
            self.dfs(lst, S_lst, i + 1)
            lst.pop()
            lst.append(S_lst[i].upper())
            self.dfs(lst, S_lst, i + 1)
            lst.pop()


if __name__ == "__main__":
    assert Solution().letterCasePermutation("a1b2") == ['a1b2', 'a1B2', 'A1b2', 'A1B2']
