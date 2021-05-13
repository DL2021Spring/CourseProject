
__author__ = 'Daniel'


class Solution(object):
    def __init__(self):
        self.hours = (1, 2, 4, 8)
        self.minutes = (1, 2, 4, 8, 16, 32)

    def readBinaryWatch(self, num):
        
        def gen():
            for hour_n in xrange(min(num, 4)+1):
                for hour in self.hour(hour_n):
                    for minute in self.minute(num-hour_n):
                        hour = str(hour)
                        minute = ('0' + str(minute))[-2:]
                        yield hour + ':' + minute

        return list(gen())

    def gen(self, n, head, lst, func):
        if head == len(lst):
            yield None

        if n == 0:
            yield 0

        for i in xrange(head, len(lst)):
            for rest in self.gen(n-1, i+1, lst, func):
                if rest is not None:
                    ret = lst[i]+rest
                    if func(ret):
                        yield ret
                    else:
                        break

    def hour(self, n):
        return self.gen(n, 0, self.hours, lambda x: x < 12)

    def minute(self, n):
        return self.gen(n, 0, self.minutes, lambda x: x < 60)


if __name__ == "__main__":
    assert Solution().readBinaryWatch(1) == ['0:01', '0:02', '0:04', '0:08', '0:16', '0:32', '1:00', '2:00', '4:00',
                                             '8:00']
