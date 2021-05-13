

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stk = []
        for e in asteroids:
            while stk and e < 0 < stk[-1]:
                if abs(e) > abs(stk[-1]):
                    
                    stk.pop()
                elif abs(e) == abs(stk[-1]):
                    
                    stk.pop()
                    break
                else:
                    
                    break
            else:
                stk.append(e)

        return stk

    def asteroidCollision_complex(self, asteroids: List[int]) -> List[int]:
        
        stk = []
        n = len(asteroids)
        for i in range(n-1, -1, -1):
            cur = asteroids[i]
            while stk and asteroids[stk[-1]] < 0 and cur > 0 and abs(asteroids[stk[-1]]) < abs(cur):
                stk.pop()

            if stk and cur > 0 and asteroids[stk[-1]] == -cur:
                stk.pop()
                continue

            if not stk:
                stk.append(i)
                continue

            if not (asteroids[stk[-1]] < 0 and cur > 0) or abs(cur) > abs(asteroids[stk[-1]]):
                stk.append(i)

        return [
            asteroids[i]
            for i in stk[::-1]
        ]


if __name__ == "__main__":
    assert Solution().asteroidCollision([10, 2, -5]) == [10]
    assert Solution().asteroidCollision([5, 10, -5]) == [5, 10]
    assert Solution().asteroidCollision([8, -8]) == []
