

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N = len(cipher)
        sum_set = set()
        s = 0
        for val in cipher:
            s += val
            sum_set.add(s)

        result = []
        for k in sum_set:
            if s % k == 0:
                j = 1
                while j < s / k + 1 and j * k in sum_set:
                    j += 1
                if j == s / k + 1:
                    result.append(k)

        result.sort()  
        return " ".join(map(str, result))


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    N = int(f.readline().strip())


    
    cipher = map(int, f.readline().strip().split(' '))

    
    s = "%s\n" % (Solution().solve(cipher))
    print s,
