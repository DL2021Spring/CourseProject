

from typing import List
from collections import deque


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        ret = deque()
        stk = []
        for i in range(len(T) - 1, -1 , -1):
            while stk and T[stk[-1]] <= T[i]:  
                stk.pop()

            if stk:
                ret.appendleft(stk[-1] - i)
            else:
                ret.appendleft(0)
            stk.append(i)

        return list(ret)


if __name__ == "__main__":
    assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
