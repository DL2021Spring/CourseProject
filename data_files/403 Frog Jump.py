
__author__ = 'Daniel'


class Solution(object):
    def canCross(self, stones):
        
        F = {}
        for stone in stones:
            F[stone] = set()

        F[0].add(0)
        for stone in stones:
            for step in F[stone]:
                for i in (-1, 0, 1):
                    nxt = stone + step + i
                    if nxt != stone and nxt in F:
                        F[nxt].add(step + i)

        return True if F[stones[-1]] else False


if __name__ == "__main__":
    assert Solution().canCross([0, 2]) == False
    assert Solution().canCross([0, 1, 3, 5, 6, 8, 12, 17]) == True
    assert Solution().canCross([0, 1, 2, 3, 4, 8, 9, 11]) == False
