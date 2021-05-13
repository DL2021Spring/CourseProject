
import heapq

__author__ = 'Danyang'


class Solution:
    def DeleteDigits(self, A, k):
        
        lst = map(int, list(str(A)))
        i = 0
        while i+1 < len(lst) and k > 0:
            if lst[i] > lst[i+1]:
                del lst[i]
                i -= 1
                if i < 0:
                    i = 0
                k -= 1
            else:
                i += 1
        if k > 0:
            lst = lst[:len(lst)-k]

        return "".join(map(str, lst)).lstrip("0")

    def DeleteDigits_error(self, A, k):
        
        lst = map(int, list(str(A)))
        m = len(lst)-k

        tuples = [(-lst[i], i) for i in xrange(m)]  
        heapq.heapify(tuples)
        for i in xrange(m, len(lst)):
            if -tuples[0][0] > lst[i]:
                heapq.heappop(tuples)
                heapq.heappush(tuples, (-lst[i], i))

        rets = [elt[1] for elt in tuples]
        rets.sort()
        rets = map(lambda x: str(lst[x]), rets)
        return "".join(rets)


if __name__ == "__main__":
    assert Solution().DeleteDigits(10009876091, 4) == "6091"


