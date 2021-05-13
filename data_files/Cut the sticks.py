
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, A = cipher
        A.sort()

        result = []
        while A:
            result.append(len(A))
            A = map(lambda x: x - A[0], A)
            A = filter(lambda x: x > 0, A)

        return "\n".join(map(str, result))


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    solution = Solution()
    N = int(f.readline().strip())
    A = map(int, f.readline().strip().split(' '))
    cipher = N, A

    
    s = "%s\n" % (solution.solve(cipher))
    print s,
