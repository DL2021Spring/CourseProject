
__author__ = 'Danyang'
MAX_INT = 2147483647
MIN_INT = -2147483648


class Solution:
    def divide(self, dividend, divisor):
        
        
        if divisor == 0 or dividend == 0:
            return 0

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        
        sign = 1 if dividend >= 0 and divisor >= 0 or dividend < 0 and divisor < 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        while dividend >= divisor:
            current_result = 1
            current = divisor  
            while current <= dividend:
                current <<= 1
                current_result <<= 1

            dividend -= current>>1
            result += current_result>>1

        return sign*result


if __name__ == "__main__":
    assert Solution().divide(5, -1) == -5