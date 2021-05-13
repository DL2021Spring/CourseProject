
__author__ = 'Danyang'


class Solution(object):
    def plusOne(self, digits):
        
        for i in xrange(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            else:
                digits[i] -= 10

        
        digits.insert(0, 1)
        return digits

    def plusOne(self, digits):
        
        digits.reverse()

        digits[0] += 1
        carry = 0
        for i in xrange(len(digits)):  
            digits[i] += carry
            if digits[i] > 9:
                digits[i] -= 10
                carry = 1
            else:
                carry = 0
                break

        if carry:
            digits.append(1)

        digits.reverse()
        return digits


if __name__ == "__main__":
    digits = [9]
    assert Solution().plusOne(digits) == [1, 0]