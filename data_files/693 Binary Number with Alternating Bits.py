



class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last = None
        while n:
            cur = n & 1
            
            if last is not None and last ^ cur == 0:
                return False
            last = cur
            n >>= 1

        return True


if __name__ == "__main__":
    assert Solution().hasAlternatingBits(5) == True
    assert Solution().hasAlternatingBits(7) == False
