

import bisect


class MyCalendarThree:

    def __init__(self):
        self.lst = []

    def book(self, start: int, end: int) -> int:
        bisect.insort(self.lst, (start, "start"))
        bisect.insort(self.lst, (end, "end"))
        ret = 0
        count = 0
        for _, flag in self.lst:
            count += 1 if flag == "start" else -1
            ret = max(ret, count)

        return ret





