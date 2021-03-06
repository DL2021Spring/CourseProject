
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, A = cipher
        
        maxa = max(A)
        if maxa < 0:
            return "%d %d" % (maxa, maxa)

        sum_b = sum(filter(lambda x: x > 0, A))

        sum_a = 0
        current_sum = 0
        for a in A:
            current_sum += a
            if current_sum < 0:
                current_sum = 0
            sum_a = max(sum_a, current_sum)

        return "%d %d" % (sum_a, sum_b)


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        N = int(f.readline().strip())
        A = map(int, f.readline().strip().split(' '))
        cipher = N, A
        
        s = "%s\n" % (solution.solve(cipher))
        print s,
