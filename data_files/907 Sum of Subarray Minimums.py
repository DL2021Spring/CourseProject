

from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        
        n = len(A)
        L = [-1 for _ in A]
        R = [n for _ in A]

        stk = []
        for i in range(n):
            while stk and A[stk[-1]] >= A[i]:
                stk.pop()

            if stk:
                L[i] = stk[-1]
            stk.append(i)

        stk = []
        for i in range(n-1, -1, -1):
            
            while stk and A[stk[-1]] > A[i]:
                stk.pop()

            if stk:
                R[i] = stk[-1]
            stk.append(i)

        ret = 0
        for i in range(n):
            ret += (
                A[i] * (i - L[i]) * (R[i] - i)
            )
            ret %= MOD

        return ret


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        
        stk = []
        A = [-float('inf')] + A + [-float('inf')]
        ret = 0
        for i, a in enumerate(A):
            while stk and A[stk[-1]] > a:
                h = stk.pop()
                
                ret += A[h] * (h - stk[-1]) * (i - h)
                ret %= MOD

            stk.append(i)
        return ret


if __name__ == "__main__":
    assert Solution().sumSubarrayMins([71,55,82,55]) == 593
    assert Solution().sumSubarrayMins([3,1,2,4]) == 17
