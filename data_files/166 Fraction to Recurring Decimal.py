
__author__ = 'Daniel'


class Solution:
    def fractionToDecimal(self, numerator, denominator):
        
        sign = 1 if numerator*denominator >= 0 else -1
        numerator = abs(numerator)
        denominator = abs(denominator)

        int_part = numerator/denominator
        frac_part = numerator-int_part*denominator

        if frac_part:
            decimal_part = self.frac(numerator-int_part*denominator, denominator)
            ret = str(int_part)+"."+decimal_part
        else:
            ret = str(int_part)

        if sign < 0:
            ret = "-" + ret

        return ret

    def frac(self, num, deno):
        
        ret = []
        d = {}
        i = 0

        while num:
            num *= 10
            q = num/deno
            r = num%deno
            if (q, r) in d:
                ret.append(")")
                ret.insert(d[(q, r)], "(")
                return "".join(ret)

            ret.append(str(q))
            d[(q, r)] = i
            i += 1
            num -= q*deno

        return "".join(ret)


class Solution_error:
    def fractionToDecimal(self, numerator, denominator):
        
        int_part = numerator/denominator
        fract_part = numerator-int_part*denominator
        if fract_part:
            decimal_part = self.frac(numerator-int_part*denominator, denominator)
            ret = str(int_part)+"."+decimal_part
        else:
            ret = str(int_part)

        return ret

    def frac(self, num, deno):
        
        ret = []
        d = {}
        i = 0

        while num:
            l = 0  
            while num < deno:
                num *= 10
                l += 1

            r = num/deno
            if r in d:
                ret.append(")")
                ret.insert(d[r]-(l-1), "(")
                return "".join(ret)

            for _ in xrange(l-1):
                ret.append("0")
                i += 1

            ret.append(str(r))
            d[r] = i
            i += 1
            num -= r*deno

        return "".join(ret)

if __name__ == "__main__":
    assert Solution().fractionToDecimal(1, 333) == "0.(003)"
    assert Solution().fractionToDecimal(1, 90) == "0.0(1)"
    assert Solution().fractionToDecimal(-50, 8) == "-6.25"
    assert Solution().fractionToDecimal(7, -12) == "-0.58(3)