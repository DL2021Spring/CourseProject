



class Solution:
    def hammingDistance(self, x, y):
        
        diff = x ^ y
        ret = 0
        while diff:
            ret += diff & 1
            diff >>= 1
            
        return ret


if __name__ == "__main__":
    assert Solution().hammingDistance(3, 1) == 1
    assert Solution().hammingDistance(1, 4) == 2
