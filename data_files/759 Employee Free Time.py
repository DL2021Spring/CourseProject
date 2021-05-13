

from typing import List
import heapq


S = 0
E = 1


class Solution:
    def employeeFreeTime(self, schedule: List[List[List[int]]]) -> List[List[int]]:
        
        cur_max_end = min(
            itv[E]
            for itvs in schedule
            for itv in itvs
        )
        q = []
        for i, itvs in enumerate(schedule):
            
            j = 0
            itv = itvs[j]
            heapq.heappush(q, (itv[S], i, j))

        ret = []
        while q:
            _, i, j = heapq.heappop(q)
            itv = schedule[i][j]
            if cur_max_end < itv[S]:
                ret.append([cur_max_end, itv[S]])

            cur_max_end = max(cur_max_end, itv[E])

            
            j += 1
            if j < len(schedule[i]):
                itv = schedule[i][j]
                heapq.heappush(q, (itv[S], i, j))

        return ret

    def employeeFreeTime(self, schedule: List[List[List[int]]]) -> List[List[int]]:
        
        
        lst = []
        for itvs in schedule:
            for itv in itvs:
                lst.append([itv[S], S])
                lst.append([itv[E], E])

        lst.sort()
        count = 0
        prev = None
        ret = []
        for t, flag in lst:
            if count == 0 and prev:
                ret.append([prev, t])

            if flag == S:
                count += 1
            else:
                prev = t
                count -= 1

        return ret

    def employeeFreeTime_error(self, schedule: List[List[List[int]]]) -> List[List[int]]:
        
        schedules = list(map(iter, schedule))
        cur_max_end = min(
            itv[E]
            for emp in schedule
            for itv in emp
        )
        q = []
        for emp_iter in schedules:
            itv = next(emp_iter, None)
            if itv:
                heapq.heappush(q, (itv[S], itv, emp_iter))

        ret = []
        while q:
            _, itv, emp_iter = heapq.heappop(q)
            if cur_max_end < itv[S]:
                ret.append([cur_max_end, itv[S]])
            cur_max_end = max(cur_max_end, itv[E])
            itv = next(emp_iter, None)
            if itv:
                heapq.heappush(q, (itv[S], itv, emp_iter))

        return ret


if __name__ == "__main__":
    assert Solution().employeeFreeTime([[[1,2],[5,6]],[[1,3]],[[4,10]]]) == [[3,4]]
    assert Solution().employeeFreeTime([[[4,16],[31,36],[42,50],[80,83],[95,96]],[[4,13],[14,19],[37,53],[64,66],[85,89]],[[17,24],[38,39],[49,51],[62,67],[79,81]],[[9,15],[17,24],[45,63],[65,68],[87,88]],[[17,33],[39,41],[43,57],[58,63],[70,84]]]) == [[36, 37], [68, 70], [84, 85], [89, 95]]
