
MOD = 10 ** 9 + 7
__author__ = 'Danyang'


class Cost(object):
    def __init__(self):
        self.cost = 0

    def __iadd__(self, other):
        self.cost = (self.cost + other % MOD) % MOD
        return self


class Solution(object):
    def solve(self, cipher):
        
        M, N, Y, X = cipher

        y = list(Y)
        x = list(X)

        y.sort()
        x.sort()
        cost = Cost()
        while x and y:
            x_max = x[-1]
            y_max = y[-1]
            if x_max > y_max:
                cost += x.pop() * (M - len(y))
            elif y_max > x_max:
                cost += y.pop() * (N - len(x))
            else:
                if sum(x) > sum(y):
                    cost += x.pop() * (M - len(y))
                else:
                    cost += y.pop() * (N - len(x))
        while x:
            cost += x.pop() * (M - len(y))
        while y:
            cost += y.pop() * (N - len(x))
        return cost.cost


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        M, N = map(int, f.readline().strip().split(" "))
        Y = map(int, f.readline().strip().split(" "))
        X = map(int, f.readline().strip().split(" "))
        cipher = [M, N, Y, X]
        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
