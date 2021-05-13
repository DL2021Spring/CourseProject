


class Solution:
    def count(self, l):
        return (l-1) * l // 2

    def numberOfArithmeticSlices(self, A):
        
        ret = 0
        if len(A) < 3:
            return ret

        delta = []
        for i in range(1, len(A)):
            delta.append(A[i] - A[i-1])

        s = 0
        e = 0
        while s < len(delta):
            while e < len(delta) and delta[s] == delta[e]:
                e += 1

            l = e - s
            ret += self.count(l)

            s = e

        return ret


if __name__ == "__main__":
    assert Solution().numberOfArithmeticSlices([1, 2, 3, 4]) == 3
