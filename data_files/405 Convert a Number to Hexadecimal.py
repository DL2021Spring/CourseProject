
__author__ = 'Daniel'


class Solution(object):
    def toHex(self, num):
        
        ret = []
        while len(ret) < 8 and num:
            ret.append(self.encode(num & 0xf))
            num >>= 4

        return ''.join(ret[::-1]) or '0'

    def toHexNormal(self, num):
        
        ret = []
        while len(ret) < 8 and num:
            ret.append(self.encode(num % 16))
            num /= 16

        return ''.join(ret[::-1]) or '0'

    def encode(self, d):
        if 0 <= d < 10:
            return str(d)

        return chr(ord('a') + d - 10)


if __name__ == "__main__":
    assert Solution().toHex(-1) == 'ffffffff'
