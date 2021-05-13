
import sys

__author__ = 'Daniel'


class Solution(object):
    def coinChange(self, coins, amount):
        
        if amount == 0:
            return 0

        F = [sys.maxint for _ in xrange(amount+1)]
        for k in coins:
            if k < amount+1:
                F[k] = 1

        for i in xrange(1, amount+1):
            if F[i] != sys.maxint:
                for k in coins:
                    if i+k <= amount:
                        F[i+k] = min(F[i+k], F[i]+1)

        return F[amount] if F[amount] != sys.maxint else -1


class SolutionTLE(object):
    def coinChange(self, coins, amount):
        
        F = [sys.maxint for _ in xrange(amount+1)]
        for k in coins:
            if k < amount + 1:
                F[k] = 1

        for i in xrange(1, amount+1):
            for k in coins:
                if i-k > 0 and F[i-k] != sys.maxint:
                    F[i] = min(F[i], F[i-k]+1)

        return F[amount] if F[amount] != sys.maxint else -1


if __name__ == "__main__":
    assert Solution().coinChange([243, 291, 335, 209, 177, 345, 114, 91, 313, 331], 7367) == 23