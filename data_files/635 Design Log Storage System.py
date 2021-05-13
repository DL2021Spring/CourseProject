

import bisect


class LogSystem:
    def __init__(self):
        
        self.lst = []

    def put(self, id: int, timestamp: str) -> None:
        bisect.insort(self.lst, (timestamp, id))

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        
        lo = "0001:01:01:00:00:00"
        hi = "9999:12:31:23:59:59"
        pre = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19,
        }[gra]

        s = s[:pre] + lo[pre:]
        e = e[:pre] + hi[pre:]
        i = bisect.bisect_left(self.lst, (s, 0))
        j = bisect.bisect_right(self.lst, (e, float("inf")))
        return [id for _, id in self.lst[i:j]]






