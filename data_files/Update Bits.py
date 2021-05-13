
__author__ = 'Danyang'


class Solution:
    def updateBits(self, n, m, i, j):
        
        mask = ((1<<32)-1)-((1<<j+1)-1)+((1<<i)-1)
        ret = (n&mask)+(m<<i)
        return self.twos_comp(ret, 32)

    @staticmethod
    def twos_comp(val, bits):
        
        if val > 0 and val&(1<<(bits-1)) != 0:  
            val -= 1<<bits
        return val


if __name__ == "__main__":
    assert Solution().updateBits(-2147483648, 2147483647, 0, 30) == -1
    assert Solution().updateBits(1, -1, 0, 31) == -1
    n = int("10000000000", 2)
    m = int("10101", 2)
    assert bin(Solution().updateBits(n, m, 2, 6)) == "0b10001010100"

