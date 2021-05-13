

from collections import deque


class Solution:
    def baseNeg2(self, N: int) -> str:
        
        ret = deque()
        while N != 0:
            r = N % 2  
            ret.appendleft(r)
            N -= r
            N //= -2

        return "".join(map(str, ret)) or "0"


if __name__ == "__main__":
    assert Solution().baseNeg2(3) == "111"
    assert Solution().baseNeg2(4) == "100"
