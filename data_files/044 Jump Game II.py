
__author__ = 'Danyang'
class Solution:
    def jump_TLE(self, A):
        
        if not A:
            return 0

        length = len(A)
        counter = 0
        dp = [[] for _ in A]

        q = []
        q.append(0)
        while q:
            current_level = q
            q = []
            for ind in current_level:
                if ind>=length-1:
                    return counter
                for j in xrange(ind+1, ind+A[ind]+1):
                    if j not in current_level:  
                        q.append(j)
            counter += 1
        return counter

    def jump(self, A):
        
        length = len(A)
        counter = 0

        start = 0
        end = 1  
        gmax = 0
        while end<length:  
            if not start<end: return 0  
            for i in xrange(start, end):
                gmax = max(gmax, A[i]+i)

            counter += 1
            start = end
            end = gmax+1

        return counter


if __name__=="__main__":
    print Solution().jump([3, 2, 1, 0, 4])
    assert Solution().jump([2,3,1,1,4])==2
