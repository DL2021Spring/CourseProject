
__author__ = 'Danyang'


class Solution(object):
    def multiply(self, num1, num2):
        
        result = []

        
        if len(num1) > len(num2):  
            return self.multiply(num2, num1)

        
        num1 = map(int, list(num1[::-1]))
        num2 = map(int, list(num2[::-1]))

        
        for d in num1:
            result.append(self.multiply_1_digit(d, num2))

        
        lst = self.add_list(result)

        
        lst.reverse()  
        result = "".join(map(str, lst)).lstrip("0")
        if not result:
            return "0"
        return result

    def multiply_1_digit(self, digit, num):
        
        ret = []

        carry = 0
        for elt in num:
            mul = elt*digit + carry
            carry = mul/10
            mul %= 10
            ret.append(mul)

        if carry != 0:
            ret.append(carry)

        return ret

    def add_list(self, lst):
        
        sig = 0
        ret = [0]
        for ind, val in enumerate(lst):
            for i in xrange(sig): val.insert(0, 0)  
            ret = self.add(ret, val)
            sig += 1
        return ret

    def add(self, num1, num2):
        

        if len(num1) > len(num2):
            return self.add(num2, num1)

        ret = []
        carry = 0
        for idx in xrange(len(num2)):  
            try:
                sm = num1[idx] + num2[idx] + carry
            except IndexError:
                sm = num2[idx] + carry

            carry = sm/10
            ret.append(sm % 10)

        if carry != 0:
            ret.append(carry)

        return ret


if __name__ == "__main__":
    solution = Solution()
    assert [1, 2] == solution.add([2, 1], [9])
    assert str(123*999) == solution.multiply("123", "999")
    assert str(0) == solution.multiply("0", "0")
    assert str(123*456) == solution.multiply("123", "456")
