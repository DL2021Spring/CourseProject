

import bisect


class MyCalendarTwo:

    def __init__(self):
        
        self.lst = []  


    def book(self, start: int, end: int) -> bool:
        
        bisect.insort(self.lst, (start, "start"))
        bisect.insort(self.lst, (end, "end"))
        count = 0
        for _, flag in self.lst:
            count += 1 if flag == "start" else -1
            if count > 2:
                self.lst.remove((start, "start"))
                self.lst.remove((end, "end"))
                return False

        return True




