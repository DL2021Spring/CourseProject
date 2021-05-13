
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        start_ptr = 0
        end_ptr = len(cipher) - 1

        cnt = 0
        while start_ptr < end_ptr:
            ord1 = ord(cipher[start_ptr]) - ord('a')
            ord2 = ord(cipher[end_ptr]) - ord('a')
            cnt += abs(ord1 - ord2)
            start_ptr += 1
            end_ptr -= 1

        return cnt


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        
        cipher = f.readline().strip()

        
        s = "%s\n" % (Solution().solve(cipher))
        print s,
