
__author__ = 'Daniel'


class Solution(object):
    def __init__(self):
        self.table = {
            0: None,
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
        }

    def numberToWords(self, num):
        
        if num == 0: return "Zero"

        ret = []
        self.toWords(num, ret)
        ret = filter(lambda x: x, ret)  
        return " ".join(map(str, ret))

    def toWords(self, num, ret):
        
        SIGS = [1000000000, 1000000, 1000, 100]
        for SIG in SIGS:
            self.partial_parse(num, SIG, ret)
            num %= SIG

        TEN = 10
        if num/TEN > 1:
            ret.append(self.table[(num/TEN)*TEN])

        ret.append(self.table[num%TEN])

    def partial_parse(self, num, sig, ret):
        
        if num/sig:
            prefix = []
            self.toWords(num/sig, prefix)
            ret.extend(prefix)
            ret.append(self.table[sig])


if __name__ == "__main__":
    assert Solution().numberToWords(1234567891) == "One Billion Two Hundred Thirty Four Million Five Hundred Sixty " \
                                                   "Seven Thousand Eight Hundred Ninety One"
