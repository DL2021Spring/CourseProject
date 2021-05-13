

import bisect
from collections import defaultdict


class TimeMap:

    def __init__(self):
        
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        n = (timestamp, value)
        bisect.insort(self.m[key], n)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""

        
        lst = self.m[key]
        i = bisect.bisect(lst, (timestamp, ""))
        if i < len(lst) and lst[i][0] == timestamp:
            return lst[i][1]
        i -= 1
        if i >= 0:
            return lst[i][1]
            
        return ""






