
__author__ = 'Danyang'


class Solution:
    def singleNumber_optimal(self, A):
        
        bit_0, bit_1, bit_2 = ~0, 0, 0  
        for elmt in A:
            bit_t = bit_2  
            bit_2 = (bit_1 & elmt) | (bit_2 & ~elmt)
            bit_1 = (bit_0 & elmt) | (bit_1 & ~elmt)
            bit_0 = (bit_t & elmt) | (bit_0 & ~elmt)  
        return bit_1

    def singleNumber_array(self, A):
        
        cnt = [0 for _ in xrange(32)]

        for elmt in A:
            for i in xrange(32):
                if elmt>>i&1==1:
                    cnt[i] = (cnt[i]+1)%3

        result = 0
        for i in xrange(32):
            result |= cnt[i]<<i

        return result


    def singleNumber(self, A):
        
        one, two, three = 0, 0, 0

        
        
        
        
        
        

        for elmt in A:
            
            two |= one&elmt
            one ^= elmt
            three = one&two

            one &= ~three
            two &= ~three
        return one






if __name__=="__main__":
    
    tests = [
        [1, 1, 1, 2, 2, 2, 3, 4, 4, 4],
        [1]
    ]
    for A in tests:
        assert Solution().singleNumber_optimal(A)==Solution().singleNumber_array(A)
        assert Solution().singleNumber_optimal(A)==Solution().singleNumber(A)
