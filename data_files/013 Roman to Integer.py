
__author__ = 'Danyang'
roman2int = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


class Solution:
    def romanToInt(self, s):
        
        result = 0
        for ind, val in enumerate(s):
            if ind > 0 and roman2int[val] > roman2int[s[ind-1]]:  
                result -= roman2int[s[ind-1]]  
                result += roman2int[val]-roman2int[s[ind-1]]
            else:
                result += roman2int[val]

        return result




