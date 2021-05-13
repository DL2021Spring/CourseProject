

__author__ = 'Danyang'
MOD = 10 ** 9 + 7


class Solution(object):
    def solve_error(self, cipher):
        
        N, lst = cipher
        odd_cnt = len(filter(lambda x: x % 2 == 1, lst))
        even_cnt = N - odd_cnt

        a = (2 ** even_cnt) % MOD

        result = 0
        result += a - 1

        i = 2
        comb = (odd_cnt) * (odd_cnt - 1) / (1 * 2)
        while i <= odd_cnt:
            result += comb * a
            result %= MOD
            i += 2
            comb *= (odd_cnt - i + 1) * (odd_cnt - i) / ((i - 1) * i)
            comb %= MOD

        return result

    def solve(self, cipher):
        
        N, lst = cipher
        odd_cnt = len(filter(lambda x: x % 2 == 1, lst))
        even_cnt = N - odd_cnt

        a = (2 ** even_cnt) % MOD
        b = (2 ** (odd_cnt - 1)) % MOD

        if odd_cnt != 0:
            result = a - 1 + (b - 1) * a
        else:
            result = a - 1

        return result % MOD


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    N = int(f.readline().strip())
    lst = map(int, f.readline().strip().split(' '))
    cipher = N, lst
    
    s = "%s\n" % (Solution().solve(cipher))
    print s,
