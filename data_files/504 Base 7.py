



class Solution:
    def convertToBase7(self, num):
        
        if num == 0:
            return "0"
        ret = []
        n = abs(num)
        while n:
            ret.append(n % 7)
            n //= 7

        ret = "".join(map(str, ret[::-1]))
        if num < 0:
            ret = "-" + ret

        return ret


if __name__ == "__main__":
    assert Solution().convertToBase7(100) == "202"
    assert Solution().convertToBase7(-7) == "-10"
