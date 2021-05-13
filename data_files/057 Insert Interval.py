
__author__ = 'Danyang'



class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "[%d, %d]" % (self.start, self.end)

    def __repr__(self):
        return repr(self.__str__())


class Solution(object):
    def insert(self, itvls, newItvl):
        s, e = newItvl.start, newItvl.end
        left = filter(lambda x: x.end < s, itvls)
        right = filter(lambda x: x.start > e, itvls)
        if len(left)+len(right) != len(itvls):
            s = min(s, itvls[len(left)].start)
            e = max(e, itvls[-len(right)-1].end)

        return left + [Interval(s, e)] + right

    def insert_itr(self, itvls, newItvl):
        


class SolutionSlow(object):
    def insert(self, itvls, newItvl):
        
        return self.merge(itvls+[newItvl])

    def merge(self, itvls):
        
        itvls.sort(cmp=lambda a, b: a.start - b.start)

        ret = [itvls[0]]
        for cur in itvls[1:]:
            pre = ret[-1]
            if cur.start <= pre.end:  
                pre.end = max(pre.end, cur.end)
            else:
                ret.append(cur)

        return ret


if __name__ == "__main__":
    lst = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    insert = [4, 9]
    lst_interval = []
    for item in lst:
        lst_interval.append(Interval(item[0], item[1]))
    print Solution().insert(lst_interval, Interval(insert[0], insert[1]))
