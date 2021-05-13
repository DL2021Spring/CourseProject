



class Solution:
    def idx(self, a):
        return a - 1

    def findDuplicates(self, A):
        
        for i in range(len(A)):
            t = self.idx(A[i])
            while i != t:
                if A[i] == A[t]:
                    break
                else:
                    A[i], A[t] = A[t], A[i]
                    t = self.idx(A[i])

        ret = []
        for i in range(len(A)):
            if self.idx(A[i]) != i:
                ret.append(A[i])

        return ret


if __name__ == "__main__":
    assert set(Solution().findDuplicates([4,3,2,7,8,2,3,1])) == set([2,3])
