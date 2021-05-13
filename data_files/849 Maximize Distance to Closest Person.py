

from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        n = len(seats)
        L = [float("inf") for _ in range(n)]
        R = [float("inf") for _ in range(n)]
        for i in range(n):
            if seats[i] == 1:
                L[i] = 0
            elif i - 1 >= 0:
                L[i] = L[i-1] + 1
        for i in range(n-1, -1 , -1):
            if seats[i] == 1:
                R[i] = 0
            elif i + 1 < n:
                R[i] = R[i+1] + 1

        return max(
            min(L[i], R[i])
            for i in range(n)
        )

    def maxDistToClosest2(self, seats: List[int]) -> int:
        
        idxes = []
        for i, e in enumerate(seats):
            if e == 1:
                idxes.append(i)

        ret = [-float("inf"), 0]
        n = len(seats)
        
        for i, j in zip((0, n-1), (0, -1)):
            dist = abs(i - idxes[j])
            if dist > ret[0]:
                ret = [dist, i]

        for j in range(len(idxes) - 1):
            i = (idxes[j] + idxes[j+1]) // 2
            dist = min(abs(i - idxes[j]), abs(i - idxes[j+1]))
            if dist > ret[0]:
                ret = [dist, i]

        return ret[0]


if __name__ == "__main__":
    assert Solution().maxDistToClosest([1,0,0,0,1,0,1]) == 2
