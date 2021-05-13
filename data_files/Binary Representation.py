
from decimal import *

__author__ = 'Danyang'


class Solution:
    def binaryRepresentation(self, n):
        
        dec_part = ""
        if "." in n:
            int_part, dec_part = n.split(".")
            getcontext().prec = len(dec_part)+1
            dec_part = "."+dec_part
            if not self.is_representable(Decimal(dec_part)):
                return "ERROR"
        else:
            int_part = n

        a = self.natural_num_to_bin(int(int_part))
        b = self.fraction_to_bin(Decimal(dec_part))

        if a == "":
            a = "0"
        if b == "":
            return a
        else:
            return a+"."+b

    @staticmethod
    def natural_num_to_bin(n):
        
        sb = []  
        while n > 0:
            sb.append(n&1)
            n >>= 1

        return "".join(map(str, reversed(sb)))

    @staticmethod
    def fraction_to_bin(n):
        
        sb = []
        while n > 0:
            if len(sb) > 32:
                return "ERROR"
            n *= Decimal(2)
            cur = int(n)
            sb.append(cur)
            n -= Decimal(cur)
        return "".join(map(str, sb))

    @staticmethod
    def is_representable(frac):
        
        while True:
            temp = str(frac).rstrip("0")
            if temp.endswith("."):
                return True
            if not temp.endswith("5"):
                return False
            frac *= Decimal(2)


if __name__ == "__main__":
    assert Solution().binaryRepresentation("0.72") == "ERROR"
    assert Solution().binaryRepresentation("0.125") == "0.001"
    assert Solution().binaryRepresentation("0.6418459415435791") == "ERROR"
