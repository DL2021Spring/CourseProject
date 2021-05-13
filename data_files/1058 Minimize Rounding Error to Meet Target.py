

from typing import List
import math


class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        
        A = list(map(float, prices))
        f_sum = sum(map(math.floor, A))
        c_sum = sum(map(math.ceil, A))
        if not f_sum <= target <= c_sum:
            return "-1"

        errors = [
            e - math.floor(e)
            for e in A
        ]
        errors.sort(reverse=True)
        ret = 0
        remain = target - f_sum
        for err in errors:
            if remain > 0:
                ret += 1 - err
                remain -= 1
            else:
                ret += err

        return f'{ret:.{3}f}'
