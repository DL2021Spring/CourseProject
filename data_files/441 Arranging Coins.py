



class Solution:
    def arrangeCoins(self, n):
        
        return int(
            (2*n + 1/4)**(1/2)  - 1/2
        )


if __name__ == "__main__":
    assert Solution().arrangeCoins(5) == 2
    assert Solution().arrangeCoins(8) == 3
