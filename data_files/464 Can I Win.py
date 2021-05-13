



class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        
        cache = {}
        
        choices = frozenset([choice for choice in range(1, maxChoosableInteger + 1)])
        return self._can_win(desiredTotal, choices, sum(choices), cache)

    def _can_win(self, total, choices, gross,cache):
        if (total, choices) in cache:
            return cache[(total, choices)]

        ret = False
        if max(choices) >= total:
            ret = True

        elif gross < total:
            ret = False
        else:
            for choice in choices:
                if not self._can_win(
                        total - choice,
                        choices - set([choice]),
                        gross - choice,
                        cache
                ):
                    ret = True
                    break

        cache[(total, choices)] = ret
        return ret


if __name__ == "__main__":
    assert Solution().canIWin(10, 11) == False
    assert Solution().canIWin(10, 0) == True
    assert Solution().canIWin(13, 11) == True
